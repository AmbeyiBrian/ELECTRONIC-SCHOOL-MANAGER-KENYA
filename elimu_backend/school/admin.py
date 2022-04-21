from django.contrib import admin
from school.models import school, principal


class schoolAdmin(admin.ModelAdmin):
    admin.site.register(school)
    readonly_fields = 'activation_code'
    excluded_fields = 'activation_code'


class principalsAdmin(admin.ModelAdmin):
    admin.site.register(principal)
