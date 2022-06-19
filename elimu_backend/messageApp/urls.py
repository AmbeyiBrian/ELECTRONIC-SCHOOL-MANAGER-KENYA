from django.urls import path
from messageApp import views

urlpatterns = [
    path('PostMessageAPI/', views.PostMessageAPI.as_view(), name='PostMessageAPI'),
    path('GetMessageAPI/<int:school_id>', views.PostMessageAPI.as_view(), name='GetMessageAPI'),
]