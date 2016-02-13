from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from publications.models import publics

def publication_one(request, publication_id=1):
    return render_to_response('publication.html', {
        'publication': publics.objects.get(id=publication_id),
    }
)