"""
Handler for general site-wide view functionality
"""
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect as redirect
from django.template.context import RequestContext

#------------------------------------------------------------------------------
def root(request):
    """
    Root requests 
    """
    return redirect('general/landing/')

#------------------------------------------------------------------------------
def landing(request):
    """
    Landing page
    """

    return render_to_response(
        'general/home.html',
        {
        },
        context_instance=RequestContext(request)
    )

