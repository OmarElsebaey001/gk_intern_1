from django.db import models
from django.core.validators import MinValueValidator
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

