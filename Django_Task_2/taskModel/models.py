from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

from content.tagsChoices import TAGS_CHOICES
# Create your models here.


class Model(models.Model):
    model_name=models.CharField(max_length=255)


class Versions(models.Model):
    model=models.ForeignKey(Model,on_delete=models.CASCADE,related_name='version')
    name=models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now=True)



class AllocationItem(models.Model):
    def minVal(x:int)->int:
        if (x<=0):
            raise Exception('Allocation Weight has to be greater than 0')
        return x

    weight=models.DecimalField(max_digits=8,
        decimal_places=3,
        validators=[minVal,MaxValueValidator(100)])
    ISINcode=models.CharField(max_length=255,null=True)
    version=models.ForeignKey(Versions,on_delete=models.CASCADE,related_name='allocation_item')


class Portfolio(models.Model):
    name=models.CharField(max_length=255)
    value=models.DecimalField(max_digits=8,
        decimal_places=3,
        validators=[MinValueValidator(0)])
    modelFollowed=models.ForeignKey(Model,on_delete=models.CASCADE,related_name='followers')
class PortfolioAllocations(models.Model):
    name=models.CharField(max_length=255)
    valueShare=models.DecimalField(max_digits=8,
        decimal_places=3,
        validators=[MinValueValidator(0)])
    portfolio=models.ForeignKey(Portfolio,on_delete=models.CASCADE,related_name='portfolio_allocations')


class Tags(models.Model):
    name=models.CharField(choices=TAGS_CHOICES,max_length=255)
    model=models.ForeignKey(Model,on_delete=models.CASCADE,related_name='tags')