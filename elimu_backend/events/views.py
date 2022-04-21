from rest_framework.response import Response
from rest_framework.views import APIView
from events.serializers import getSerializer, postSerializer
from events.models import events


class school_events(APIView):  # getting school list of events
    permission_classes = ()
    serializer_class = postSerializer

    def get(self, request, school):
        school_detail = events.objects.filter(school=school).order_by('date_of_event')
        data = getSerializer(school_detail, many=True).data
        return Response(data)

    def post(self, request):
        serializer = postSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
