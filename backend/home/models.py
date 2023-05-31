from django.conf import settings
from django.db import models
class Animal(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,null=True,blank=True,)
    age = models.IntegerField(null=True,blank=True,)
class Acma(models.Model):
    'Generated Model'
    asd = models.BigIntegerField()
