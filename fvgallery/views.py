# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from .models import Album,Photo,Video

def photo_all(request):
    args = {}
    args['photo_list'] = Album.objects.all().order_by('-publish_date')
    return render_to_response('photo_album.html', args)

def video_all(request):
    args = {}
    args['video_list'] = Video.objects.all()                      #Video.objects.all().order_by('-publish_date')
    return render_to_response('video_gallery.html', args)

def photo_album_one(request, id_album=1):
    args = {}
    args['album_one'] = Photo.objects.all().filter(album_id=id_album)
    return render_to_response('photo.html', args)

def video_one(request, id_video=1):
    args = {}
    args['video'] = Video.objects.get(id=id_video)
    return render_to_response('video.html', args)