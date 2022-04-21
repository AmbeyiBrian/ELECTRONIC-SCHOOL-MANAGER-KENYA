from django.urls import path
from events import views

urlpatterns = [
    # path('eventsAPI/', views.eventsAPI.as_view(), name='eventsAPI'),
    path('school_events/', views.school_events.as_view(), name='school_events'),
    path('school_events/<int:school>', views.school_events.as_view(), name='school_events'),
]
