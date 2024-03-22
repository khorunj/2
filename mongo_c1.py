from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://khorunj:25052005@khorunj.vkjiukc.mongodb.net/?retryWrites=true&w=majority&appName=khorunj"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.ds02

# Decorator
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Error occurred:", e)
    return wrapper

# Shows all the cats
@handle_exceptions
def read_all_cats():
    for i in list(db.cats.find()):
        print(i)

# Shows cat by name
@handle_exceptions
def read_cat(x):
    cursor = db.cats.find({"name": x})
    found = False
    for cat in cursor:
        print(cat)
        found = True
    if not found:
        print("Cat with name", x, "not found")

# Updates cat age by name 
@handle_exceptions
def update_age_byname(name,new_age):
    db.cats.update_one(
        {"name": name},
        {"$set": {"age": new_age}}
        )
    print("Successfully updated age for cat with name:", name)

# Adds feature by name 
@handle_exceptions
def add_feature_byname(name,new_feature):
    db.cats.update_one(
        {"name": name},
        {"$push": {"features": new_feature}}
    )
    print("Successfully added new feature to cat with name:", name)

# Deletes the cat by name 
@handle_exceptions
def delete_byname(name):
    result = db.cats.delete_one({"name": name})
    if result.deleted_count > 0:
        print("Successfully deleted cat with name:", name)
    else:
        print("No cat found with name:", name)

# Deletes all the cats 
@handle_exceptions
def delete_all_cats():
    result = db.cats.delete_many({})
    print("Successfully deleted", result.deleted_count, "cats")



