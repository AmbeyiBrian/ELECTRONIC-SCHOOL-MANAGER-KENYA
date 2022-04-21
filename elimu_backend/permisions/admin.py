from django.contrib import admin
from permisions.models import Permissions

class PermissionAdmin(admin.ModelAdmin):
    admin.site.register(Permissions)