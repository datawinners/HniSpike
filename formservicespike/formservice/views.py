# Create your views here.

from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render_to_response
from formservice.models import Dictionary, Question

def process_form(request):
    if request.method == 'POST':
        query_dict = request.post
        d = Dictionary()
        datatype =  query_dict.__getitem__("answer_type")
        if not d.validate(datatype):
            render_to_response(HttpResponseBadRequest())
        else:
            q = Question(query_dict.__getitem__("description"),d.return_value(datatype))
            q.save()
            render_to_response(HttpResponse("Thank-you"))

def main_form(request):
       return render_to_response('formservice/index.html')
