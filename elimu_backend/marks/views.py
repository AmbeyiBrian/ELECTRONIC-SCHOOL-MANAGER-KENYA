from rest_framework.views import APIView
from rest_framework.response import Response
from marks.serializers import marksSerializer
from marks.models import Marks


class PostAPI(APIView):
    permission_classes = ()
    serializer_class = marksSerializer

    def post(self, request):
        serializer = marksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        elif (serializer.errors['non_field_errors']):
            return ValueError('The fields school, student, term, mid_end must make a unique set.')
        return Response(serializer.errors)


class PutAPI(APIView):
    permission_classes = ()
    serializer_class = marksSerializer

    def get(self, request, school, year, term, mid_end, student):
        mark = Marks.objects.get(school=school, year=year, term=term, mid_end=mid_end, student=student)
        serializer = marksSerializer(mark)
        return Response(serializer.data)

    def put(self, request, school, year, term, mid_end, student, format=None):
        mark = Marks.objects.get(school=school, year=year, term=term, mid_end=mid_end, student=student)
        serializer = marksSerializer(mark, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class GetAPI(APIView):
    permission_classes = ()
    serializer_class = marksSerializer

    def get(self, request, school):
        mark = Marks.objects.filter(school=school)
        serializer = marksSerializer(mark, many=True)
        return Response(serializer.data)
