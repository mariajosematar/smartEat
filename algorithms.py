import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from pymongo import MongoClient

# connect to the database
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# retrieve the inventory collection
inventory_collection = db["inventory"]

# Load inventory data from the database
inventory = pd.DataFrame(list(inventory_collection.find()))

# Convert expiration_date to days_until_expiration
inventory["days_until_expiration"] = (pd.to_datetime(inventory["expiration_date"]) - pd.Timestamp.now()).dt.days

# Create target variable
inventory["expires_soon"] = inventory["days_until_expiration"].apply(lambda x: x <= 14)

# Create feature matrix
X = inventory[["quantity", "location"]]
y = inventory["expires_soon"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

