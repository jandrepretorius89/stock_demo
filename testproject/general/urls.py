from django.conf.urls import patterns, url

import general.views
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('general.views',
    url(r'^landing/$', 'landing'),
)
