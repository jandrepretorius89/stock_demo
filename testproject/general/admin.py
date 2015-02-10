from general.models import Country, District
from django.contrib import admin

class DistrictOptions(admin.ModelAdmin):
    list_display = ('name', 'get_country',)


    list_filter = ['name', ]
    list_filter_ordering = ['get_country', ]
    search_fieldsets = ['name', 'get_country', ]

    def get_country(self, obj):
        return obj.country.name

class DistrictInline(admin.StackedInline):
    model = District
    extra = 5


class CountryOptions(admin.ModelAdmin):
    inlines = [DistrictInline, ]
    list_display = ('name',)
    list_filter = ['name', ]
    search_fieldsets = ['name', ]


admin.site.register(Country, CountryOptions)
admin.site.register(District, DistrictOptions)



