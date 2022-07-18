from mongoengine import *
# unique=True


class Drink(Document):
    _id = StringField(max_length=200)
    title = StringField(max_length=200, required=True)
    price = IntField(max_length=200)
    description = StringField(max_length=200)
    imageUrl = StringField(max_length=400)