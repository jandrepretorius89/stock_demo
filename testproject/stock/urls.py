from django.conf.urls import patterns, url

import stock.views

urlpatterns = patterns('stock.views',
    url(r'^manage/$', 'manage'),
    url(r'^add/$', 'add'),
    url(r'^index/$', 'index'),
    url(r'^profile/(?P<stock_item_id>\d+)/$', 'profile'),
    url(r'^remove/(?P<stock_item_id>\d+)/$', 'remove'),
    url(r'^edit/(?P<stock_item_id>\d+)/$', 'edit'),
    url(r'^stock_level/manage_levels/$', 'manageStockLevels'),
    url(r'^stock_level/stock/$', 'indexStockLevelsStock'),
    url(r'^stock_level/facility/$', 'indexStockLevelsFacility'),
    url(r'^stock_level/facility_stock/(?P<stock_item_id>\d+)/$', 'indexStockLevelsFacility'),
    url(r'^stock_level/facility/stock_manage/(?P<facility_id>\d+)/(?P<stock_item_id>\d+)/$', 'allocateStock'),
    url(r'^stock_level/facility/levels/(?P<facility_id>\d+)/$', 'indexFacilityLevels'),
    url(r'^stock_level/remove/(?P<stock_level_id>\d+)/$', 'removeStockLevel'),
    url(r'^under_stocked/$', 'underStocked'),
    url(r'^stock_level/link_stock/(?P<facility_id>\d+)$', 'linkStockLevel'),
)
