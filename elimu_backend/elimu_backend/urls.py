from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('user_accounts.urls')),
    re_path('teachers/', include('teachers.urls')),
    re_path('school/', include('school.urls')),
    re_path('timetable/', include('timetable.urls')),
    re_path('stream/', include('stream.urls')),
    re_path('students/', include('students.urls')),
    re_path('events/', include('events.urls')),
    re_path('gallery/', include('gallery.urls')),
    re_path('terms/', include('terms.urls')),
    re_path('permisions/', include('permisions.urls')),
    re_path('suggestions/', include('suggestions.urls')),
    re_path('marks/', include('marks.urls')),
    re_path('subjects/', include('subjects.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
