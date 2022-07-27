from rest_framework import serializers
from user_accounts.models import Users
from rest_framework.authtoken.models import Token


class user_serializer(serializers.ModelSerializer):  # serializer class to create a general user
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = (
            'first_name', 'last_name', 'gender', 'email_address', 'phone_number', 'user_class',
            'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Users(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class principal_serializer2(serializers.ModelSerializer):  # serializer to retrieve information about a principal
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = (
            'first_name', 'last_name', 'gender', 'email_address', 'phone_number', 'user_class',
            'password', 'auth_token', 'principal', 'teacher', 'sub_staff'
        )
        depth = 1


class teacher_serializer(serializers.ModelSerializer):  # serializer to create a user as a teacher
    class Meta:
        model = Users
        fields = (
            'first_name', 'last_name', 'gender', 'email_address', 'phone_number', 'national_id', 'user_class',
            'password', 'auth_token',
        )


class update_user_info_serializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'first_name', 'last_name', 'gender', 'email_address', 'phone_number', 'national_id', 'user_class'
        )