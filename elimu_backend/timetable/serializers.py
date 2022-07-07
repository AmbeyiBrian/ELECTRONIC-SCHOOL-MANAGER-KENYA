from rest_framework import serializers
from timetable.models import timetable


class postTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = timetable
        fields = (
            ['school', 'stream', 'lesson_number', 'subject', 'day']
        )


class getTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = timetable
        fields = ('__all__')
        depth = 2


class putTimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = timetable
        fields = (['teacher'])

#
# class LessonsListSerializer(serializers.ListSerializer):
#     child = putTimeTableSerializer()
#
#     def update(self, instance, validated_data):
#         lesson_mapping = {lesson.id: lesson for lesson in instance}
#         data_mapping = {item['id']: item for item in validated_data}
#         ret = []
#
#         for lesson_id, data in data_mapping.items():
#             lesson = lesson_mapping.get(lesson_id, None)
#             if lesson is None:
#                 ret.append(self.child.create(data))
#             else:
#                 ret.append(self.child.update(data))
#         return ret
#
