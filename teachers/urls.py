__author__ = 'ipman'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<teacher_id>\d+)/$', 'teachers.views.teacher_one'),
    url(r'^', 'teachers.views.teachers_all'),
)