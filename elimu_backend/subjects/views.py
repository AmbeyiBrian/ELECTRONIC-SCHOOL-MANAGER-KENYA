from rest_framework.response import Response
from rest_framework.views import APIView
from subjects.serializers import getSubjectsSerializer, postSubjectsSerializer, getElectiveSerializer, \
    postElectiveSerializer
from subjects.models import optional_subjects, electives


class subjectsAPI(APIView):
    permission_classes = ()
    serializer_class = getSubjectsSerializer

    def post(self, request):
        serializer = postSubjectsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, school):
        school_subjects = optional_subjects.objects.filter(school=school)
        serializer = getSubjectsSerializer(school_subjects, many=True)
        return Response(serializer.data)


class DeleteAPI(APIView):
    permission_classes = ()
    serializer_class = getSubjectsSerializer

    def delete(self, request, id, format=None):
        subject = optional_subjects.objects.get(id=id)
        subject.delete()
        serializer = getSubjectsSerializer(subject)
        return Response(serializer.data)


class electivesAPI(APIView):
    permission_classes = ()
    serializer_class = getElectiveSerializer

    def get(self, request, school):
        school_electives = electives.objects.filter(school=school)
        serializer = getElectiveSerializer(school_electives, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = postElectiveSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DeleteElectiveAPI(APIView):
    permission_classes = ()
    serializer_class = getElectiveSerializer

    def delete(self, request, id, format=None):
        elective = electives.objects.get(id=id)
        elective.delete()
        serializer = getElectiveSerializer(elective)
        return Response(serializer.data)


# class SubjectStudentAPI(APIView):
#     permission_classes = ()
#     serializer_class = PostSubjectStudentSerializer
#
#     def post(self, request):
#         serializer = PostSubjectStudentSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         return Response(serializer.errors)
