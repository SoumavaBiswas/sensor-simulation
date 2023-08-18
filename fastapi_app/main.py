import json
import logging
from datetime import datetime, timedelta

from fastapi import FastAPI
from pymongo import MongoClient
from redis import StrictRedis

app = FastAPI()

# MongoDB setup
try:
    mongo_client = MongoClient(
        "mongodb://sensor-simulation-mongodb-1/sensor_data")
except:
    logging.exception("Mongo is not connected successfully.")
finally:
    logging.info("Mongo is successfully connected.")
    db = mongo_client["sensor_data"]
    collection = db["readings"]

# Redis setup
redis_client = StrictRedis(host="redis", port=6379, decode_responses=True)


@app.get("/sensor_readings")
def get_sensor_readings(start: str = None, end: str = None):
    if not end:
        end = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    if not start:
        start = (datetime.utcnow() - timedelta(hours=1)
                 ).strftime('%Y-%m-%dT%H:%M:%SZ')

    start_time = start
    end_time = end
    query = {"timestamp": {"$gte": start_time, "$lte": end_time}}
    data = list(collection.find(query))
    for doc in data:
        doc["_id"] = str(doc["_id"])
    return data


@app.get("/latest_readings/{sensor_id}")
def get_latest_readings(sensor_id: str):
    data = redis_client.lrange(sensor_id, 0, 9)
    return [json.loads(entry) for entry in data]
