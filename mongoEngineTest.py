from mongoengine import *
import datetime


connect('mongoengine_test', host='localhost', port=27017)
class Post(Document):
    name = StringField(required=True, max_length=200)
    genre = StringField(required=True)
    episodes = IntegerField(required=True, max_length=50)
    type = StringField(default=datetime.datetime.now)