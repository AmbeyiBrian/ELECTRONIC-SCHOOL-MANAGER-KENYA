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
            print(serializer.errors)
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
