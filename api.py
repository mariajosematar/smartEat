from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client["food_management_system"]
inventory_collection = db["inventory"]

# Add inventory endpoint
@app.route("/inventory", methods=["POST"])
def add_inventory():
    inventory = request.json
    inventory_collection.insert_one(inventory)
    return jsonify({"message": "Inventory added successfully"})

# Modify inventory endpoint
@app.route("/inventory/<food_name>", methods=["PUT"])
def modify_inventory(food_name):
    new_inventory = request.json
    inventory_collection.update_one({"food_name": food_name}, {"$set": new_inventory})
    return jsonify({"message": "Inventory updated successfully"})

# Retrieve inventory endpoint
@app.route("/inventory/<food_name>", methods=["GET"])
def get_inventory(food_name):
    inventory = inventory_collection.find_one({"food_name": food_name})
    return jsonify(inventory)
