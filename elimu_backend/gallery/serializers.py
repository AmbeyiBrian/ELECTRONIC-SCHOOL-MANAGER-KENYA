from rest_framework import serializers
from gallery.models import Gallery


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = (
            ['school', 'photo', 'description']
        )


class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('__all__')
