from rest_framework.response import Response
from rest_framework.views import APIView
from terms.serializers import postSerializer
from terms.models import Terms


class termsAPI(APIView):
    permission_classes = ()
    serializer_class = postSerializer

    def get(self, request, school):
        lessons = Terms.objects.filter(school=school).order_by('-opening_date')
        serializer = postSerializer(lessons, many=True)
        return Response(serializer.data)


class termsPostAPI(APIView):

    permission_classes = ()
    serializer_class = postSerializer

    def post(self, request):
        serializer = postSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)


class termPutAPI(APIView):
    permission_classes = ()
    serializer=postSerializer

    def get(self, request, id):
        lessons = Terms.objects.get(id=id)
        serializer = postSerializer(lessons)
        return Response(serializer.data)

    def put(self, request, id):
        term=Terms.objects.get(id=id)
        serializer=postSerializer(term, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
