from MySQLdb import *
from django.db import models
# from django_mongoengine import Document

# Create your models here.





class Department(models.Model):
    departmentname = models.CharField(max_length=20, default=NULL)

class Saler(models.Model):
    salername = models.CharField(max_length=20, default=NULL)
    mobile = models.IntegerField(default=NULL)
    qq = models.IntegerField(default=NULL)
    department = models.ForeignKey(Department)
    islead = models.IntegerField(default=NULL)

class Customer(models.Model):
    username = models.CharField(max_length=20)
    company = models.CharField(max_length=40)
    mobile = models.IntegerField(default=NULL)
    qq = models.IntegerField(default=NULL)
    wangwang = models.CharField(max_length=10)
    saler = models.ForeignKey(Saler)
    gender = models.IntegerField(default=NULL)
    createdate = models.DateTimeField()

