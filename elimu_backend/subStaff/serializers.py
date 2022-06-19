from rest_framework import serializers
from subStaff.models import SubStaff


class SubStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubStaff
        fields = '__all__'


class SubStaffSerializer2(serializers.ModelSerializer):
    class Meta:
        model = SubStaff
        fields = '__all__'
        depth = 1
