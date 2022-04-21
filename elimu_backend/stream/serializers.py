from rest_framework import serializers
from stream.models import streams


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
