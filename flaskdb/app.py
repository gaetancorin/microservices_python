from flask import Flask, render_template, make_response, jsonify, request
import db
from bson.json_util import dumps, loads

app = Flask(__name__)
HOST= "0.0.0.0"
PORT = 3000

# reçoit une req GET, envoi en res toute la collection.
@app.route("/getAll", methods=["GET"])
def getAll():
    Cursor = db.collection.find({})
    res = []
    for i in Cursor:
        res.append(i)
    for i in range(len(res)):
        res[i]["_id"] = str(res[i]["_id"])
    print(res, "\n")
    res = make_response(jsonify(res), 200)
    return res
# def allCollection():
#     Cursor = db.collection.find({})
#     malist = list(Cursor)
#     print(malist)
#     res = make_response(dumps(malist), 200)
#     return res

#test to insert data to the data base
@app.route("/createOne", methods=["POST"])
def createOne():
    req = request.get_json()
    res = {"title": req["title"]}
    print(res)
    # db.collection.insert_one({"name": "bogosse"})
    return "Connected to the data base!"


#     title
# :
# "appareil photo"
# description
# :
# "de très haute qualité"
# imageUrl
# :
# "https://cdn.pixabay.com/photo/2019/06/11/18/56/camera-4267692_1280.jpg"
# userId
# :
# "userID40282382"
# price
# :
# 24000

@app.route('/')
def flask_mongodb_atlas():
    return "Tout les chemins mènent a Rome, mais pas celui là..."

    
if __name__ == "__main__":
    print("Server running in port", PORT)
    app.run(host=HOST, port=PORT, debug=True)