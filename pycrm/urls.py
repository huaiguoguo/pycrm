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
from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = patterns('crm.controller',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^', 'customer.index'),
    url(r'^index/', 'customer.index'),

    url(r'^user/', 'user.index'),

    url(r'^customer/$', 'customer.customer'),
    url(r'^customer/addcustomer/$', 'customer.addcustomer'),
    url(r'^order/', 'order.index'),
    url(r'^product/', 'product.index'),
    url(r'^work/', 'work.index'),
    url(r'^market/', 'market.index'),
    url(r'^service/', 'service.index'),
    url(r'^wechat/', 'wechat.index'),
    url(r'^setting/', 'setting.index'),

    # 下面是左侧菜单
    url(r'^menu/(?P<menuName>(\w){1,10})', 'menu.index'),
)
