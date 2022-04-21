from rest_framework import serializers
from suggestions.models import Suggestions


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = (['user', 'school', 'suggestion'])


class getSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d %h %Y %H:%M")
    class Meta:
        model = Suggestions
        fields = '__all__'
