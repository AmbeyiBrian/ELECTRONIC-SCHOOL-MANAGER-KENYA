from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from user_accounts.serializers import user_serializer, principal_serializer2, update_user_info_serializer
from user_accounts.models import Users
from rest_framework.authtoken.models import Token


class create_user(generics.CreateAPIView):
    permission_classes = ()
    serializer_class = user_serializer


class login_user(APIView):  # login function. Uses the email address and password to authenticate
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        email_address = request.data.get('email_address')
        password = request.data.get('password')
        user = authenticate(email_address=email_address, password=password)
        serializer = principal_serializer2(user)

        if user:
            try:
                user.auth_token.delete()
            except:
                Token.objects.create(user=user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)


class logout_user(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, email_address):
        user = Users.objects.get(email_address=email_address)
        try:
            user.auth_token.delete()
            return Response("Token deleted successfully")
        except:
            return Response("Token deleted successfully")


class GetUserInfoAPI(APIView):
    permission_classes = ()

    def get(self, request, email_address):
        user = Users.objects.get(email_address=email_address)
        serializer = principal_serializer2(user)
        return Response(serializer.data)

    def put(self, request, email_address, format=None):
        user = Users.objects.get(email_address=email_address)
        serializer = update_user_info_serializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
