# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from teachers.models import teacher
from django.core.paginator import Paginator

def teachers_all(request, page_number=1):
    args = {}
    all_teachers = teacher.objects.all().filter(post=1)
    current_page = Paginator(all_teachers,10)
    args['teachers'] = current_page.page(page_number)
    return render_to_response('teachers/teachers.html', args)

def teacher_one(request, page_slug):
    args = {}
    args['teacher'] = teacher.objects.get(alias=page_slug)
    return render_to_response('teachers/teacher.html', args)

def leaders_all(request):
    args = {}
    args['leaders'] = teacher.objects.all().filter(post=2)
    return render_to_response('leaders/leaders.html', args)

def leader_one(request, page_slug):
    args = {}
    args['leader'] = teacher.objects.get(alias=page_slug)
    return render_to_response('leaders/leader.html', args)