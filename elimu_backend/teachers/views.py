from rest_framework.response import Response
from rest_framework.views import APIView
from teachers.serializers import teachersSerializer, listTeacherSerializer, teachersSerializer2
from teachers.models import teachers


class teacherAPI(APIView):
    permission_classes = ()
    serializer_class = teachersSerializer

    def post(self, request):
        serializer = teachersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, school):
        list_teachers = teachers.objects.filter(school=school)
        serializer = listTeacherSerializer(list_teachers, many=True)
        return Response(serializer.data)


class teacher_activation_code_validation(APIView):
    permission_classes = ()

    def get(self, request, activation_code):
        try:
            teacher_account = teachers.objects.get(activation_code=activation_code)
            data=teachersSerializer2(teacher_account).data
        except:
            return ValueError
        else:
            return Response(data)

    def put(self, request, activation_code, format=None):
        teacher_account = teachers.objects.get(activation_code=activation_code)
        serializer = teachersSerializer(teacher_account, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

