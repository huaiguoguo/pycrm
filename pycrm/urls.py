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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'crm.views.index'),
    url(r'^user/', 'crm.views.user'),
    url(r'^customer', 'crm.views.customer'),
    url(r'^order/', 'crm.views.order'),
    url(r'^product/', 'crm.views.product'),
    url(r'^work/', 'crm.views.work'),
    url(r'^market/', 'crm.views.market'),
    url(r'^service/', 'crm.views.service'),
    url(r'^wechat/', 'crm.views.wechat'),
    url(r'^setting/', 'crm.views.setting'),
]
