__author__ = 'guo'

from django.conf.urls import include, url, patterns


urlpatterns = patterns('order.views',
    url(r'^index/$', 'index'),
    # # ���������˵�
    # url(r'^menu/(?P<menuName>(\w){1,10})', 'crm.menu.index'),
)