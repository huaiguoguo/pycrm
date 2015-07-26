#*-*coding:utf8*-*#
__author__ = 'guo'

from django.shortcuts import render

# Create your views here.


# 左侧菜单
def index(request, menuName):
    name = menuName
    return render(request, 'layout/menu.html', locals())