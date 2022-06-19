from django.urls import path
from timetable import views

urlpatterns = [
    path('timetableAPI/', views.timetableAPI.as_view(), name='timetableAPI'),
    path('timetableAPI/<int:school>', views.timetableAPI.as_view(), name='timetableAPI'),
    path('updateTimeTableAPI/<int:lessonID>', views.updateTimeTableAPI.as_view(), name='updateTimeTableAPI'),
]
