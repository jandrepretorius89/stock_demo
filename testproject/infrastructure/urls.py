from django.conf.urls import patterns, url
from django.contrib import admin

import infrastructure.views
admin.autodiscover()
urlpatterns = patterns('infrastructure.views',
    url(r'^manage/$', 'manage'),
    url(r'^add/$', 'add'),
    url(r'^index/$', 'index'),
    url(r'^profile/(?P<facility_id>\d+)/$', 'profile'),
    url(r'^edit/(?P<facility_id>\d+)/$', 'edit'),
    url(r'^remove/(?P<facility_id>\d+)/$', 'remove'),
)
