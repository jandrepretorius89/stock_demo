from django.contrib import admin
from django.conf.urls import patterns, url, include
import settings

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'general.views.root'),
    url(r'^general/', include('general.urls')),
    url(r'^infrastructure/', include('infrastructure.urls')),
    url(r'^stock/', include('stock.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

