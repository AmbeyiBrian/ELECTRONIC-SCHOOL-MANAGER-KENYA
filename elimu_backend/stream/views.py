from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from stream.serializers import getStreamSerializer, postStreamSerializer, getStreamSUbjectTeacherSerializer, postStreamSUbjectTeacherSerializer
from stream.models import streams, stream_subject_teacher


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


class streamSubjectTeacherAPI(APIView):
    permission_classes = ()
    serializer_class = getStreamSUbjectTeacherSerializer

    def post(self, request):
        serializer = postStreamSUbjectTeacherSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            raise status.HTTP_400_BAD_REQUEST

    def get(self, request, streamID):
        school_streams = stream_subject_teacher.objects.filter(stream=streamID)
        serializer = getStreamSUbjectTeacherSerializer(school_streams, many=True)
        return Response(serializer.data)

    def put(self, request, selected_stream_teacher_subject_id, format=None):
        stream_subject = stream_subject_teacher.objects.get(id=selected_stream_teacher_subject_id)
        serializer = postStreamSUbjectTeacherSerializer(stream_subject, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors)


class streamSubjectTeacherGetAPI(APIView):
    permission_classes = ()
    serializer_class = getStreamSUbjectTeacherSerializer

    def get(self, request, school):
        streams_teachers = stream_subject_teacher.objects.filter(school=school)
        serializer = getStreamSUbjectTeacherSerializer(streams_teachers, many=True)
        return Response(serializer.data)
