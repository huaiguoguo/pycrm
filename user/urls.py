__author__ = 'guo'

from django.conf.urls import include, url, patterns


urlpatterns = patterns('user.views',
    url(r'^user/', 'index'),
    # 下面是左侧菜单
    url(r'^menu/(?P<menuName>(\w){1,10})', 'index'),
)