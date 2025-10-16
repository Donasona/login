from django.db import models

# Create your models here.
class Loginmodel(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password =models.IntegerField(null=False)