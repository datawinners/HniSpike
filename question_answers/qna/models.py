
from django.db import models

# Create your models here.
class Questionnaire():

    def __init__(self, name, description,code):
        self.name = name
        self.description = description
        self.code = code
        self.__questions = []
        

    def AddQuestion(self, question):
        self.__questions.append(question)

    def QuestionCount(self):
        return len(self.__questions)
        
    

class Question():
    def __init__(self, text, code, type, format):
        self.text = text
        self.code = code
        self.type = type
        self.format = format

class Message(object):
    def __init__(self, smsText):
        self.smsText = smsText
        self.tokens = []

    def Validate(self):
        tokens = self.smsText.split(" ")
        d = DummyDataSource()
        qcode = tokens[0]
        qsExists = d.FindQuestionnaire(qcode)
        if not qsExists:
            return False,"Invalid Questionnaire Code"
        questionCodes = tokens[1::2]

        result = map(lambda x: d.FindQuestion(qcode, x), questionCodes)
        if not all(result):
            return False,"Invalid Question Code"
        
        return True,zip(questionCodes,tokens[2::2])


class DummyDataSource():

    q = Questionnaire("Mosquito Net Stock","Stock of mosquito nets.","MSQ")
    q.AddQuestion(Question("How many nets do you need?","MTN","Numeric","#"))
    q.AddQuestion(Question("When do you need?","DTE","Date","dd.mm.yyyy"))
    q.AddQuestion(Question("Stock level?","STK","Numeric","0-#"))

    Questionnaires = [q]
        
    def FindQuestionnaire(self, code):
        questionnaire = filter(lambda x:x.code == code, self.Questionnaires)
        return questionnaire[0] if questionnaire else None

    def FindQuestion(self, qsCode, code):
        qq= self.FindQuestionnaire(qsCode)
        if qq is None:
            return None
        question = filter(lambda x:x.code == code, qq._Questionnaire__questions)
        return None if len(question) == 0 else question[0]
        

    




