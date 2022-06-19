from rest_framework import serializers
from fee.models import FeeStructure, FeeStatement


class PostFeeStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeStructure
        fields = (
            ['school', 'form', 'term', 'attribute', 'amount']
        )


class GetFeeStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeStructure
        fields = ('__all__')


class PostFeeStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeStatement
        fields = (
            ['student', 'ref_code', 'description', 'amount', 'balance']
        )


class GetFeeStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeStatement
        fields = ('__all__')
        depth = 1
