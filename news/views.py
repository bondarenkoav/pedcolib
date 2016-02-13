from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from news.models import novosti

def news_all(request):
    return render_to_response('newss.html', {
        'newss': novosti.objects.all()
    }
)

def news_one(request, news_id=1):
    return render_to_response('news.html', {
        'news': novosti.objects.get(id=news_id),
    }
)