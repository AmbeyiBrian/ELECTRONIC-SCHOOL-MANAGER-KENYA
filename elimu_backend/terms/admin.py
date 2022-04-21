from django.contrib import admin
from terms.models import Terms

class TermAdmin(admin.ModelAdmin):
    admin.site.register(Terms)