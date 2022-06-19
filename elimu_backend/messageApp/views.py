from rest_framework.views import APIView
from rest_framework.response import Response
from twilio.rest import Client
from user_accounts.models import Users
from students.models import students
from messageApp.models import Message
from messageApp.serializers import GetMessageSerializer, PostMessageSerializer


class PostMessageAPI(APIView):
    permission_classes = ()
    serializer_class = PostMessageSerializer

    def get(self, request, school_id):
        messages = Message.objects.filter(school=school_id).order_by('-id')
        serializer = GetMessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        account_sid = 'AC3bf6f879b30543e0320db47cc3893708'
        auth_token = '3a4943dfad224437e65e80f9e2f6d4b4'
        client = Client(account_sid, auth_token)

        serializer = PostMessageSerializer(data=request.data)

        if serializer.is_valid():
            if request.data['sms']:
                if request.data['target_audience'] == 'Teachers':
                    a = Users.objects.filter(teacher__school=request.data['school'])
                    for i in a:
                        message = client.messages.create(
                            body=request.data['message'],
                            from_='+13156602983',
                            to=i.phone_number)
                elif request.data['target_audience'] == 'Sub staff':
                    a = Users.objects.filter(sub_staff__school=request.data['school'])
                    for i in a:
                        message = client.messages.create(
                            body=request.data['message'],
                            from_='+13156602983',
                            to=i.phone_number)
                elif request.data['target_audience'] == 'Parents':
                    a = students.objects.filter(school=request.data['school'])
                    x = []
                    for i in a: x.append(i.parent)
                    x = set(x)
                    x.remove(None)
                    a = Users.objects.filter(email_address__in=x)
                    for i in a:
                        message = client.messages.create(
                            body=request.data['message'],
                            from_='+13156602983',
                            to=i.phone_number)
                elif request.data['target_audience'] == 'All':
                    a = Users.objects.filter(teacher__school=request.data['school'])
                    for i in a:
                        message = client.messages.create(
                            body=request.data['message'],
                            from_='+13156602983',
                            to=i.phone_number)

                    a = Users.objects.filter(sub_staff__school=request.data['school'])
                    for i in a:
                        message = client.messages.create(
                            body=request.data['message'],
                            from_='+13156602983',
                            to=i.phone_number)

                    a = students.objects.filter(school=request.data['school'])
                    x = []
                    for i in a: x.append(i.parent)
                    x = set(x)
                    x.remove(None)
                    a = Users.objects.filter(email_address__in=x)
                    for i in a:
                        message = client.messages.create(
                            body=request.data['message'],
                            from_='+13156602983',
                            to=i.phone_number)

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
