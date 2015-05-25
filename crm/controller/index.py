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
    return render(request, 'index/index.html', locals())
