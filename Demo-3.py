from pymongo import MongoClient

con = MongoClient("mongodb://localhost:27017")

db = con["mydatabase"]

col = db["mycollection"]

# Fetching the first document
doc = col.find_one()
print(doc)

# Fetching all the documents
doc_list = col.find()
for d in doc_list:
    print(d)
    
# Fetching based on condition
doc_list = col.find({"Name":"Partha"})
for d in doc_list:
    print(d)
    
doc_list = col.find({"Age":{"$gte":20}})
for d in doc_list:
    print(d)
    
# Fetching based on regex
doc_list = col.find({"Name":{"$regex":"^P"}})
for d in doc_list:
    print(d)
    
# Projection - Filtering columns
doc_list = col.find({},{"_id":0,"Name":1,"Age":1})
for d in doc_list:
    print(d)    

##### List of operators in MongoDB #####
'''
$eq :: Equal to
$ne :: Not equal
$gt :: Greater than
$gte :: Greater than or equal to
$lt :: Less than
$lte :: Less than or equal to
'''
########################################