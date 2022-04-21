from rest_framework import serializers
from school.models import school, principal


class school_serializer(serializers.ModelSerializer):
    class Meta:
        model = school
        fields = (
            "__all__"
        )

class school_put_serializer(serializers.ModelSerializer):
    class Meta:
        model=school
        fields=(
                ['school_name', 'school_code', 'school_telephone', 'school_email', 'postal_address', 'postal_code', 'vision', 'mission',
                 'motto', 'county', 'sub_county', 'mpesa_business_number', 'mpesa_account_number', 'bank_name', 'bank_account_number']
            )


class principal_serializer(serializers.ModelSerializer):
    class Meta:
        model = principal
        fields = (
            ['principal', 'school']
        )
