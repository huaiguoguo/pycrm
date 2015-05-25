"""pycrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from crm.controller import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^', 'crm.controller.customer.index'),
    url(r'^index/', 'crm.controller.customer.index'),

    url(r'^user/', 'crm.controller.user.index'),

    url(r'^customer/', 'crm.controller.customer.customer'),
    url(r'^addcustomer/', 'crm.controller.customer.addcustomer'),

    url(r'^order/', 'crm.controller.order.index'),
    url(r'^product/', 'crm.controller.product.index'),
    url(r'^work/', 'crm.controller.work.index'),
    url(r'^market/', 'crm.controller.market.index'),
    url(r'^service/', 'crm.controller.service.index'),
    url(r'^wechat/', 'crm.controller.wechat.index'),
    url(r'^setting/', 'crm.controller.setting.index'),
    url(r'^menu/(?P<menuName>(\w){1,10})', 'crm.controller.menu.index'),
]
