from django.urls import path
from subStaff import views

urlpatterns = [
    path('getSubStaff/<int:school>', views.SubStaffAPI.as_view(), name='getSubStaff'),
    path('postSubStaff/', views.SubStaffAPI.as_view(), name='postSubStaff'),
    path('ActivationKeyValidation/<str:activation_code>', views.ActivationKeyValidation.as_view(), name='ActivationKeyValidation'),
]
