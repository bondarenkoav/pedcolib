from django.shortcuts import redirect
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.core.paginator import Paginator

from responses.models import response
from responses.forms import ResponsesForm


def responses_all(request, page_number=1):
    args = {}
    args.update(csrf(request))
    all_responses = response.objects.filter(veryfid_data=True)
    current_page = Paginator(all_responses,5)
    args['responses'] = current_page.page(page_number)
    args['form'] = ResponsesForm
    return render_to_response('response.html', args)

def add_response(request):
    if request.POST:
        form = ResponsesForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/response/')