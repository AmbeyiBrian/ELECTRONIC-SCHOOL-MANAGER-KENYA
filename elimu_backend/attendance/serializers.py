from rest_framework.serializers import ModelSerializer
from attendance.models import attendanceSheet


class postSerializer(ModelSerializer):
    class Meta:
        model = attendanceSheet
        fields = (
            ['student', 'date', 'present']
        )


class getSerializer(ModelSerializer):
    class Meta:
        model = attendanceSheet
        fields = '__all__'


class getSerializer2(ModelSerializer):
    class Meta:
        model = attendanceSheet
        fields = '__all__'

        depth = 2
