from django.urls import path
from gallery import views

urlpatterns = [
    path('PostAPI/', views.PostAPI.as_view(), name='PostAPI'),
    path('GetAPI/<int:school>', views.GetAPI.as_view(), name='GetAPI'),
    path('DeleteAPI/<int:id>', views.DeleteAPI.as_view(), name='DeleteAPI')
]