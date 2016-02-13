__author__ = 'ipman'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<news_id>\d+)/$', 'news.views.news_one'),
    url(r'^', 'news.views.news_all'),
)