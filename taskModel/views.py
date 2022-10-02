from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from . import serializers
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


# @api_view()
# def getModels(request):
#     allmodels=models.Model.objects.all()
#     serialized=serializers.ModelSerializer(allmodels,many=True)
#     return Response(serialized.data,status=status.HTTP_200_OK)



# @api_view()
# def getVersions(request):
#     allVersions=models.Versions.objects.all()
#     serialized=serializers.VersionsSerializer(allVersions,many=True)
#     return Response(serialized.data,status=status.HTTP_200_OK)


class ModelsViewSet(ModelViewSet):
    serializer_class=serializers.ModelSerializer
    queryset=models.Model.objects.all()

class VersionsViewSet(ModelViewSet):
    serializer_class=serializers.VersionsSerializer
    queryset=models.Versions.objects.all()
