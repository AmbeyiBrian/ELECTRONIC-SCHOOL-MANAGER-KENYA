from django.urls import path
from fee import views

urlpatterns = [
    path('FeeAPI/', views.FeeAPI.as_view(), name='FeeAPI'),
    path('FeeAPI/<int:school>', views.FeeAPI.as_view(), name='FeeAPI'),
    path('PutAPI/<int:id>', views.PutAPI.as_view(), name='PutAPI'),
    path('DeleteAPI/<int:id>', views.DeleteAPI.as_view(), name='DeleteAPI'),
    path('FeeStatementAPI/', views.FeeStatementAPI.as_view(), name='FeeStatementAPI'),
    path('FeeStatementAPI/<int:school>', views.FeeStatementAPI.as_view(), name='FeeStatementAPI'),
    path('MpesaAPI/', views.MpesaAPI.as_view(), name='MpesaAPI'),

    path('index', views.index, name='index'),
    path('daraja/stk_push_callback', views.stk_push_callback, name='stk_push_callback')
]