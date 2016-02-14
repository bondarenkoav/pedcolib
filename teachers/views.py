from django.shortcuts import render_to_response
from teachers.models import teacher
from django.core.paginator import Paginator

def teachers_all(request, page_number=1):
    args = {}
    all_teachers = teacher.objects.all()
    current_page = Paginator(all_teachers,10)
    args['teachers'] = current_page.page(page_number)
    return render_to_response('teachers.html', args)

def teacher_one(request, teacher_id=1):
    return render_to_response('teacher.html', {
        'teacher': teacher.objects.get(id=teacher_id),
    }
)