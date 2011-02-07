"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from qna.models import DummyDataSource, Message
from qna.parsers import ParserFactory

class QuestionnaireTest(TestCase):
    def setUp(self):
        self.q = DummyDataSource().Questionnaires[0]

    def test_should_create(self):
        self.assertEquals(3, self.q.QuestionCount())
        self.assertEquals(2, len(filter(lambda x:x.type=="Numeric",self.q._Questionnaire__questions)))

    def test_should_accept_submissions(self):
        pass

    def test_should_process_valid_messages(self):
        sms="MSQ MTN 09 DTE 22.02.2010 STK 89"
        m=Message(sms)
        success, result  = m.Validate()

        self.assertTrue(success)
        self.assertEquals(3, len(result))

    def test_should_process_invalid_messages(self):
        sms="ABC MTN 09 DTE 22.02.2010 STK 89"
        m=Message(sms)
        success, result  = m.Validate()

        self.assertFalse(success)
        self.assertEquals("Invalid Questionnaire Code", result)


    def test_should_fail_for_invalid_question_code(self):
        sms="MSQ ABC 09 DTE 22.02.2010 STK 89"
        m=Message(sms)
        success, result  = m.Validate()

        self.assertFalse(success)
        self.assertEquals("Invalid Question Code", result)

class ParserTest(TestCase):

    def test_should_validate_numeric(self):
        value = 20
        parsers=ParserFactory(value)
        p = parsers.get_parser("0")
        self.assertTrue(p.validateFor("0",value))

    def test_should_validate_int_range(self):
        value = 30
        parsers=ParserFactory(type(value))
        p = parsers.get_parser("0-0")
        self.assertTrue(p.validateFor("20-40", value))

    def test_should_validate_float_range(self):
        value = 30.5
        parsers=ParserFactory(type(value))
        p = parsers.get_parser("0-0")
        self.assertTrue(p.validateFor("20.5-40.6", value))

    def test_should_not_validate_invalid_float_range(self):
        value = 10.4
        parsers=ParserFactory(type(value))
        p = parsers.get_parser("0-0")
        self.assertFalse(p.validateFor("20.5-40.6", value))

    def test_should_validate_min_range(self):
        value = 30
        parsers=ParserFactory(type(value))
        p = parsers.get_parser("x-0")
        self.assertTrue(p.validateFor("20-0", value))

    def test_should_validate_max_range(self):
        value = 30
        parsers=ParserFactory(type(value))
        p = parsers.get_parser("0-x")
        self.assertTrue(p.validateFor("0-40", value))

