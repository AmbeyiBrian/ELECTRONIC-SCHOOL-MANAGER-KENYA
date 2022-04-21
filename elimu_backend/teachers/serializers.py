from rest_framework import serializers
from teachers.models import teachers


class teachersSerializer(serializers.ModelSerializer):  # It is used to serialize data when creating a teacher account
    class Meta:
        model = teachers
        fields = ('__all__')


class teachersSerializer2(serializers.ModelSerializer):  # It is almsost similar to the one above.
    class Meta:                                              # It is used to serialize  data for a particular teacher
        model = teachers                                 # to a depth of 1. It used when retrieving data
        fields = ('__all__')
        depth = 1


class listTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teachers
        fields = ('__all__')
        depth = 1
