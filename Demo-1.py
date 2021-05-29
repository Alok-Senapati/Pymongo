from pymongo import MongoClient # MongoClient is used for connecting to MongoDB.

# Connecting a connection and Connection object.
# MongoClient takes a connection string to connect to MongoDB database.
# Connection string systax :: "mongodb://hostname:portnumber/"
con = MongoClient("mongodb://localhost:27017")
print(type(con))
