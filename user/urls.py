__author__ = 'guo'

from django.conf.urls import include, url, patterns


urlpatterns = patterns('user.views',
    url(r'^user/', 'index'),
    # ���������˵�
    url(r'^menu/(?P<menuName>(\w){1,10})', 'index'),
)