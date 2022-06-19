from rest_framework import serializers
from subjects.models import optional_subjects, electives


class getSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = optional_subjects
        fields = '__all__'


class postSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = optional_subjects
        fields = (
            ['school', 'group', 'subject_name']
        )

class getElectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = electives
        fields = '__all__'


class postElectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = electives
        fields = (
            ['school', 'elective', 'subject_name']
        )


# class PostSubjectStudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=SubjectStudent
#         fields=(['student', 'subject'])
