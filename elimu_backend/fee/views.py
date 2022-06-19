from rest_framework.response import Response
from rest_framework.views import APIView
from fee.models import FeeStructure, FeeStatement
from fee.serializers import GetFeeStructureSerializer, PostFeeStructureSerializer, GetFeeStatementSerializer, \
    PostFeeStatementSerializer


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
#
#
# from django.http import HttpResponse
# import requests
# from requests.auth import HTTPBasicAuth
# import json
# from .mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
#
#
# def getAccessToken(request):
#     consumer_key = 'cHnkwYIgBbrxlgBoneczmIJFXVm0oHky'
#     consumer_secret = '2nHEyWSD4VjpNh2g'
#     api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
#     r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
#     mpesa_access_token = json.loads(r.text)
#     validated_mpesa_access_token = mpesa_access_token['access_token']
#     return HttpResponse(validated_mpesa_access_token)
#
#
# def lipa_na_mpesa_online(request):
#     access_token = MpesaAccessToken.validated_mpesa_access_token
#     api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#     headers = {"Authorization": "Bearer %s" % access_token}
#     try:
#         request = {
#             "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
#             "Password": LipanaMpesaPpassword.decode_password,
#             "Timestamp": LipanaMpesaPpassword.lipa_time,
#             "TransactionType": "CustomerPayBillOnline",
#             "Amount": 1,
#             "PartyA": 254797259698,  # replace with your phone number to get stk push
#             "PartyB": LipanaMpesaPpassword.Business_short_code,
#             "PhoneNumber": 254797259698,  # replace with your phone number to get stk push
#             "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
#             "AccountReference": "Henry",
#             "TransactionDesc": "Testing stk push"
#         }
#         response = requests.post(api_url, json=request, headers=headers)
#     except:
#         return HttpResponse('Failed')
#     else:
#         return HttpResponse(response)
