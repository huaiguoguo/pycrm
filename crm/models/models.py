from MySQLdb import *
from django.db import models
# from django_mongoengine import Document

# Create your models here.

class Department(models.Model):
    departmentname = models.CharField(max_length=20)

class Saler(models.Model):
    salername = models.CharField(max_length=20)
    mobile = models.IntegerField()
    qq = models.IntegerField()
    department = models.ForeignKey(Department, related_name='departmentforeign')
    islead = models.IntegerField()

class Industry(models.Model):
    industryname = models.CharField(max_length=20)
    createdate = models.DateTimeField()

class Level(models.Model):
    levelname = models.CharField(max_length=20)

class Customer(models.Model):
    saler = models.ForeignKey(Saler, related_name='salerforeign')
    industry = models.ForeignKey(Industry, related_name='industryforeign')
    level = models.ForeignKey(Level, related_name='levelforeign', default=True)
    customername = models.CharField(max_length=20, unique=True)
    company = models.CharField(max_length=40)
    mobile = models.IntegerField()
    qq = models.IntegerField()
    wangwang = models.CharField(max_length=10)
    gender = models.IntegerField()
    createdate = models.DateTimeField()


