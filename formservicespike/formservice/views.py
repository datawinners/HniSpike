from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render_to_response
from formservice.models import Dictionary, Question, Questionnaire, Questionnaire

NUMBER_OF_FIELDS = 2

def process_form(request):
    d = Dictionary()
    if request.method == 'POST':
        query_dict = request.POST
        query_list = query_dict.values()
        answer_type_list = query_list[0:len(query_list)/ NUMBER_OF_FIELDS:1]
        desc_list = query_list[len(query_list)/NUMBER_OF_FIELDS:len(query_list):1]
        q_list = []
        for index in range(len(desc_list)):
            if not d.validate(answer_type_list[index]):
                    return HttpResponse("error")
            else:
                q = Question(description=desc_list[index],answer_data_type=d.return_value(answer_type_list[index]))
                q_list.append(q)
        questionnaire = Questionnaire(question_list=q_list,description = "My form")
        #questionnaire.save()
        return render_to_response('formservice/process.html',{'questionnaire': questionnaire})


def main_form(request):
       return render_to_response('formservice/index.html')
