from pymongo import MongoClient

client = MongoClient()

db = client["food_management_system"]
inventory_collection = db["inventory"]
