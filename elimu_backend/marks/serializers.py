from rest_framework import serializers
from marks.models import Marks


class marksGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'
        depth = 2

class marksPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'
