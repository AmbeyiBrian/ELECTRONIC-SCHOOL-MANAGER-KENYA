from rest_framework.response import Response
from rest_framework.views import APIView
from subStaff.serializers import SubStaff
from subStaff.serializers import SubStaffSerializer, SubStaffSerializer2


class SubStaffAPI(APIView):
    permission_classes = ()
    serializer_class = SubStaffSerializer

    def post(self, request):
        serializer = SubStaffSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request, school):
        subStaff = SubStaff.objects.filter(school=school)
        serializer = SubStaffSerializer2(subStaff, many=True)
        return Response(serializer.data)


class ActivationKeyValidation(APIView):
    permission_classes = ()
    serializer_class = SubStaffSerializer

    def get(self, request, activation_code):
        try:
            subStaff = SubStaff.objects.get(activation_code=activation_code)
            serializer = SubStaffSerializer(subStaff)
        except:
            return ValueError
        else:
            return Response(serializer.data)

    def put(self, request, activation_code, format=None):
        sub_staff_account = SubStaff.objects.get(activation_code=activation_code)
        serializer = SubStaffSerializer(sub_staff_account, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

