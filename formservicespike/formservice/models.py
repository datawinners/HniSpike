from uuid import uuid4
from couchdb.mapping import TextField, IntegerField, DictField, ListField, Document
from django.db import models

from formservice.connection import Connection


class FormDocument(Document):
    """
        Common struture for all Document object we are retriving from
        CouchDb for the datadict.
    """
    def __init__(self, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)
        if not getattr(self, 'id', None):
            self.id = uuid4().hex

    @classmethod
    def load(cls, *args, **kwargs):
       return Document.load(Connection().db, *args, **kwargs)


    def save(self):
        return self.store(Connection().db)


    @classmethod
    def create(cls, *args, **kwargs):
        obj = cls(*args, **kwargs)
        obj.save()
        return obj


    @classmethod
    def query(cls, map_function, reduce_func="",
              *args, **kwargs):
        return Document.query(Connection().db, map_function,
                              reduce_func, *args, **kwargs)

class Question(FormDocument):

    description =TextField()
    answer_data_type = IntegerField()

    def __init__(self, *args, **kwargs):
        FormDocument.__init__(self, *args, **kwargs)


    def check(self):
        return self.description
    

#class Questionnaire(FormDocument):
#    #question_list = ListField()
#
#class Questionnaire(FormDocument):
#    question_list = ListField()
#
#    def __init__(self,q_list):
#        self.question_list = q_list

class Dictionary:
    dictionary = {"age":1,"name":2}

    def validate(self,key):
        return key in self.dictionary

    def return_value(self,key):
        return self.dictionary[key]
        
