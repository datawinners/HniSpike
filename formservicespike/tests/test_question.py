from formservice.models import Question

class test_question:
    def test_should_return_and_save_question_object(self):
        q = Question(description="wsdf",answer_data_type = 2)
        q.save()
        assert q.check()=="wsdf"

  