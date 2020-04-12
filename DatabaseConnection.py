from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://dbUser:1234@clusterdartapp-09n10.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["DartDB"]
collection = db["Player"]

post = {"_id": 0, "name": "Philipp", "avg": 2}

collection.insert_one(post)


#kkkdd