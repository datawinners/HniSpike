from formservice.models import Question, Questionnaire
""" Run couch and uncomment the saves """

class test_question:
    def test_should_return_and_save_question_object(self):
        q = Question(description="wsdf",answer_data_type = 2)
        #q.save()
        assert q.check()=="wsdf"

    def test_should_return_and_save_questionnaire_object(self):
        q1 = Question(description="wsdf",answer_data_type = 2)
        q2 = Question(description="abcd",answer_data_type = 1)
        qlist = [q1,q2]
        q=Questionnaire(question_list=qlist,description="abcdef")
        #q.save()
        assert q.check()=="wsdf"