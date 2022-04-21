from django.urls import path
from permisions import views

urlpatterns = [
    path('EditPermision/<int:id>', views.EditPermision.as_view(), name='EditPermision'),
    path('GetPermissions/<int:school>', views.GetPermissions.as_view(), name='GetPermissions'),
]