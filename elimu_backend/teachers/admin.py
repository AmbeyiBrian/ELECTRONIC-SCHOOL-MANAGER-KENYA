from django.contrib import admin
from teachers.models import teachers


class teachersAdmin(admin.ModelAdmin):
    admin.site.register(teachers)