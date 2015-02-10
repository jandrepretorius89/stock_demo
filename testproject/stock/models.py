"""
Model definitions for general application
"""
from django.db import models


#==============================================================================
class StockItem(models.Model):
    """
    Define stock items
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(null=True, max_length=250, blank=True)
    trade_name = models.CharField(null=True, max_length=250, blank=True)
    abbreviation = models.CharField(null=True, max_length=25, blank=True)
    description = models.TextField(null=True, blank=True)

    class_name = models.CharField(null=True, max_length=25, blank=True)
    cas_number = models.CharField(null=True, unique=True, max_length=25, blank=True)
    va_class = models.CharField(null=True, max_length=25, blank=True)
    active = models.BooleanField(blank=True, default=True)
    #--------------------------------------------------------------------------
    def __unicode__(self):
        return '%s' % (self.name)

    #--------------------------------------------------------------------------
    class Meta:

        app_label = 'stock'
    #--------------------------------------------------------------------------
    def save(self, *args, **kwargs):

        super(StockItem, self).save(*args, **kwargs)
        StockLevel.objects.create(stock_item=self)

#==============================================================================
class StockLevel(models.Model):
    """
    Define stock levels
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    stock_item = models.ForeignKey(StockItem, blank=True, null=True)
    facility = models.ForeignKey('infrastructure.Facility', blank=True, null=True)
    minimum_level = models.IntegerField(default=0, blank=True, null=True)
    current_level = models.IntegerField(default=0, blank=True, null=True)
    #--------------------------------------------------------------------------
    def __unicode__(self):
        return '%s' % (self.name)

    #--------------------------------------------------------------------------
    class Meta:

        app_label = 'stock'
        unique_together = ('stock_item', 'facility',)

    #--------------------------------------------------------------------------
    def isLow(self):
        """
        Returns True/False if low or not 
        """
        if self.current_level < self.minimum_level:
            return True

        return False

    @staticmethod
    #--------------------------------------------------------------------------
    def getStockItemFacilityCount(stock_item):
        """
        Returns a count of the total stock over all facilities
        """
        count = 0
        all_items = StockLevel.objects.filter(stock_item=stock_item)
        for item in all_items:
            count = count + item.current_level
        return count
