import logging

from pymongo import MongoClient


def get_mongo_collection():
    try:
        mongo_client = MongoClient(
            "mongodb://sensor-simulation-mongodb-1/sensor_data")
        logging.info("Mongo is successfully connected.")
        db = mongo_client["sensor_data"]
        collection = db["readings"]
        return collection
    except:
        logging.exception("Mongo is not connected successfully.")
