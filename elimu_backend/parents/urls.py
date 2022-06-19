from django.urls import path
from parents import views

urlpatterns = [
    path('ParentAPI/<str:activation_code>', views.ParentAPI.as_view(), name='ParentAPI'),
    path('ParentStudentValidationAPI/<str:parent>', views.ParentStudentValidationAPI.as_view(), name='ParentStudentValidationAPI'),
    path('ParentPutAPI/<str:activation_code>', views.ParentAPI.as_view(), name='ParentPutAPI'),
]