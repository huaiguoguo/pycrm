#*-*coding:utf8*-*#
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,Http404
from crm.models import *

# Create your views here.


# 主页
def index(request):
    age = 12
    name = 'liming'
    return render(request, 'index.html', locals())

# 用户管理
def user(request):
    return render(request, 'user.html', locals())

# 客户管理
def customer(request):
    return render(request, 'customer.html', locals())

# 订单管理
def order(request):
    return render(request, 'order.html', locals())

# 产品管理
def product(request):
    return render(request, 'product.html', locals())

# 工作管理
def work(request):
    return render(request, 'work.html', locals())

# 营销管理
def market(request):
    return render(request, 'market.html', locals())

# 服务管理
def service(request):
    return render(request, 'service.html', locals())

# 微信管理
def wechat(request):
    return render(request, 'wechat.html', locals())

# 系统设置
def setting(request):
    return render(request, 'setting.html', locals())



# 左侧菜单
def menu(request, menuName):
    name = menuName
    return render(request, 'menu.html', locals())