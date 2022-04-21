from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from timetable.serializers import postTimeTableSerializer, getTimeTableSerializer, putTimeTableSerializer
from timetable.models import timetable
from teachers.models import teachers


class timetableAPI(APIView):
    permission_classes = ()
    serializer_class = postTimeTableSerializer

    def post(self, request):
        serializer = postTimeTableSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    def get(self, request, school):
        lessons = timetable.objects.filter(school=school).order_by('lesson_number')
        serializer = getTimeTableSerializer(lessons, many=True)
        return Response(serializer.data)


class updateTimeTableAPI(APIView):
    permission_classes = ()

    def get(self, request, lessonID):
        try:
            lesson = timetable.objects.get(id=lessonID)
            data = postTimeTableSerializer(lesson).data
        except:
            return ValueError
        else:
            return Response(data)

    def put(self, request, lessonID, format=None):
        lesson = timetable.objects.get(id=lessonID)
        serializer = postTimeTableSerializer(lesson, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors)


class UpdateSubjectTeacher4StreamAPI(APIView):
    permission_classes = ()
    serializer_class = putTimeTableSerializer

    def get(self, request, school, stream_id, subject):
        lessons = timetable.objects.filter(school=school, stream=stream_id, subject=subject)
        data = postTimeTableSerializer(lessons, many=True).data
        return Response(data)

    def get_object(self, obj_id):
        try:
            return timetable.objects.get(id=obj_id)
        except:
            raise status.HTTP_400_BAD_REQUEST

    def validate_ids(self, id_list):
        for id in id_list:
            try:
                timetable.objects.get(id=id)
            except:
                raise status.HTTP_400_BAD_REQUEST
        return True

    def put(self, request, school, stream_id, subject, format=None):
        lessons = timetable.objects.filter(school=school, stream=stream_id, subject=subject).values_list('id',
                                                                                                         flat=True)
        data = lessons

        id_list = data
        self.validate_ids(id_list=id_list)
        instances = []

        for id in id_list:
            obj = self.get_object(obj_id=id)
            obj.teacher = teachers.objects.get(id=request.data['teacher'])
            print(obj)
            obj.save()
            instances.append(obj)
        serializer = postTimeTableSerializer(instances, many=True)
        return Response(serializer.data)
