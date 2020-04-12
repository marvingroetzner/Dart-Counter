from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://dbUser:1234@clusterdartapp-09n10.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["DartDB"]
collection = db["Player"]

#post nur für das erstmalige erstellen benutzen
#updaten get nur über put
#put erstellt allerdings auch einmalig einen neuen eintrag und updatetd dann nurnoch
put = {"_id": 0, "name": "Philipp", "avg": 2}

collection.insert_one(post)

#testcommit
