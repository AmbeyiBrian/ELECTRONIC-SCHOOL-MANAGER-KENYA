from django.urls import path
from stream import views

urlpatterns = [
    path('streamAPI/', views.streamAPI.as_view(), name='streamAPI'),
    path('streamAPI/<int:school>', views.streamAPI.as_view(), name='streamAPI'),
    path('streamPutAPI/<int:streamID>', views.streamPutAPI.as_view(), name='streamPutAPI'),
    path('streamSubjectTeacherAPI/', views.streamSubjectTeacherAPI.as_view(), name='streamSubjectTeacherAPI'),
    path('streamSubjectTeacherAPI/<int:streamID>', views.streamSubjectTeacherAPI.as_view(), name='streamSubjectTeacherAPI'),
    path('streamSubjectTeacherPutAPI/<int:selected_stream_teacher_subject_id>', views.streamSubjectTeacherAPI.as_view(), name='streamSubjectTeacherPutAPI'),
    path('streamSubjectTeacherGetAPI/<int:school>', views.streamSubjectTeacherGetAPI.as_view(), name='streamSubjectTeacherGetAPI'),
]