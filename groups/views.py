from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from groups.models import group

def groups_all(request):
    return render_to_response('groups.html', {
        'groups': group.objects.all()
    }
)

def group_one(request, group_id=1):
    return render_to_response('group.html', {
        'group': group.objects.get(id=group_id),
    }
)