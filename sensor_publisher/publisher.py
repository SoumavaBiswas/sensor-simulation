import json
import random
import time

import paho.mqtt.client as mqtt

# Define MQTT broker details
broker_address = "sensor-simulation-broker-1"
broker_port = 2883

# Simulate sensor readings
sensors = [
    {"sensor_id": "sensor1", "topic": "sensors/temperature"},
    {"sensor_id": "sensor2", "topic": "sensors/humidity"}
]

client = mqtt.Client()

# Simulating random sensor value.
# For sensor 1 value can be anything between 10 to 19.
# For sensor 2 value can be anything betweeb 20 to 29.abs
# Since we mimic two sensors only, for any other sensor id it will throw error.


def get_sensor_value(sensor_id):
    if sensor_id == "sensor1":
        return str(round(random.uniform(10, 20), 2))
    if sensor_id == "sensor2":
        return str(round(random.uniform(20, 30), 2))
    else:
        raise ValueError("Unknown Sensor Id.")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


client.on_connect = on_connect
client.connect(broker_address, broker_port, 60)

while True:
    for sensor in sensors:
        payload = {
            "sensor_id": sensor["sensor_id"],
            # Simulate values
            "value": get_sensor_value(sensor["sensor_id"]),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        client.publish(sensor["topic"], json.dumps(payload))
    time.sleep(10)
