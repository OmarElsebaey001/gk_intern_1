from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from . import models
from . import serializers
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count,Sum


class ModelsViewSet(ModelViewSet):
    serializer_class=serializers.ModelSerializer
    queryset=models.Model.objects.all()
    lookup_field='id'

    @action(detail=True)
    def summary(self,_,id):
        target=models.Model.objects.prefetch_related('followers').filter(pk=id)
        followersData=target.aggregate(numberOfFollowers=Count('followers'),valueOfFollowers=Sum('followers__value'))
        return Response(followersData,status=status.HTTP_200_OK)


class VersionsViewSet(ModelViewSet):
    serializer_class=serializers.VersionsSerializer
    queryset=models.Versions.objects.prefetch_related('allocation_item').all()
    lookup_field='id'



class PortfolioViewSet(ModelViewSet):
    serializer_class=serializers.PortfolioSerializer
    queryset=models.Portfolio.objects.all()
    lookup_field='id'

class AllocationItemViewSet(ModelViewSet):
    serializer_class=serializers.AllocationItemSerializer
    lookup_field='id'

    def get_queryset(self):
        return models.AllocationItem.objects.filter(version=self.kwargs['version_id']).all()

    def get_serializer_context(self):
        return {'version_id':self.kwargs['version_id']}
