"""
Model definitions for general application
"""
from django.db import models
#==============================================================================
class Country(models.Model):
    """
    Define countries
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.TextField(null=True)
    abbreviation = models.TextField(null=True, blank=True)
    #--------------------------------------------------------------------------
    def __unicode__(self):
        return '%s' % (self.name)

    #--------------------------------------------------------------------------
    class Meta:

        app_label = 'general'
        verbose_name_plural = "countries"

#==============================================================================
class District(models.Model):
    """
    Define districts
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.TextField(null=True)
    abbreviation = models.TextField(null=True, blank=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    #--------------------------------------------------------------------------
    def __unicode__(self):
        return '%s' % (self.name)

    #--------------------------------------------------------------------------
    class Meta:

        app_label = 'general'