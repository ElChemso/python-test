import socket
import struct
import random

from datetime import datetime
from datetime import timedelta

from cyber_python_test.anomalies.host_connection import HostConnection


def create_host_traffic_with_anomalies(num_data_points=300):
    host_ip = get_random_ip()
    # Start creating the date in the past
    date = datetime.now() - timedelta(days=7)

    # For one of the data points create an anomaly
    anomaly_index = random.randint(0, num_data_points)
    anomaly_field = random.choice(['resp_bytes', 'connection_duration', 'orig_bytes'])

    # Create a set of 4 ips and ports that will become the random destinations
    destination_ips_and_ports = [(get_random_ip(), 8080), (get_random_ip(), 443), (get_random_ip(), 22), (get_random_ip(), 3307)]

    # Populate a list of hosts with values from a random range, at a given point insert an anomaly
    for x in range(0, num_data_points):
        date += timedelta(minutes=random.randint(5, 30))
        dst_ip, dst_port = random.choice(destination_ips_and_ports)

        # For all data points except the anomaly set the response data to be between 300kb and 720kb
        resp_bytes = random.randint(300000, 720000)
        orig_bytes = random.randint(500, 1000)
        connection_duration = random.randint(50, 150)

        # For the anomaly set the response size to be 5mb
        if x == anomaly_index:
            if anomaly_field == 'resp_bytes':
                resp_bytes = random.randint(5000000, 10000000)

            if anomaly_field == 'connection_duration':
                connection_duration = random.randint(500, 700)

            if anomaly_field == 'orig_bytes':
                orig_bytes = random.randint(5000, 7000)

        host = HostConnection(ip=host_ip,
                              destination_ip=dst_ip,
                              destination_port=dst_port,
                              date=date,
                              connection_duration_ms=connection_duration,
                              orig_bytes=orig_bytes,
                              resp_bytes=resp_bytes)

        yield host


def get_random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
