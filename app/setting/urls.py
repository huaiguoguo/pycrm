__author__ = 'guo'

from django.conf.urls import include, url, patterns


urlpatterns = patterns('product.views',
    url(r'^product/', 'index'),
    # # ���������˵�
    # url(r'^menu/(?P<menuName>(\w){1,10})', 'crm.menu.index'),
)