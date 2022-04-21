from django.urls import path
from school import views

urlpatterns = [
    path('activationKey/<str:activation_code>', views.schoolActivationKey.as_view(), name='schoolActivationKey'),
    path('get_school_id_and_principal_id/<int:id>', views.get_school_id_and_principal_id.as_view(), name='get_school_id_and_principal_id'),
    path('get_school_details/<int:id>', views.get_school_details.as_view(), name='get_school_details'),
    # path('principalLinkWithSchool/', views.principalLinkWithSchool.as_view(), name='principalLinkWithSchool'),
]