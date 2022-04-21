from rest_framework import serializers
from marks.models import Marks


class marksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'
