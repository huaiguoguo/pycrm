#*-*coding:utf8*-*#
__author__ = 'guo'

from django.shortcuts import render

# Create your views here.

# 主页
def index(request):
    return render(request, 'user/user.html', locals())

# 左侧菜单
def menu(request, menuName):
    name = menuName
    return render(request, 'menu.html', locals())