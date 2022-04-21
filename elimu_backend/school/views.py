from rest_framework.response import Response
from rest_framework.views import APIView
from school.models import school, principal, activation_code_generator
from school.serializers import school_serializer, school_put_serializer, principal_serializer


class schoolActivationKey(APIView):
    permission_classes = ()

    def get(self, request, activation_code):
        try:
            school_info = school.objects.get(activation_code=activation_code)
            data = school_serializer(school_info).data
        except:
            return ValueError
        else:
            school_info.activation_code = activation_code_generator()
            school_info.save()
            return Response(data.get('id'))


class get_school_id_and_principal_id(APIView):
    permission_classes = ()

    def get(self, request, id):
        principal_school = principal.objects.get(id=id)
        data = principal_serializer(principal_school).data
        return Response(data)


class get_school_details(APIView):  # getting school information
    permission_classes = ()

    def get(self, request, id):
        school_detail = school.objects.get(id=id)
        data = school_serializer(school_detail).data
        return Response(data)

    def put(self, request, id, format=None):
        school_data = school.objects.get(id=id)
        serializer = school_put_serializer(school_data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
