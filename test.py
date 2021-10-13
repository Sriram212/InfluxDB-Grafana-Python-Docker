import sys
from datetime import datetime
import time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import random

# You can generate a Token from the "Tokens Tab" in the UI
token = "ONthwLTbNcqUbymJtzskFSqE-A8PSg7xfG4_UrB6yf1TN_x7-IICwSOqogMUKDFWnZlvDXHkVEBnaAKwKq8q-Q=="
org = "test"
bucket = "firstDB"
client = InfluxDBClient(url="http://influxdb:8086", token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)
delete_api = client.delete_api()
delete_api.delete('2021-10-01T00:00:00Z', datetime.utcnow(), '_measurement="mem"', bucket=bucket, org=org)

seconds = 5
t_end = time.time() + seconds

while time.time() < t_end:
    # do whatever you do
    randomInt = round(random.uniform(0.00, 99.99), 2)
    point = point = Point("mem")\
        .tag("Stock", "TSLA")\
        .field("value", randomInt)\
        .time(datetime.utcnow(), WritePrecision.NS)
    write_api.write(bucket, org, point)