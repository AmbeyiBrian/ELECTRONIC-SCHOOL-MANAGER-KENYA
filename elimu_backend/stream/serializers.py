from rest_framework import serializers
from stream.models import streams, stream_subject_teacher


class getStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = streams
        fields = '__all__'
        depth = 2


class postStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = streams
        fields = (
            ['school', 'class_teacher', 'form', 'stream_name', 'active']
        )


class getStreamSUbjectTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = stream_subject_teacher
        fields = '__all__'

        depth = 2


class postStreamSUbjectTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = stream_subject_teacher
        fields = (
            ['school', 'stream', 'teacher', 'subject']
        )
