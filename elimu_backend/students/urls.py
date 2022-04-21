from django.urls import path
from students import views

urlpatterns = [
    path('studentsAPI/', views.studentsAPI.as_view(), name='studentsAPI'),
    path('studentsAPI/<int:school>', views.studentsAPI.as_view(), name='studentsAPIGet'),
    path('studentSearchAPI/<str:searchText>', views.studentSearchAPI.as_view(), name='studentSearchAPI'),
    path('getStudent/<int:studentID>', views.getStudent.as_view(), name='studentID'),
]