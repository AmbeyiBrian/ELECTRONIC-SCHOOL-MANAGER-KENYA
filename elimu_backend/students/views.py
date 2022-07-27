from rest_framework.response import Response
from rest_framework.views import APIView
from students.serializers import postStudentSerializer, getStudentSerializer
from students.models import students

from fee.models import FeeStructure, FeeStatement
from terms.models import Terms


class studentsAPI(APIView):
    permission_classes = ()
    serializer_class = postStudentSerializer

    def post(self, request):
        serializer = postStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            new_student = students.objects.get(school=request.data['school'], admission_number=request.data['admission_number'])
            current_term=Terms.objects.filter(school=request.data['school']).order_by('id')
            current_term=current_term[0].term_name

            fee_total = 0
            for i in FeeStructure.objects.filter(form=new_student.stream.form, school=request.data['school'], term=current_term):
                fee_total += i.amount

            FeeStatement.objects.create(student=new_student, ref_code='INITIAL', description='Initial term fee', amount=0, balance=fee_total).save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, school):
        list_students = students.objects.filter(school=school).order_by('admission_number')
        serializer = getStudentSerializer(list_students, many=True)
        return Response(serializer.data)


class studentSearchAPI(APIView):
    permission_classes = ()

    def get(self, request, searchText):
        list_students = students.objects.filter(last_name__icontains=searchText)
        serializer = getStudentSerializer(list_students, many=True)
        return Response(serializer.data)


class getStudent(APIView):
    permission_classes = ()

    def get(self, request, studentID):
        student = students.objects.filter(id=studentID)
        serializer = getStudentSerializer(student, many=True)
        return Response(serializer.data)

    def put(self, request, studentID, format=None):
        student = students.objects.get(id=studentID)
        serializer = postStudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
