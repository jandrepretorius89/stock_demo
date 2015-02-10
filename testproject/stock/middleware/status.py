"""
Gets an up to date list of under stocked facilities
"""
from stock.stock_cntrl import StockController

#==============================================================================
class GetFacilityStatus(object):
    """
    All views show current stock status if under stocked
    """
    #--------------------------------------------------------------------------
    def process_request(self, request):

        controller = StockController()
        setattr(request.user, 'status', controller.getCurrentStatus())

        return None
