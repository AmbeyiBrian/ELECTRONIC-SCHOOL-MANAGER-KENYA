from django.urls import path
from rest_framework import routers
from user_accounts import views

router = routers.DefaultRouter()
# router.register('users', user_viewsets)

urlpatterns = [
    path('create_user/', views.create_user.as_view(), name='create_user'),
    path('login_user/', views.login_user.as_view(), name='login_user'),
    path('logout_user/<str:email_address>', views.logout_user.as_view(), name='logout_user'),
    path('GetUserInfoAPI/<str:email_address>', views.GetUserInfoAPI.as_view(), name='GetUserInfoAPI'),
    # path('get_principalesID/<str:email_address>', views.get_principalesID.as_view(), name='get_principalesID'),
]
