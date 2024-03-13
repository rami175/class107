import pymongo
import certifi
con_str = "mongodb+srv://ramicesar175:123456ram@107.y7se7sx.mongodb.net/?retryWrites=true&w=majority&appName=107"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("107")