from rest_framework.response import Response
from rest_framework.views import APIView
from fee.models import FeeStructure, FeeStatement
from fee.serializers import GetFeeStructureSerializer, PostFeeStructureSerializer, GetFeeStatementSerializer, \
    PostFeeStatementSerializer
from students.models import students
import json


class FeeAPI(APIView):
    permission_classes = ()
    serializer_class = PostFeeStructureSerializer

    def post(self, request, *args, **kwargs):
        serializer = PostFeeStructureSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, school):
        fee_attributes = FeeStructure.objects.filter(school=school)
        serializer = GetFeeStructureSerializer(fee_attributes, many=True)
        return Response(serializer.data)


class PutAPI(APIView):
    permission_classes = ()
    serializer_class = PostFeeStructureSerializer

    def put(self, request, id):
        fee_item = FeeStructure.objects.get(id=id)
        serializer = PostFeeStructureSerializer(fee_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def get(self, request, id):
        fee_attribute = FeeStructure.objects.get(id=id)
        serializer = GetFeeStructureSerializer(fee_attribute)
        return Response(serializer.data)


class DeleteAPI(APIView):
    permission_classes = ()
    serializer_class = GetFeeStructureSerializer

    def delete(self, request, id, format=None):
        fee_item = FeeStructure.objects.get(id=id)
        fee_item.delete()
        serializer = GetFeeStructureSerializer(fee_item)
        return Response(serializer.data)


class FeeStatementAPI(APIView):
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = PostFeeStatementSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, school):
        fee_statements = FeeStatement.objects.filter(student__school=school).order_by('-id')
        serializer = GetFeeStatementSerializer(fee_statements, many=True)
        return Response(serializer.data)


from django_daraja.mpesa.core import MpesaClient
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from fee.models import MpesaCalls, MpesaPayment


class MpesaAPI(APIView):
    permission_classes = ()

    def post(self, request):
        global fee_data
        fee_data=request.data
        cl = MpesaClient()
        phone_number = request.data['phone_number']
        amount = int(request.data['amount'])
        account_reference = request.data['bank_account_number']
        transaction_desc = request.data['description']
        callback_url = "https://2974-41-89-104-15.eu.ngrok.io/fee/daraja/stk_push_callback"
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

        if response.status_code == 200:
            r = response.content
            t = json.loads(r)
            MpesaCalls.objects.create(CheckoutRequestID=t['CheckoutRequestID'],
                                      ResponseDescription=t['ResponseDescription']).save()
            return HttpResponse(r)
        else:
            e = response.content
            er = json.loads(e)
            err = er['errorMessage']
            print("Transaction error", err)
            return HttpResponse(err)


@csrf_exempt
def index(request):
    cl = MpesaClient()
    phone_number = '0797259698'
    amount = 1
    account_reference = 'Henry'
    transaction_desc = 'Description'
    callback_url = "https://2974-41-89-104-15.eu.ngrok.io/fee/daraja/stk_push_callback"
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

    if response.status_code == 200:
        r = response.content
        t = json.loads(r)
        MpesaCalls.objects.create(CheckoutRequestID=t['CheckoutRequestID'], ResponseDescription=t['ResponseDescription']).save()
        return HttpResponse(r)
    else:
        e = response.content
        er = json.loads(e)
        err = er['errorMessage']
        print("Transaction ERROR", err)
        return HttpResponse(err)


@csrf_exempt
def stk_push_callback(request):
    dt = json.loads(request.body)
    data = dt['Body']['stkCallback']

    if data['ResultCode']==0:
        payment = MpesaPayment.objects.create(
                                    amount=data['CallbackMetadata']['Item'][0]['Value'],
                                    description=data['ResultDesc'],
                                    reference=data['CallbackMetadata']['Item'][1]['Value'],
                                    phone_number=data['CallbackMetadata']['Item'][4]['Value'],
                                    )
        payment.save()
        FeeStatement.objects.create(
                student=students.objects.get(id=int(fee_data['student'])),
                ref_code=data['CallbackMetadata']['Item'][1]['Value'],
                description=fee_data['description'],
                amount=fee_data['amount'],
                balance=fee_data['balance']
            ).save()
    else:
        pass

    return JsonResponse(dict(data))

