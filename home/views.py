from django.shortcuts import render_to_response
from home.models import Slider
from responses.models import response
from news.models import novosti
from publications.models import publics

def home_get_info(request):
    return render_to_response('home.html', {
        'slides'  : Slider.objects.all(),
        'news_all': novosti.objects.all(),
        'responses': response.objects.all(),
        'publications': publics.objects.all()[:12]
    }
)