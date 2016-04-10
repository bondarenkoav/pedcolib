# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from teachers.models import teacher, teacher_photo_album
from django.core.paginator import Paginator

def teachers_all(request, page_number=1):
    args = {}
    current_page = Paginator(teacher.objects.filter(post=1).order_by('fullname'),10)
    args['teachers'] = current_page.page(page_number)
    return render_to_response('teachers/teachers.html', args)

def teacher_one(request, page_slug):
    args = {}
    one_teacher = teacher.objects.get(alias=page_slug)
    args['teacher'] = one_teacher
    args['teacher_album'] = teacher_photo_album.objects.filter(teacher=one_teacher.id)
    #args['teacher_album'] = teacher_photo_album.objects.get(teacher_id=one_teacher.id)
    return render_to_response('teachers/teacher.html', args)

def leaders_all(request, page_number=1):
    args = {}
    current_page = Paginator(teacher.objects.filter(post=2).order_by('fullname'),10)
    args['leaders'] = current_page.page(page_number)
    return render_to_response('leaders/leaders.html', args)

def leader_one(request, page_slug):
    args = {}
    one_leader = teacher.objects.get(alias=page_slug)
    args['leader'] = one_leader
    args['teacher_album'] = teacher_photo_album.objects.filter(teacher=one_leader.id)
    return render_to_response('leaders/leader.html', args)

def veterans_all(request, page_number=1):
    args = {}
    current_page = Paginator(teacher.objects.all().filter(post=3).order_by('fullname'),10)
    args['veterans'] = current_page.page(page_number)
    return render_to_response('veterans/veterans.html', args)

def veteran_one(request, page_slug):
    args = {}
    one_veteran = teacher.objects.get(alias=page_slug)
    args['veteran'] = one_veteran
    args['teacher_album'] = teacher_photo_album.objects.filter(teacher=one_veteran.id)
    return render_to_response('veterans/veteran.html', args)