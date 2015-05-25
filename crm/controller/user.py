#*-*coding:utf8*-*#
__author__ = 'guo'

from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,Http404
from crm.models.models import *

# 用户管理模块
def user(request):
    return render(request, 'user.html', locals())