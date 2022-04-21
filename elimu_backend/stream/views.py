from rest_framework.response import Response
from rest_framework.views import APIView
from stream.serializers import getStreamSerializer, postStreamSerializer
from stream.models import streams


class streamAPI(APIView):
    permission_classes = ()
    serializer_class = getStreamSerializer

    def post(self, request):
        serializer = postStreamSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, school):
        school_streams = streams.objects.filter(school=school).order_by('form')
        serializer = getStreamSerializer(school_streams, many=True)
        return Response(serializer.data)


class streamPutAPI(APIView):
    permission_classes = ()
    serializer_class = postStreamSerializer

    def get(self, request, streamID):
        school_streams = streams.objects.get(id=streamID)
        serializer = getStreamSerializer(school_streams)
        return Response(serializer.data)

    def put(self, request, streamID, format=None):
        stream = streams.objects.get(id=streamID)
        serializer = postStreamSerializer(stream, data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        print(serializer.errors)
        return Response(serializer.errors)
