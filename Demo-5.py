from pymongo import MongoClient

con = MongoClient("mongodb://localhost:27017")

db = con["mydatabase"]

col = db["mycollection"]

# Deleting document
col.delete_one({}) # Deletes the first document present in rhe collection
col.delete_one({"Name":"Partha"}) # Deletes the first document which satisfies the condition
del_obj = col.delete_many({"Name":"Alok"}) # Deletes all the documents which satisfies the condition
print(del_obj.deleted_count)
del_obj = col.delete_many({}) # Deletes all records from the collection
print(del_obj.deleted_count)
