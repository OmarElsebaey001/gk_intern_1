from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from . import serializers
from rest_framework import status
from rest_framework.viewsets import ModelViewSet



class ModelsViewSet(ModelViewSet):
    serializer_class=serializers.ModelSerializer
    queryset=models.Model.objects.all()
    lookup_field='id'


class VersionsViewSet(ModelViewSet):
    serializer_class=serializers.VersionsSerializer
    queryset=models.Versions.objects.prefetch_related('allocation_item').all()
    lookup_field='id'


class AllocationItemViewSet(ModelViewSet):
    serializer_class=serializers.AllocationItemSerializer
    lookup_field='id'
    def get_queryset(self):
        return models.AllocationItem.objects.filter(version=self.kwargs['version_id']).all()

    def get_serializer_context(self):
        return {'version_id':self.kwargs['version_id']}