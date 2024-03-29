from mongoengine import *

class Drink(Document):
    _id = StringField(max_length=200)
    title = StringField(max_length=200, required=True, unique=True)
    price = IntField(max_length=200)
    description = StringField(max_length=200)
    imageUrl = StringField(max_length=400)