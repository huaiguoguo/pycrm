__author__ = 'guo'

from django.conf.urls import include, url, patterns


urlpatterns = patterns('crm.views',
    url(r'^index/$', 'index'),
)
