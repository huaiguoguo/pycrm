__author__ = 'guo'
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static


urlpatterns = patterns('app.cheku.views',
    url(r'^index/$', 'index'),
    url(r'^brand/$', 'Brand'),
    url(r'^list/$', 'list'),
)
