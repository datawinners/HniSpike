from uuid import uuid4
from couchdb.client import Document
from couchdb.mapping import TextField, IntegerField
from django.db import models
import couch
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
    
    