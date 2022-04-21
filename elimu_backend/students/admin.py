from django.contrib import admin
from students.models import students

class studentsAdmin(admin.ModelAdmin):
    admin.site.register(students)