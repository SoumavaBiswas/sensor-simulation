import json
from datetime import datetime, timedelta

from conn.mongo_connection import get_mongo_collection
from conn.redis_connection import get_redis_client
from fastapi import FastAPI
from util.utils import datetime_format, is_valid_datetime

app = FastAPI()

collection = get_mongo_collection()
redis_client = get_redis_client()


@app.get("/sensor_readings")
def get_sensor_readings(start: str = None, end: str = None):

    # If no start time and end time are provided,
    # the endpoint will retrieve sensor data from the last hour.
    if not end:
        end = datetime.utcnow().strftime(datetime_format)
    if not start:
        start = (datetime.utcnow() - timedelta(hours=1)
                 ).strftime(datetime_format)

    # If the provided start and end values are not in a valid datetime format (TZ format),
    # a dictionary containing an error message will be returned."
    if is_valid_datetime(start) and is_valid_datetime(end):
        query = {"timestamp": {"$gte": start, "$lte": end}}
        if collection is not None:
            data = list(collection.find(query))
            for doc in data:
                doc["_id"] = str(doc["_id"])
        else:
            data = []
    else:
        data = {"detail": "Invalid datetime format. Please provide in TZ format"}
    return data


@app.get("/latest_readings/{sensor_id}")
def get_latest_readings(sensor_id: str):
    data = redis_client.lrange(sensor_id, 0, 9)
    return [json.loads(entry) for entry in data]
