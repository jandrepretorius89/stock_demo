'''
Created on 07 Feb 2015

@author: JANDRE-PRETORIUS
'''

import infrastructure.models
#==============================================================================
class FacilityController(object):
    """
    Controller for all facility management 
    """
    #--------------------------------------------------------------------------
    def getAllFacilities(self):
        """
        Returns all active facilities of any type
        """
        return infrastructure.models.Facility.objects.all().filter(active=True)
    #--------------------------------------------------------------------------
    def getFacility(self, f_id):
        """
        Returns a single, active facility object based on provided id
        """
        try:
            if f_id:
                return infrastructure.models.Facility.objects.get(pk=f_id, active=True)
        except:
            return None

        return None
    #--------------------------------------------------------------------------
    def remove(self, f_id=None, f_object=None):
        """
        "Removes" a facility by deactivating it.
        """
        try:
            if f_id:
                facility = infrastructure.models.Facility.objects.get(pk=f_id)
                facility.active = False
                facility.save()
        except:
            return

        return




