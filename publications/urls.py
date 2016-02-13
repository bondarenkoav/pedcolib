__author__ = 'ipman'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<publication_id>\d+)/$', 'publications.views.publication_one'),
)