from rest_framework import serializers
from . import models
from drf_writable_nested.serializers import WritableNestedModelSerializer
class AllocationItemSerializer(WritableNestedModelSerializer):
    class Meta:
        model=models.AllocationItem
        fields=['id','weight','ISINcode']

    def create(self, validated_data):
        return super().create(validated_data | self.context)
class VersionsSerializer(WritableNestedModelSerializer):

    allocation_item=AllocationItemSerializer(many=True,required=False)

    __isValidSum:bool=lambda _,data:sum(i['weight'] for i in data['allocation_item'])==100

    def create(self, validated_data):
        if (not self.__isValidSum(validated_data)):
            raise Exception('Weights Sum must be equal to 100!')
        return super().create(validated_data)
    class Meta:
        model=models.Versions
        fields=['id','name','created_on','allocation_item','model']


class ModelSerializer(serializers.ModelSerializer):
    version=VersionsSerializer(many=True,required=False)


    class Meta:
        model=models.Model
        fields=['id','model_name','followers','version']

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Portfolio
        fields=['id','name','value','modelFollowed']

class PortfolioAllocations(serializers.ModelSerializer):
    class Meta:
        model=models.Portfolio
        fields=['id','name','value','portfolio']