from django.shortcuts import render_to_response
from teachers.models import teacher

def teachers_all(request):
    return render_to_response('teachers.html', {
        'teachers': teacher.objects.all()
    }
)

def teacher_one(request, teacher_id=1):
    return render_to_response('teacher.html', {
        'teacher': teacher.objects.get(id=teacher_id),
    }
)