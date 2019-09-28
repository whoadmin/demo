from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    privilege = models.IntegerField()