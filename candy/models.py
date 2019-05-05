from django.db import models
from manufacturer.models import Manufacturer
# Create your models here.


class CandyCategory(models.Model):
    name = models.CharField(max_length=255)


class Candy(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True) #blank means that it isnt required.
    category = models.ForeignKey(CandyCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


class CandyImage(models.Model):
    image = models.CharField(max_length=999)
    candy = models.ForeignKey(Candy, on_delete=models.CASCADE)