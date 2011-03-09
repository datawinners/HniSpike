from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render_to_response
from formservice.models import Dictionary, Question, Questionnaire, Questionnaire

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def process_form(request):
    d = Dictionary()
 #   questionnaire = Questionnaire()
    if request.method == 'POST':
        query_dict = request.POST
        query_list = query_dict.values()
        answer_type_list = query_list[0:len(query_list)/2:1]
        desc_list = query_list[len(query_list)/2:len(query_list):1]
        q_list = []
        for index in range(len(desc_list)):
            if not d.validate(answer_type_list[index]):
                    return HttpResponse("error")
            else:

                q = Question(description=desc_list[index],answer_data_type=d.return_value(answer_type_list[index]))
                q_list.append(q)

        questionnaire = Questionnaire(question_list=q_list,description = "My form")
        questionnaire.save()
        return render_to_response('formservice/process.html')


def main_form(request):
       return render_to_response('formservice/index.html')
