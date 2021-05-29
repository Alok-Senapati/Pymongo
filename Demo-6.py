from pymongo import MongoClient

con = MongoClient("mongodb://localhost:27017")

db = con["mydatabase"]

col = db["mycollection"]

# Updating document
col.update_one({},{"$set":{"Name":"Alok Senapati"}}) # Updating the first document in the collection
col.update_one({"Name":"Partha"},{"$set":{"Name":"P S Muduli"}}) # Update the first document whose name is Partha
update_obj = col.update_many({"Name":"Tapan"},{"$set":{"Name":"T K Kar"}}) # Updates all documents where name is Tapan
print(update_obj.modified_count) # Prints number of document modified
update_obj = col.update_many({},{"$set":{"Age":30}}) # Updates all documents in the collection
print(update_obj.modified_count)