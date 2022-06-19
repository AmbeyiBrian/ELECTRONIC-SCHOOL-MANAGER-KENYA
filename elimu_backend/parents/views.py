from rest_framework.response import Response
from rest_framework.views import APIView
from students.serializers import postStudentSerializer, getStudentSerializer
from students.models import students


class ParentAPI(APIView):
    permission_classes = ()
    serializer_class = postStudentSerializer

    def get(self, request, activation_code):
        student = students.objects.get(activation_code=activation_code)
        serializer = getStudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, activation_code, format=None):
        student = students.objects.get(activation_code=activation_code)
        serializer = postStudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors)


class ParentStudentValidationAPI(APIView):
    permission_classes = ()
    serializer_class = postStudentSerializer

    def get(self, request, parent):
        my_students = students.objects.filter(parent=parent)
        serializer = getStudentSerializer(my_students, many=True)
        return Response(serializer.data)
