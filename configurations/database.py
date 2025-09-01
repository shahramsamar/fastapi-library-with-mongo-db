from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



uri = "mongodb://localhost:27017/?directConnection=true"
# create a new client and connect to the server
clinet = MongoClient(uri,server_api=ServerApi("1"))


# send a ping to confrim a successful connection
try:
    clinet.admin.command("ping")
    print("Pinged your deployment.You successfilly connected to MongoDb!!!!!")
except Exception as e:
    print(e)    


db = clinet.library
books_collection = db["books"]
    