from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)

HOST= "0.0.0.0"
PORT = 3200

INFO = {
    "languages":{
        "es":"espagnol",
        "en":"English",
        "fr":"French"
    },
    "color":{
        "g":"green",
        "r":"red",
        "b":"blue"
    }
}
# ///////////////   METHODE GET   //////////////////
# SEND HTML
@app.route("/")
def sendHtml():
    return "<h1 style='color:blue;'>Bienvenue sur la page home</h1>", 200

# SEND TEMPLATE
@app.route('/template/')
def sendTemplate():
    return render_template('index.html')

# QUERYSTRING TO JSON
@app.route('/qstring')
def querystringToJson():
    if request.args:
        req = request.args
        res = {}
        for key, value in req.items():
            res[key] = value
        res = make_response(jsonify(res), 200)
        return res
    res = make_response(jsonify({ "error":"No query string"}), 400)
    return res

# SEND ALL COLLECTIONS BY JSON
@app.route('/json')
def sendAllJson():
    res = make_response(jsonify(INFO), 200)
    return res

#  READ ONE MEMBER
@app.route('/json/<collection>/<member>')
def sendOneMember(collection, member):
    if collection in INFO:
        member = INFO[collection].get(member)
        if member:
            res = make_response(jsonify({ "res": member}), 200)
            return res
        res = make_response(jsonify({ "error":"No member in collection"}), 400)
        return res
    res = make_response(jsonify({ "error":"No collection found"}), 400)
    return res
        
# //////////////     METHODE POST     /////////////////////////
# get collection name by url and members names by json and create it
# CREATE COLLECTION
@app.route('/json/<collection>', methods=["POST"])
def createCollection(collection):
    req = request.get_json()
    if collection in INFO:
        res = make_response(jsonify({ "error":"collection exists"}), 400)
        return res
    INFO.update({collection: req})
    res = make_response(jsonify({ "message":"collection create"}), 200)
    return res

# //////////////     METHODE PUT    /////////////////////////
# get collection and member by url, new member value is get by Json
# UPDATE MEMBER
@app.route('/json/<collection>/<member>', methods=["PUT"])
def updateMember(collection, member):
    req = request.get_json()
    if collection in INFO:
        if member:
            INFO[collection][member] = req["new"]
            res = make_response(jsonify({ "res":INFO[collection]}), 200)
            return res
        res = make_response(jsonify({ "error":"member not found"}), 400)
        return res
    res = make_response(jsonify({ "error":"collection not found"}), 400)
    return res

# //////////////     METHODE DEL    /////////////////////////
# get collection by url, and delete it
@app.route('/json/<collection>', methods=["DELETE"])
def deleteCollection(collection):
    if collection in INFO:
        del INFO[collection]
        res = make_response(jsonify(INFO), 200)
        return res
    res = make_response(jsonify({ "error":"collection not found"}), 400)
    return res


# Il est important d'avoir " if __name__ == "__main__": " sous les endpoints
if __name__ == "__main__":
    print("Server running in port", PORT)
    app.run(host=HOST, port=PORT, debug=True)


