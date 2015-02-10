from infrastructure.models import Employee, Designation, Facility
from django.contrib import admin


class DesignationOptions(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name', ]
    list_filter_ordering = ['name', ]
    search_fieldsets = ['name', ]


class EmployeeOptions(admin.ModelAdmin):
    list_display = ('name', 'get_facility',)
    list_filter = ['name', ]
    list_filter_ordering = ['get_facility', ]
    search_fieldsets = ['name', 'get_facility', ]

    def get_facility(self, obj):
        try:
            return obj.facility.name
        except:
            return ''


class FacilityOptions(admin.ModelAdmin):
    list_display = ('name', 'get_district', 'active')
    list_filter = ['name', ]
    list_filter_ordering = ['name', 'get_district' ]
    search_fieldsets = ['name', 'get_district' ]

    def get_district(self, obj):
        try:
            return obj.district.name
        except:
            return ''

admin.site.register(Employee, EmployeeOptions)
admin.site.register(Designation, DesignationOptions)

admin.site.register(Facility, FacilityOptions)

