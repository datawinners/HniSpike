
# Create your models here.
from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, StringField

class Link(Document):
    url = StringField()


class Bookmarks(Document):
    title = StringField()
    user = ReferenceField(User)
    link = ReferenceField(Link)

