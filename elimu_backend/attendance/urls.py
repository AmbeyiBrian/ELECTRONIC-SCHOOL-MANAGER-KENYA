from django.urls import path
from attendance import views

urlpatterns = [
    path('attendanceAPI/', views.attendanceAPI.as_view(), name='attendanceAPI'),
    path('attendanceAPI/<int:school>', views.attendanceAPI.as_view(), name='attendanceAPI'),
    path('attendanceAPI/<int:student>/<str:date>', views.attendanceAPI.as_view(), name='attendanceAPI'),
    path('attendanceAPI2/<int:school>', views.attendanceAPI2.as_view(), name='attendanceAPI2'),
]
