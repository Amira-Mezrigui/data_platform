from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/db"
mongo = PyMongo(app)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/data', methods=['GET'])
def get_data():
    data = mongo.db.col.find()
    return jsonify([item for item in data])

@app.route('/data', methods=['POST'])
def add_data():
    name = request.json['name']
    age = request.json['age']
    mongo.db.mycollection.insert_one({'name': name, 'age': age})
    return jsonify({'message': 'data added successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)