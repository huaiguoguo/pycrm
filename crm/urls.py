__author__ = 'guo'

from django.conf.urls import include, url, patterns


urlpatterns = patterns(
    url(r'^crm/', 'crm.views.index'),
)