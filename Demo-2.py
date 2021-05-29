from pymongo import MongoClient

con = MongoClient("mongodb://localhost:27017")

# Selecting a database
db = con["mydatabase"]      # If the database exists, the database will be returned else, a database will be created.

### Hint :: In MongoDB a database wll be created only if it has some content.

# Selecting a collection
collection = db["mycollection"]     # If the collection exists, collection object will be returned. Else, collection will be created and then the new collection object will be returned.

# Inserting a record or document to a collection
# A document is like a collection of key-value pair of property and value
document = {"Name":"Alok","ID":1002}
return_val = collection.insert_one(document)

# Getting the _id of the inserted document
print(return_val.inserted_id)

# Inserting many documents
document_list = [{"Name":"Pramesh","ID":2001,"Age":20},\
                 {"Name":"Partha","ID":2002,"Grade":"A"},\
                 {"Name":"Tapan","ID":2003,"Age":25}]
collection.insert_many(document_list)

# Fetching the list of database available in the server.
db_list = con.list_database_names()
print(db_list)

# Fetching the list of collections available in the database
col_list = db.list_collection_names()
print(col_list)

