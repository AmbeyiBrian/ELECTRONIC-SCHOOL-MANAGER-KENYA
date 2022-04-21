from rest_framework import serializers
from events.models import events


class getSerializer(serializers.ModelSerializer):
    date_of_event = serializers.DateTimeField(format="%d %h %Y %H:%M")
    date_created = serializers.DateTimeField(format="%d %h %Y %H:%M")

    class Meta:
        model = events
        fields = '__all__'


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = events
        fields = (
            ['school', 'date_of_event', 'event_description', 'title', 'target_audience']
        )
