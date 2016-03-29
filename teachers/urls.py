__author__ = 'ipman'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^teachers/page/(?P<page_number>\d+)/$', 'teachers.views.teachers_all'),
    url(r'^teachers/teacher/(?P<page_slug>[-\w]+)/$', 'teachers.views.teacher_one'),  #/persons/teachers/teacher/aleksandrova-iuliia-viktorovna/
    url(r'^teachers/$', 'teachers.views.teachers_all'),

    url(r'^leaders/leader/(?P<page_slug>[-\w]+)/$', 'teachers.views.leader_one'),
    url(r'^leaders/', 'teachers.views.leaders_all'),
)