'''
Created on 07 Feb 2015

@author: JANDRE-PRETORIUS
'''

from django.db.models import Count
import stock.models
import infrastructure.models
import decimal
#==============================================================================
class StockController(object):
    """
    Controller for all stock management 
    """
    #--------------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        pass
    #--------------------------------------------------------------------------
    def getAllStock(self):
        """
        """
        return stock.models.StockItem.objects.filter(active=True)
    #--------------------------------------------------------------------------
    def getStockItem(self, s_id):
        """
        """
        if not s_id:
            return None

        return stock.models.StockItem.objects.get(pk=s_id, active=True)

    #--------------------------------------------------------------------------
    def remove(self, f_id=None, f_object=None):
        """
        Returns a single stock item object based on provided id
        """
        try:
            if f_id:
                stockitem = stock.models.StockItem.objects.get(pk=f_id)
                stockitem.active = False
                stockitem.save()
        except:
            return

        return
    #--------------------------------------------------------------------------
    def getAllStockLevelsPerItem(self):
        """
        """
        result = {}
        items = stock.models.StockLevel.objects.filter(stock_item__active=True).values('stock_item').annotate(total=Count('facility')).order_by('stock_item')
        for item in items:
            stock_item = stock.models.StockItem.objects.get(pk=int(item['stock_item']))
            stock_item_facility_count = item['total']
            total_stock = stock.models.StockLevel.getStockItemFacilityCount(stock_item)
            average_stock = total_stock / stock_item_facility_count if stock_item_facility_count else 0
            average_stock = decimal.Decimal(str(average_stock), 2)

            result[stock_item] = {
                'item':stock_item.name,
                'facility_count':stock_item_facility_count,
                'total':total_stock,
                'average':average_stock
            }

        return result

    #--------------------------------------------------------------------------
    def getAllStockLevelsPerFacility(self, facility_id=None):
        """
        """
        if facility_id:
            all_facilities = infrastructure.models.Facility.objects.filter(active=True, pk=facility_id)
        else:
            all_facilities = infrastructure.models.Facility.objects.filter(active=True)

        result = []

        for facility in all_facilities:
            levels = facility.getAllStockLevels()
            for level in levels:
                result.append([
                    facility.name,
                    level.stock_item.name,
                    level.current_level,
                    level.minimum_level,
                    level.isLow(),
                    level.facility.id,
                    level.stock_item.id,
                    ]
               )
        return result

    #--------------------------------------------------------------------------
    def getAllStockLevelsPerStockPerFacility(self, stock_id):
        """
        Return all the facilities stocking a specific item
        """
        all_levels = stock.models.StockLevel.objects.filter(stock_item__id=stock_id)

        result = []

        for level in all_levels:
            if level.facility:
                levels = level.facility.getAllStockLevels(stock_id=stock_id)
                for stock_level in levels:
                    result.append([
                        stock_level.facility.name,
                        stock_level.stock_item.name,
                        stock_level.current_level,
                        stock_level.minimum_level,
                        stock_level.isLow(),
                        stock_level.facility.id,
                        stock_level.stock_item.id,
                        ]
                   )
        return result
    #--------------------------------------------------------------------------
    def getFacility(self, facility_id):
        """
        """
        try:
            return infrastructure.models.Facility.objects.get(pk=facility_id)
        except:
            return None

    #--------------------------------------------------------------------------
    def getFacilityStock(self, facility_id, stock_item_id):
        """
        """
        try:
            return stock.models.StockLevel.objects.get(facility__id=facility_id, stock_item__id=stock_item_id)
        except:
            return None
    #--------------------------------------------------------------------------
    def getStockLevel(self, stock_level_id):
        """
        """
        try:
            return stock.models.StockLevel.objects.get(pk=stock_level_id)
        except:
            return None

    #--------------------------------------------------------------------------
    def updateStock(self, facility_id, stock_item_id, post):
        """
        Update a stock item's levels for a facility
        """
        try:
            level = stock.models.StockLevel.objects.get(facility__id=facility_id, stock_item__id=stock_item_id)
            if post['current_level']:
                level.current_level = int(post['current_level'])
            if post['min_level']:
                level.minimum_level = int(post['min_level'])

            level.save()
            return True
        except:
            return False

    #--------------------------------------------------------------------------
    def cleanUpdate(self, post):
        """
        Some validation on an update post
        """
        current_level_error = False
        min_level_error = False
        try:
            c_level = post['current_level']
            if c_level:
                c_level = int(post['current_level'])
                if c_level < 0:
                    current_level_error = True
        except:
            current_level_error = True

        try:
            m_level = post['min_level']
            if m_level:
                m_level = int(post['min_level'])
                if m_level < 0:
                    min_level_error = True
        except:
            min_level_error = True

        if current_level_error or min_level_error:
            return False, "Please ensure that values are positive, whole integers."

        return True, ''
    #--------------------------------------------------------------------------
    def getZeroLevel(self, stock_level_id):
        """
        Zeros a level
        """
        try:
            level = self.getStockLevel(stock_level_id)
            level.current_level = 0
            level.minimum_level = 0
            level.save()
            return True
        except:
            return False


    #--------------------------------------------------------------------------
    def getCurrentStatus(self):
        """
        Gets the current count of under stocked facilities
        """
        result = []
        levels = []
        facilities = []
        stock_items = stock.models.StockItem.objects.filter(active=True)
        for item in stock_items:
            levels.append(self.getAllStockLevelsPerStockPerFacility(item.id))
        for sub_levels in levels:
            for level in sub_levels:
                if level[4]:
                    if level[0] not in facilities:
                        facilities.append(level[0])
                    result.append(level)

        return [result, len(facilities)]




