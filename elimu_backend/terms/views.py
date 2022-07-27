from rest_framework.response import Response
from rest_framework.views import APIView
from terms.serializers import postSerializer
from terms.models import Terms

from fee.models import FeeStructure, FeeStatement
from students.models import students
from django.db.models import Sum


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

            current_term = Terms.objects.filter(school=request.data['school']).order_by('id')
            current_term = current_term[0].term_name

            studs = students.objects.filter(school=request.data['school'])

            for i in studs:
                FeeStatement.objects.create(student=students.objects.get(id=i.id), ref_code='INITIAL',
                                            description='Initial term fee',
                                            amount=0, balance=FeeStructure.objects.filter(school=request.data['school'],
                                                                                          term=current_term,
                                                                                          form=i.stream.form).aggregate(
                        sum=Sum('amount'))['sum'] + (FeeStatement.objects.filter(student__id=i.id).order_by('-id')[
                                                                  0].balance if len(
                        FeeStatement.objects.filter(student__id=i.id).order_by('-id')) > 0 else 0)).save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors)


class termPutAPI(APIView):
    permission_classes = ()
    serializer = postSerializer

    def get(self, request, id):
        lessons = Terms.objects.get(id=id)
        serializer = postSerializer(lessons)
        return Response(serializer.data)

    def put(self, request, id):
        term = Terms.objects.get(id=id)
        serializer = postSerializer(term, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
