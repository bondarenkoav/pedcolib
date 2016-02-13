__author__ = 'ipman'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^add_response/$', 'responses.views.add_response'),
     url(r'^page/(\d+)/$', 'responses.views.responses_all'),
     url(r'^', 'responses.views.responses_all'),
)