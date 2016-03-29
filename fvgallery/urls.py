__author__ = 'ipman'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^photo/(?P<id_photo>\d+)/$', 'fvgallery.views.photo_album_one'),
    url(r'^video/(?P<id_video>\d+)/$', 'fvgallery.views.video_one'),

    url(r'^photo/$', 'fvgallery.views.photo_all'),
    url(r'^video/$', 'fvgallery.views.video_all'),
)