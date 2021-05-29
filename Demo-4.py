from pymongo import MongoClient

con = MongoClient("mongodb://localhost:27017")

db = con["mydatabase"]

col = db["mycollection"]

# Sorting the fetched data
doc_list = col.find().sort("Age",1) # 1: Asceding , -1: Descending, Default is Ascending
for doc in doc_list:
    print(doc)
    
# Limit the numberof document fetched
doc_list = col.find().limit(3) 
for doc in doc_list:
    print(doc)