from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from .models import graduate
from .forms import GraduateForm

def graduates_all(request, page_number=1):
    args = {}
    args.update(csrf(request))
    all_graduates = graduate.objects.filter(veryfid_data=True)
    current_page = Paginator(all_graduates,6)
    args['graduates'] = current_page.page(page_number)
    args['form'] = GraduateForm
    return render_to_response('graduates.html', args)

def addgraduate(request):
    if request.POST:
        form = GraduateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('/graduates/')