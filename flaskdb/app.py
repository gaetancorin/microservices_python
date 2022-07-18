from flask import Flask, render_template, make_response, jsonify, request
import db
from bson.json_util import dumps, loads

app = Flask(__name__)
HOST= "0.0.0.0"
PORT = 3000
# création de l' api connecté au front
# reçoit une req GET, envoi en res toute la collection.
@app.route("/api/stuff")
# def allCollection():
#     Cursor = db.collection.find({})
#     res = []
#     for i in Cursor:
#         res.append(i)
#     for i in range(len(res)):
#         res[i]["_id"] = str(res[i]["_id"])
#     print(res, "\n")
#     res = make_response(jsonify(res), 200)
#     return res
def allCollection():
    Cursor = db.collection.find({})
    malist = list(Cursor)
    print(malist)
    res = make_response(dumps(malist), 200)
    return res



        # res = {}
    # for key, value in req:
    #     res[key] = value


#test to insert data to the data base
@app.route("/test")
def test():
    db.collection.insert_one({"name": "bogosse"})
    return "Connected to the data base!"

@app.route('/')
def flask_mongodb_atlas():
    return "Tout les chemins mènent a Rome, mais pas celui là..."

    
if __name__ == "__main__":
    print("Server running in port", PORT)
    app.run(host=HOST, port=PORT, debug=True)