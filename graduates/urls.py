__author__ = 'ipman'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #url(r'^(?P<graduate_id>\d+)/$', 'graduates.views.graduate_one'),
    url(r'^addgraduate/$', 'graduates.views.addgraduate'),
    url(r'^page/(\d+)/$', 'graduates.views.graduates_all'),
    url(r'^', 'graduates.views.graduates_all'),
)