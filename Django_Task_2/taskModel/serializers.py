from typing import OrderedDict
from rest_framework import serializers
from . import models


class AllocationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AllocationItem
        fields=['id','weight']

    def create(self, validated_data):
        return super().create(validated_data | self.context)
class VersionsSerializer(serializers.ModelSerializer):

    def checkWeightsSum(weightsDict:OrderedDict)->None:
        if sum(weightsDict.values())!=100:
            raise Exception('Sum of Weights must be Equal to 100 exactly.')

    allocation_item=AllocationItemSerializer(many=True,required=False,validators=[checkWeightsSum])
    class Meta:
        model=models.Versions
        fields=['id','name','ISINcode','portfolioVersion','allocation_item']


class ModelSerializer(serializers.ModelSerializer):
    version=VersionsSerializer(many=True,required=False)
    class Meta:
        model=models.Model
        fields=['id','model_name','version']
