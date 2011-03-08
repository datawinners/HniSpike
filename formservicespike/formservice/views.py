# Create your views here.

from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render_to_response
from formservice.models import Dictionary, Question

def process_form(request):
    if request.method == 'POST':
        query_dict = request.POST
        d = Dictionary()
        datatype =  query_dict.__getitem__("answer_type")
        if not d.validate(datatype):
            return HttpResponse("muhahahaha")
        else:
            q = Question(query_dict.__getitem__("question"),d.return_value(datatype))
            q.save()
        return render_to_response('Thank you')

def main_form(request):
       return render_to_response('formservice/index.html')
