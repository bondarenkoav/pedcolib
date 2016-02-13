__author__ = 'ipman'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<group_id>\d+)/$', 'groups.views.group_one'),
    url(r'^', 'groups.views.groups_all'),
)