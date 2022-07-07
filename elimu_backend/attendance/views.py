from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from attendance.serializers import getSerializer, postSerializer, getSerializer2
from attendance.models import attendanceSheet


class attendanceAPI(APIView):
    permission_classes = ()
    serializer_class = postSerializer

    def get(self, request, school, year, term):
        attendance = attendanceSheet.objects.filter(student__school=school, year=year, term=term)
        data = getSerializer(attendance, many=True).data
        return Response(data)

    def post(self, request):
        serializer = postSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            raise status.HTTP_400_BAD_REQUEST

    def delete(self, request, student, date):
        attendance = attendanceSheet.objects.get(student=student, date=date)
        data = getSerializer(attendance)
        attendance.delete()
        return Response(data.data)

class attendanceAPI2(APIView):
    permission_classes = ()
    serializer_class = postSerializer

    def get(self, request, school):
        attendance = attendanceSheet.objects.filter(student__school=school)
        data = getSerializer2(attendance, many=True).data
        return Response(data)
