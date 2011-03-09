from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render_to_response
from formservice.models import Dictionary, Question

def process_form(request):
    d = Dictionary()
    questionnaire = Questionnaire()
    if request.method == 'POST':
        query_dict = request.POST
#        for key,value in query_dict:



#            if(key == "answer_type")
#                datatype =  query_dict["answer_type"]
#                if not d.validate(datatype):
#                    return HttpResponse("error")
#                else:
#                q = Question(desc=query_dict["question"],ans_data_type=d.return_value(datatype))
#            q.save()
        return HttpResponse("Thank you")

def main_form(request):
       return render_to_response('formservice/index.html')
