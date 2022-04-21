from rest_framework import serializers
from terms.models import Terms


class postSerializer(serializers.ModelSerializer):
    opening_date = serializers.DateField(format="%d %h %Y")
    closing_date = serializers.DateField(format="%d %h %Y")
    class Meta:
        model = Terms
        fields = '__all__'
