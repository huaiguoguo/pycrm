__author__ = 'guo'
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static


urlpatterns = patterns('menu.views',
    url(r'^index/(?P<menuName>(\w){1,10})$', 'index'),
)
