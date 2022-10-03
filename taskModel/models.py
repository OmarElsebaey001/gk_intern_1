from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class Model(models.Model):
    model_name=models.CharField(max_length=255)


class Versions(models.Model):
    model=models.ForeignKey(Model,on_delete=models.CASCADE,related_name='version')
    name=models.CharField(max_length=255)
    ISINcode=models.CharField(max_length=255)
    allocation=models.DecimalField(
        max_digits=8,
        decimal_places=3,
        validators=[MinValueValidator(1)]
        )
    portfolioVersion=models.IntegerField()



class AllocationItem(models.Model):
    def minVal(x:int)->int:
        if (x<=0):
            raise Exception('Allocation Weight has to be greater than 0')
        return x

    weight=models.DecimalField(max_digits=8,
        decimal_places=3,
        validators=[minVal,MaxValueValidator(100)])
    version=models.ForeignKey(Versions,on_delete=models.CASCADE,related_name='allocation_item')
