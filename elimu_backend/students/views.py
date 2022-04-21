from rest_framework.response import Response
from rest_framework.views import APIView
from students.serializers import postStudentSerializer, getStudentSerializer
from students.models import students


class studentsAPI(APIView):
    permission_classes = ()
    serializer_class = postStudentSerializer

    def post(self, request):
        serializer = postStudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, school):
        list_students = students.objects.filter(school=school).order_by('admission_number')
        serializer = getStudentSerializer(list_students, many=True)
        return Response(serializer.data)


class studentSearchAPI(APIView):
    permission_classes = ()

    def get(self, request, searchText):
        list_students = students.objects.filter(last_name__icontains=searchText)
        serializer = getStudentSerializer(list_students, many=True)
        return Response(serializer.data)


class getStudent(APIView):
    permission_classes = ()

    def get(self, request, studentID):
        student = students.objects.filter(id=studentID)
        serializer = getStudentSerializer(student, many=True)
        return Response(serializer.data)

    def put(self, request, studentID, format=None):
        student = students.objects.get(id=studentID)
        serializer = postStudentSerializer(student, data=request.data)

        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
