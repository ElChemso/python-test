import unittest
from cyber_python_test.anomalies import create_traffic


class TestAnomalies(unittest.TestCase):

    def test_anomaly_generation(self):
        for host_connection in create_traffic.create_host_traffic_with_anomalies():
            print host_connection

