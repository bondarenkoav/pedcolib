__author__ = 'ipman'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', 'home.views.home_get_info'),
)