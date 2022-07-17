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
# return du code html
@app.route("/")
def home():
    return "<h1 style='color:blue;'>Bienvenue sur la page home</h1>", 200

# return un template html
@app.route('/template')
def template():
    return render_template('index.html')

# recoit en req get des informations dans l'url et le transforme en une res json
@app.route('/qstring')
def query_string():
    if request.args:
        req = request.args
        res = {}
        for key, value in req.items():
            res[key] = value
        res = make_response(jsonify(res), 200)
        return res
    res = make_response(jsonify({ "error":"No query string"}), 400)
    return res

# envois la variable INFO qui contient un dictionnaire qui sera jsonify
@app.route('/json')
def send_json():
    res = make_response(jsonify(INFO), 200)
    return res

# recherche dans INFO la collection demander, vérifie que le membre existes, et res le json du membre
@app.route('/json/<collection>/<member>')
def get_data(collection, member):
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
# recoit la collection par l'url, les key:valeurs par la méthode post, et si la collection n'existe pas, les rajoute dans la variable INFO
@app.route('/json/<collection>', methods=["POST"])
def create_collection(collection):
    req = request.get_json()
    if collection in INFO:
        res = make_response(jsonify({ "error":"collection exists"}), 400)
        return res
    INFO.update({collection: req})
    res = make_response(jsonify({ "message":"collection create"}), 200)
    return res

# //////////////     METHODE PUT    /////////////////////////
# recoit un json {"new":<elementModifié>} par la methode PUT, 
# puis modifie le membre de la collection passé par l'url
@app.route('/json/<collection>/<member>', methods=["PUT"])
def update_collection(collection, member):
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
# supprime la collection passé en url par la méthode DELETE
@app.route('/json/<collection>', methods=["DELETE"])
def delete_collection(collection):
    if collection in INFO:
        del INFO[collection]
        res = make_response(jsonify(INFO), 200)
        return res
    res = make_response(jsonify({ "error":"collection not found"}), 400)
    return res



if __name__ == "__main__":
    print("Server running in port", PORT)
    app.run(host=HOST, port=PORT, debug=True)


