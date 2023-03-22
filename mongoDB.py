from pymongo import MongoClient

# connect to the database
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# retrieve the inventory collection
inventory_collection = db["inventory"]
