from rest_framework import serializers
from messageApp.models import Message


class GetMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class PostMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (['school', 'message', 'target_audience', 'sms', 'creator'])
