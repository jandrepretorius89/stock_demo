"""
Model definitions for general application
"""
from django.db import models

import general.models
import stock.models
import infrastructure.constants


#==============================================================================
class Facility(models.Model):
    """
    Define facilities
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=128, blank=True, default='', unique=True)
    abbreviation = models.CharField(max_length=128, blank=True, default='')
    type = models.IntegerField('Facility Type', choices=infrastructure.constants.FACILITY_TYPES, default=infrastructure.constants.FACILITY_TYPE_CLINIC, blank=True)

    postal_address = models.CharField(max_length=128, blank=True, default='')
    district = models.ForeignKey(general.models.District, blank=True, null=True)
    active = models.BooleanField(blank=True, default=True)
    #--------------------------------------------------------------------------
    def __unicode__(self):
        return '%s' % (self.name)

    #--------------------------------------------------------------------------
    class Meta:

        app_label = 'infrastructure'

    #--------------------------------------------------------------------------
    def getType(self):
        return '%s' % dict(infrastructure.constants.FACILITY_TYPES)[self.type]
    #--------------------------------------------------------------------------
    def getManager(self):
        """
        Returns an employee object of type manager linked to self.
        """
        try:
            manager = Employee.objects.filter(facility=self, designation__name='Manager')[0]
            return '%s %s' % (str(manager.name) , str(manager.last_name))
        except:
            return None
    #--------------------------------------------------------------------------
    def getManagerNumber(self):
        """
        Get self's manager's number
        """
        try:
            manager = Employee.objects.filter(facility=self, designation__name='Manager')[0]
            return manager.contact_number
        except:
            return None

    #--------------------------------------------------------------------------
    def getAllStockLevels(self, stock_id=None):
        """
        All stock levels for a facility for a specific stock item
        """
        if stock_id:
            return stock.models.StockLevel.objects.filter(stock_item__id=stock_id, facility=self, stock_item__active=True)

        levels = stock.models.StockLevel.objects.filter(facility=self, stock_item__active=True)

        return levels
#==============================================================================
class Designation(models.Model):
    """
    Define employee designations
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, blank=True, default='')

    #--------------------------------------------------------------------------
    def __unicode__(self):
        return '%s' % (self.name)

    #--------------------------------------------------------------------------
    class Meta:
        app_label = 'infrastructure'

#==============================================================================
class Employee(models.Model):
    """
    Define employee
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=128, blank=True, default='')
    last_name = models.CharField(max_length=128, blank=True, default='')
    title = models.CharField(max_length=128, blank=True, default='')
    identification_number = models.CharField(max_length=128, blank=True, default='')
    designation = models.ForeignKey(Designation, blank=True, null=True)
    facility = models.ForeignKey(Facility, blank=True, null=True)

    contact_number = models.CharField(max_length=128, blank=True, default='')
    email = models.CharField(max_length=128, blank=True, default='')
    #--------------------------------------------------------------------------
    def __unicode__(self):
        return '%s' % (self.name)

    #--------------------------------------------------------------------------
    class Meta:

        app_label = 'infrastructure'
