from pymongo import MongoClient

con = MongoClient("mongodb://localhost:27017")

db = con["mydatabase"]

col = db["mycollection"]

# Before Droping
doc_list = col.find()
for doc in doc_list:
    print(doc)
 
# Droping a collection
col.drop()

# After Droping
doc_list = col.find()
for doc in doc_list:
    print(doc)