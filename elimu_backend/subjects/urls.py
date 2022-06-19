from django.urls import path
from subjects import views

urlpatterns = [
    path('subjectsAPI/', views.subjectsAPI.as_view(), name='subjectsAPI'),
    path('subjectsAPI/<int:school>', views.subjectsAPI.as_view(), name='subjectsAPI'),
    path('DeleteAPI/<int:id>', views.DeleteAPI.as_view(), name='DeleteAPI'),

    path('electivesAPI/', views.electivesAPI.as_view(), name='electivesAPI'),
    path('electivesAPI/<int:school>', views.electivesAPI.as_view(), name='electivesAPI'),
    path('DeleteElectiveAPI/<int:id>', views.DeleteElectiveAPI.as_view(), name='DeleteElectiveAPI'),

    # path('SubjectStudentAPI/', views.SubjectStudentAPI.as_view(), name='SubjectStudentAPI'),
]