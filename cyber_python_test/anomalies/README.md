### Python Anomalies Test

This test provides a single method `create_host_traffic_with_anomalies` which returns host objects that contain 
connection information for outbound connections. An example of this information:

```
Host IP: 3.153.35.169 
Destination IP: 180.187.75.208 
Destination Port: 3307 
Date: 2018-07-04 23:49:46.235671 
Connection Duration ms: 106 
Orig Bytes: 850 
Resp Bytes: 366104 
```

In this data a single result will contain an anomaly where the connection duration, orig bytes or resp bytes is much larger than 
all other results. 

The objective is to identify the which piece of host traffic contains an anomaly. 
