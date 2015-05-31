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



    url(r'^', include('user.urls', namespace='user', app_name='user')),
    url(r'^index/', include('user.urls', namespace='user', app_name='user')),

    url(r'^user/', include('user.urls', namespace='user', app_name='user')),
    url(r'^customer', include('customer.urls', namespace='customer', app_name='customer')),
    url(r'^order/', include('order.urls', namespace='order', app_name='order')),
    url(r'^product/', include('product.urls', namespace='product', app_name='product')),
    url(r'^work/', include('work.urls', namespace='work', app_name='work')),
    url(r'^market/', include('market.urls', namespace='market', app_name='market')),
    url(r'^service/', include('service.urls', namespace='service', app_name='service')),
    url(r'^wechat/', include('wechat.urls', namespace='wechat', app_name='wechat')),
    url(r'^setting/', include('setting.urls', namespace='setting', app_name='setting')),

    # 下面是左侧菜单
    url(r'^menu/(?P<menuName>(\w){1,10})', 'crm.menu.index'),
)
