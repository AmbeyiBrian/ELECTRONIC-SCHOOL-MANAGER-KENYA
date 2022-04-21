from django.urls import path
from marks import views

urlpatterns = [
    path('PostAPI/', views.PostAPI.as_view(), name='PostAPI'),
    path('PutAPI/<int:school>/<int:year>/<int:term>/<str:mid_end>/<int:student>', views.PutAPI.as_view(), name='PutAPI'),
    path('GetAPI/<int:school>', views.GetAPI.as_view(), name='GetAPI'),
]
