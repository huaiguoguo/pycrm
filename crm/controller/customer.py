#*-*coding:utf8*-*#
__author__ = 'guo'

from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,Http404
from crm.models.models import *

# Create your views here.


# 主页
def index(request):
    age = 12
    name = 'liming'
    return render(request, 'custormer/index.html', locals())

# 客户管理
def customer(request):
    customerList = Customer.objects.all()
    return render(request, 'custormer/customer.html', locals())

# 添加客户
def addcustomer(request):
    return render(request, 'custormer/add.html', locals())