__author__ = 'guo'

from django.conf.urls import include, url, patterns


urlpatterns = patterns('product.views',
    url(r'^index/$', 'index'),
    # 下面是左侧菜单
)