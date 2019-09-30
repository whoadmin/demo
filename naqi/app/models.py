from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    create_time = models.CharField(max_length=255)
    perm_id = models.IntegerField()

class Perm(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    describe = models.CharField(max_length=255)
    code = models.IntegerField()

class Nac(models.Model):
    id = models.AutoField(primary_key=True)
    hostid = models.BigIntegerField()
    ip = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)
    dhcp_server = models.CharField(max_length=255)
    dhcp_hostname = models.CharField(max_length=255)
    nbtdomain = models.CharField(max_length=255)
    ad_displayname = models.CharField(max_length=255)
    ad_name = models.CharField(max_length=255)
    ad_mail = models.CharField(max_length=255)
    ad_title = models.CharField(max_length=255)
    ad_department = models.CharField(max_length=255)
    ad_mobile = models.CharField(max_length=255)
    href = models.CharField(max_length=255)
    etag = models.CharField(max_length=255)
    update_time = models.CharField(max_length=255)