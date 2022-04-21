from rest_framework import serializers
from students.models import students


class postStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = (
            ['school', 'stream', 'admission_number', 'first_name', 'last_name', 'gender', 'kcpe_marks', 'activation_code', 'status']
        )


class getStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'
        depth=1
