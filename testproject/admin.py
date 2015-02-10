from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'last_login', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
