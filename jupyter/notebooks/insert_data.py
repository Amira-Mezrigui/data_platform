from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017/")
db = client.db

data = [
    {"name": "Amira", "age": 29},
    {"name": "Amir", "age": 30},
    {"name": "LEA", "age": 35}
]

db.col.insert_many(data)
print("Data inserted successfully")