from formservice.models import Question

class test_question:
    def test_should_return_question_object(self):
        q = Question(description="wsdf",answer_data_type = 2)
        assert q.check()=="wsdf"

  