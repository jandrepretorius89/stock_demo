"""
Handler for general site-wide view functionality
"""
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect as redirect
from django.template.context import RequestContext
from stock.stock_cntrl import StockController
from stock.forms import StockForm, StockLevelForm
from django.db import IntegrityError
#------------------------------------------------------------------------------
def manage(request):
    """
    Manage stock page
    """
    return render_to_response(
        'stock/manage.html',
        {
        },
        context_instance=RequestContext(request)
    )

#------------------------------------------------------------------------------
def add(request):
    """
    Add new stock items
    """

    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save(False)
            return redirect('/stock/index/?msg=Successfully created a new stock item')
    else:
        form = StockForm()


    return render_to_response(
        'stock/add.html',
        {
         'form':form,
        },
        context_instance=RequestContext(request)
    )


#------------------------------------------------------------------------------
def index(request):
    """
    List all stock items
    """
    controller = StockController()
    stock = controller.getAllStock().order_by('name')
    message = request.GET.get('msg')
    return render_to_response(
        'stock/index.html',
        {
         'message':message,
         'stock':stock,
        },
        context_instance=RequestContext(request)
    )
#------------------------------------------------------------------------------
def profile(request, **kwargs):
    """
    Profile a stock item
    """
    controller = StockController()

    try:
        stock_item = controller.getStockItem(int(kwargs.get('stock_item_id')))
    except:
        return redirect('/stock/index/?msg=No matching stock item found')

    return render_to_response(
        'stock/stock_profile.html',
        {
         'stock_item':stock_item,
        },
        context_instance=RequestContext(request)
    )
#------------------------------------------------------------------------------
def remove(request, **kwargs):
    """
    Remove a stock item
    """
    try:
        controller = StockController()
        controller.remove(f_id=kwargs.get('stock_item_id'))

    except:
        return redirect('/stock/index/?msg=No matching stock item found')


    return redirect('/stock/index/?msg=Successfully Removed')

#------------------------------------------------------------------------------
def edit(request, **kwargs):
    """
    Edit a stock Item
    """
    controller = StockController()
    stock = controller.getStockItem(kwargs.get('stock_item_id'))
    existing = True
    save_error_name = None
    if request.method == "POST":
        form = StockForm(request.POST, existing_flag=existing)
        if form.is_valid():
            try:
                form.save(stock)
                return redirect('/stock/index/?msg=Successfully updated')
            except:
                save_error_name = "The name selected is an existing stock item, please try again."

    else:

        if stock:
            form = StockForm(instance=stock)
        else:
            form = StockForm()

    return render_to_response(
        'stock/add.html',
        {
         'existing':True,
         'form':form,
         'message':save_error_name,
        },
        context_instance=RequestContext(request)
    )
#------------------------------------------------------------------------------
def indexStockLevelsStock(request):
    """
    List all stock levels
    """
    controller = StockController()
    stock_levels = controller.getAllStockLevelsPerItem()
    return render_to_response(
        'stock_level/index_per_item.html',
        {
         'stock_levels':stock_levels,
        },
        context_instance=RequestContext(request)
    )
#------------------------------------------------------------------------------
def manageStockLevels(request):
    """
    Manage stock levles page
    """
    return render_to_response(
        'stock_level/manage.html',
        {
        },
        context_instance=RequestContext(request)
    )

#------------------------------------------------------------------------------
def indexStockLevelsFacility(request, **kwargs):
    """
    List all stock levels per facility
    """
    stock_id = kwargs.get('stock_item_id')
    controller = StockController()
    if stock_id:
        stock_levels = controller.getAllStockLevelsPerStockPerFacility(stock_id)
    else:
        stock_levels = controller.getAllStockLevelsPerFacility()
    return render_to_response(
        'stock_level/index_per_facility.html',
        {
         'stock_levels':stock_levels,
        },
        context_instance=RequestContext(request)
    )
#------------------------------------------------------------------------------
def indexFacilityLevels(request, **kwargs):
    """
    List all stock levels for a specific facility
    """
    facility_id = kwargs.get('facility_id')
    controller = StockController()
    stock_levels = controller.getAllStockLevelsPerFacility(facility_id=facility_id)
    facility = controller.getFacility(facility_id)
    return render_to_response(
        'stock_level/index_per_facility.html',
        {
         'stock_levels':stock_levels,
         'facility':facility,
         'facility_true':True,
        },
        context_instance=RequestContext(request)
    )
#------------------------------------------------------------------------------
def allocateStock(request, **kwargs):
    """
    Allocate stock to a facility
    """
    facility_id = kwargs.get('facility_id')
    stock_item_id = kwargs.get('stock_item_id')
    controller = StockController()
    message = request.GET.get('msg')
    if facility_id and stock_item_id:
        facility_stock = controller.getFacilityStock(facility_id, stock_item_id)

        if not facility_stock:
            return redirect('/infrastructure/index/?msg=Facility not found')
    elif facility_id:
        return redirect('/stock/stock_level/link_stock/%s' % facility_id)
    else:
        return redirect('/infrastructure/index/?msg=Facility not found')
    if request:
        if request.method == "POST":
            clean, message = controller.cleanUpdate(request.POST)

            if message and not clean:
                return redirect('/stock/stock_level/facility/stock_manage/%s/%s/?msg=%s' % (facility_stock.facility_id, facility_stock.stock_item.id, message))

            if not controller.updateStock(facility_id, stock_item_id, request.POST):
                message = 'An error has occurred, please try again.'
            else:
                return redirect('/stock/stock_level/facility/stock_manage/%s/%s/?msg=%s' % (facility_stock.facility_id, facility_stock.stock_item.id, "Successfully updated"))

    return render_to_response(
        'stock_level/allocate_stock.html',
        {
         'facility_stock':facility_stock,
         'message':message,
        },
        context_instance=RequestContext(request)
    )
#------------------------------------------------------------------------------
def removeStockLevel(request, **kwargs):
    """
    Zero a specific stock level
    """
    stock_level_id = kwargs.get('stock_level_id')
    controller = StockController()
    if stock_level_id:
        result = controller.getZeroLevel(stock_level_id)
        level = controller.getStockLevel(stock_level_id)
        if not result:
            message = "Could not update stock"
        else:
            message = "Successfully updated"
    else:
        return redirect('/infrastructure/index/?msg=Could not zero stock')


    return redirect('/stock/stock_level/facility/stock_manage/%s/%s/?msg=%s' % (level.facility_id, level.stock_item.id, "Successfully updated"))

#------------------------------------------------------------------------------
def underStocked(request):
    """
    All under stocked facilities
    """
    try:
        stock_levels = request.user.status[0]
    except:
        controller = StockController()
        stock_levels = controller.getAllStockLevelsPerFacility()


    return render_to_response(
        'stock_level/index_per_facility.html',
        {
         'stock_levels':stock_levels,
        },
        context_instance=RequestContext(request)
    )

#------------------------------------------------------------------------------
def linkStockLevel(request, **kwargs):
    """
    Link a level with facility and stock
    """
    form = StockLevelForm()
    save_error_name = ''

    controller = StockController()
    facility = controller.getFacility(kwargs.get('facility_id'))
    if request.method == "POST":
        form = StockLevelForm(request.POST)
        if form.is_valid():
            try:
                controller = StockController()
                stock_item = controller.getStockItem(request.POST.get('stock_item'))
                form.save(stock_item, facility)
                return redirect('/stock/stock_level/facility/levels/%s/' % facility.id)
            except IntegrityError:
                save_error_name = "The combination selected already exists. View facility profile to adjust levels."
            except:
                save_error_name = "The name selected is an existing stock item, please try again."
    return render_to_response(
        'stock_level/link_stock.html',
        {
         'form':form,
         'save_error_name':save_error_name,
         'facility':facility,
        },
        context_instance=RequestContext(request)
    )
