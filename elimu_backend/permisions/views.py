from rest_framework.views import APIView
from rest_framework.response import Response
from permisions.models import Permissions
from permisions.serializers import GetPermissionSerializer, PutPermissionSerializer


class EditPermision(APIView):
    permission_classes = ()
    serializer_class=PutPermissionSerializer

    def get(self, request, id):
        permission = Permissions.objects.get(id=id)
        serializer = GetPermissionSerializer(permission)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        permission = Permissions.objects.get(id=id)
        serializer = PutPermissionSerializer(permission, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class GetPermissions(APIView):
    permission_classes = ()

    def get(self, request, school):
        permission = Permissions.objects.filter(school=school)
        serializer = GetPermissionSerializer(permission, many=True)
        return Response(serializer.data)
