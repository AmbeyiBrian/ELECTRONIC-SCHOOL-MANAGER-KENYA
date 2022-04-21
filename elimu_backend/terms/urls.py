from django.urls import path
from terms import views

urlpatterns = [
    path('termsAPI/<int:school>', views.termsAPI.as_view(), name='termsAPI'),
    path('termsPostAPI/', views.termsPostAPI.as_view(), name='termsPostAPI'),
    path('termPutAPI/<int:id>', views.termPutAPI.as_view(), name='termPutAPI'),
]
