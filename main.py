from pymongo import MongoClient

print("Welcome to pyMongo")
client = MongoClient("mongodb://localhost:27017")
print(client.list_database_names())
db = client['tunir']
print(db.list_collection_names())
collection = db['mySampleConnection']

