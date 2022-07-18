
from flask import Flask, render_template, make_response, jsonify, request
from mongoengine import connect
from models import Drink
from bson.json_util import dumps, loads

connect("flaskdb2",host="mongodb+srv://gaetan:1234@cluster0.wxcxg.mongodb.net/?retryWrites=true&w=majority")

app = Flask(__name__)
HOST= "0.0.0.0"
PORT = 3000


# ///////////////   MONGO ENGIINE   /////////////

# GET ALL DRINKS
@app.route("/getAllDrinks", methods=["GET"])
def getAllDrinks():
    drinks = Drink.objects()
    return make_response(drinks.to_json(), 200)


# GET ONLY ONE DRINK
@app.route("/getOneDrink/<titleDrink>", methods=["GET"])
def getOneDrink(titleDrink):
    drink = Drink.objects(title = titleDrink )
    return make_response(drink.to_json(), 200)

# get all datas by json and create an element on mongodb
# CREATE A DRINK
@app.route("/createDrink", methods=["POST"])
def createDrink():
    req = request.get_json()
    createDrink = Drink(title= req['title'], price= req['price'], description=req['description'], imageUrl=req['imageUrl'])
    createDrink.save()
    res = make_response(jsonify({ "message":"new Drink create"}), 200)
    return res

# get mongodb element by json title, and update it
# UPDATE A DRINK
@app.route("/updateDrink", methods=["PUT"])
def updateDrink():
    req = request.get_json()
    updatedrink = Drink.objects( title = req['title'])
    updatedrink.update_one(set__title= req['title'])
    updatedrink.update_one(set__price= req['price'])
    updatedrink.update_one(set__description= req['description'])
    updatedrink.update_one(set__imageUrl= req['imageUrl'])
    res = make_response(jsonify({ "message":"Drink updated"}), 200)
    return res

# get mongodb element by json title, and delete it
# DELETE A DRINK
@app.route("/deleteDrink", methods=["DELETE"])
def deleteDrink():
    req = request.get_json()
    deletedrink = Drink.objects( title = req['title'])
    deletedrink.delete()
    res = make_response(jsonify({ "message":"Drink deleted"}), 200)
    return res



@app.route('/')
def youAreLost():
    return "Tout les chemins mènent à Rome, mais pas celui là..."

    
if __name__ == "__main__":
    print("Server running in port", PORT)
    app.run(host=HOST, port=PORT, debug=True)