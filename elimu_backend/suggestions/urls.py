from django.urls import path
from suggestions import views

urlpatterns = [
    path('postAPI/', views.postAPI.as_view(), name='postAPI'),
    path('getAPI/<int:school>', views.getAPI.as_view(), name='getAPI'),
]
