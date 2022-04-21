from rest_framework import serializers
from permisions.models import Permissions


class GetPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = '__all__'


class PutPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = (['update_timetable', 'add_edit_stream', 'add_edit_student', 'create_event', 'add_edit_teacher',
                   'edit_school_info', 'add_delete_gallery'])
