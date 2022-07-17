from flask import Flask, render_template, make_response, jsonify, request
import db

app = Flask(__name__)
HOST= "0.0.0.0"
PORT = 3000

#test to insert data to the data base
@app.route("/test")
def test():
    db.collection.insert_one({"name": "bogosse"})
    return "Connected to the data base!"

@app.route('/')
def flask_mongodb_atlas():
    return "flask mongodb atlas!"

    
if __name__ == "__main__":
    print("Server running in port", PORT)
    app.run(host=HOST, port=PORT, debug=True)