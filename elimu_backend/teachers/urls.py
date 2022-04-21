from django.urls import path
from teachers import views

urlpatterns = [
    path('teacherAPI/', views.teacherAPI.as_view(), name="teacherAPI"),
    path('teacherAPI/<int:school>', views.teacherAPI.as_view(), name="teacherAPI"),
    path('teacher_activation_code_validation/<str:activation_code>', views.teacher_activation_code_validation.as_view(), name='teacher_activation_code_validation'),
]