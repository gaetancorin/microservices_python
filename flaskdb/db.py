from flask_pymongo import pymongo

cluster = pymongo.MongoClient("mongodb+srv://gaetan:1234@cluster0.wxcxg.mongodb.net/?retryWrites=true&w=majority")
db = cluster["pythondb"]
collection = db["pythondb"]
