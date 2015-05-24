from django.db import models
# Create your models here.

class Department(models.Model):
    id = models.IntegerField(max_length=2)
    departmentname = models.CharField()

class Saler(models.Model):
    id = models.IntegerField(max_length=11)
    salername = models.CharField()
    mobile = models.IntegerField()
    qq = models.IntegerField(max_length=12)
    department = models.ForeignKey(Department)
    islead = models.IntegerField()

class Customer(models.Model):
    id = models.IntegerField(max_length=11)
    username = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    mobile = models.IntegerField(max_length=255)
    qq = models.IntegerField(max_length=12)
    wangwang = models.CharField()
    saler = models.ForeignKey(Saler)
    gender = models.IntegerField(max_length=1)
    createdate = models.TimeField()

