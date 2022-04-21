from rest_framework.views import APIView
from rest_framework.response import Response
from suggestions.models import Suggestions
from suggestions.serializers import postSerializer, getSerializer


class postAPI(APIView):
    permission_classes = ()
    serializer_class = postSerializer

    def post(self, request):
        serializer = postSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class getAPI(APIView):
    permission_classes = ()

    def get(self, request, school):
        sugs = Suggestions.objects.filter(school=school).order_by('-id')
        serializer = getSerializer(sugs, many=True)
        return Response(serializer.data)
