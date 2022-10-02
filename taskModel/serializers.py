from dataclasses import field, fields
from rest_framework import serializers
from . import models




class VersionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Versions
        fields=['id','name','ISINcode','allocation','portfolioVersion']




class ModelSerializer(serializers.ModelSerializer):
    version=VersionsSerializer(many=True,required=False)
    class Meta:
        model=models.Model
        fields=['id','model_name','version']
