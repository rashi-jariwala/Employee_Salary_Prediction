import pymongo
import config

client = pymongo.MongoClient(config.Config.MONGO_URI)

db = client[config.Config.DATABASE_NAME]

users_collection = db["users"]

prediction_collection = db["prediction_history"]