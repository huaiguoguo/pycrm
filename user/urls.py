__author__ = 'guo'

from django.conf.urls import include, url, patterns


urlpatterns = patterns('user.views',
    url(r'^index/$', 'index'),
)
