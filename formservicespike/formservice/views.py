from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render_to_response
from formservice.models import Dictionary, Question

def process_form(request):
    if request.method == 'POST':
        query_dict = request.POST
        d = Dictionary()
        datatype =  query_dict["answer_type"]
        if not d.validate(datatype):
            return HttpResponse("muhahahaha")
        else:
            q = Question(desc=query_dict["question"],ans_data_type=d.return_value(datatype))
            q.save()
        return HttpResponse("Thank you")

def main_form(request):
       return render_to_response('formservice/index.html')
