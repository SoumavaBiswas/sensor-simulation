import json

import paho.mqtt.client as mqtt
from pymongo import MongoClient
from redis import StrictRedis

# Define MQTT broker details
broker_address = "sensor-simulation-broker-1"
broker_port = 2883

# MongoDB setup
mongo_client = MongoClient("mongodb://sensor-simulation-mongodb-1/sensor_data")
db = mongo_client["sensor_data"]
collection = db["readings"]

# Redis setup
redis_client = StrictRedis(host="redis", port=6379, decode_responses=True)


def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    collection.insert_one(payload)
    sensor_id = payload["sensor_id"]

    # Convert ObjectId to string before inserting into Redis
    payload["_id"] = str(payload["_id"])

    # Update the latest readings in Redis
    redis_client.lpush(sensor_id, json.dumps(payload))
    redis_client.ltrim(sensor_id, 0, 9)  # Keep only the latest 10 readings


client = mqtt.Client()
client.on_message = on_message
client.connect(broker_address, broker_port, 60)
client.subscribe("sensors/#")

client.loop_forever()
