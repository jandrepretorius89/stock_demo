"""
Handler for infrastructure view functionality
"""
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect as redirect

from infrastructure.forms import FacilityForm
from infrastructure.models import Facility
import infrastructure.facility_cntrl
#------------------------------------------------------------------------------
def manage(request):
    """
    Landing page for infrastructure
    """
    return render_to_response(
        'infrastructure/manage.html',
        {
        },
        context_instance=RequestContext(request)
    )

#------------------------------------------------------------------------------
def add(request):
    """
    Add a facility
    """
    if request.method == "POST":
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save(False)
            return redirect('/infrastructure/index/?msg=Successfully created a new facility')
    else:
        form = FacilityForm()

    return render_to_response(
        'infrastructure/add.html',
        {
         'form':form,
        },
        context_instance=RequestContext(request)
    )


#------------------------------------------------------------------------------
def index(request):
    """
    List all facilities
    """
    controller = infrastructure.facility_cntrl.FacilityController()
    facilities = controller.getAllFacilities().order_by('name', 'district__name', 'district__country__name')
    message = request.GET.get('msg')
    return render_to_response(
        'infrastructure/index.html',
        {
         'message':message,
         'facilities':facilities,
        },
        context_instance=RequestContext(request)
    )

#------------------------------------------------------------------------------
def profile(request, **kwargs):
    """
    Profile a facility
    """
    try:
        facility = Facility.objects.get(pk=int(kwargs.get('facility_id')))
    except:
        return redirect('/infrastructure/index/?msg=No matching facility found')

    return render_to_response(
        'infrastructure/facility_profile.html',
        {
         'facility':facility,
        },
        context_instance=RequestContext(request)
    )
#------------------------------------------------------------------------------
def edit(request, **kwargs):
    """
    Edit a facility
    """
    controller = infrastructure.facility_cntrl.FacilityController()
    facility = controller.getFacility(kwargs.get('facility_id'))

    existing = True
    save_error_name = None

    if request.method == "POST":
        form = FacilityForm(request.POST, existing_flag=existing)
        if form.is_valid():
            try:
                form.save(facility)
                return redirect('/infrastructure/index/?msg=Successfully updated')
            except:
                save_error_name = "The name selected is an existing facility, please try again."

    else:

        if facility:
            form = FacilityForm(instance=facility)
        else:
            form = FacilityForm()

    return render_to_response(
        'infrastructure/add.html',
        {
         'existing':True,
         'form':form,
         'message':save_error_name,
        },
        context_instance=RequestContext(request)
    )
#------------------------------------------------------------------------------
def remove(request, **kwargs):
    """
    "Remove a facility
    """
    try:
        controller = infrastructure.facility_cntrl.FacilityController()
        controller.remove(f_id=kwargs.get('facility_id'))

    except:
        return redirect('/infrastructure/index/?msg=No matching facility found')


    return redirect('/infrastructure/index/?msg=Successfully Removed')
