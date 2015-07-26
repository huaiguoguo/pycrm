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
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = patterns(
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('app.crm.urls', namespace='crm', app_name='crm')),
    url(r'^crm/', include('app.crm.urls', namespace='crm', app_name='crm')),
    url(r'^cheku/', include('app.cheku.urls', namespace='cheku', app_name='cheku')),
    url(r'^user/', include('app.user.urls', namespace='user', app_name='user')),
    url(r'^customer/', include('app.customer.urls', namespace='customer', app_name='customer')),
    url(r'^order/', include('app.order.urls', namespace='order', app_name='order')),
    url(r'^product/', include('app.product.urls', namespace='product', app_name='product')),
    url(r'^work/', include('app.work.urls', namespace='work', app_name='work')),
    url(r'^market/', include('app.market.urls', namespace='market', app_name='market')),
    url(r'^service/', include('app.service.urls', namespace='service', app_name='service')),
    url(r'^wechat/', include('app.wechat.urls', namespace='wechat', app_name='wechat')),
    url(r'^setting/', include('app.setting.urls', namespace='setting', app_name='setting')),

    # 下面是左侧菜单
    url(r'^menu/', include('app.menu.urls', namespace='menu', app_name='menu')),
)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


