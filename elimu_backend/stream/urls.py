from django.urls import path
from stream import views

urlpatterns = [
    path('streamAPI/', views.streamAPI.as_view(), name='streamAPI'),
    path('streamAPI/<int:school>', views.streamAPI.as_view(), name='streamAPI'),
    path('streamPutAPI/<int:streamID>', views.streamPutAPI.as_view(), name='streamPutAPI'),
]