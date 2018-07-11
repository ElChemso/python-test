
class HostConnection(object):

    def __init__(self, ip, destination_ip, date, destination_port, connection_duration_ms, orig_bytes, resp_bytes):
        self.host_ip = ip
        self.destination_ip = destination_ip
        self.destination_port = destination_port
        self.date = date
        self.connection_duration_ms = connection_duration_ms
        self.orig_bytes = orig_bytes
        self.resp_bytes = resp_bytes

    def __str__(self):
        return "Host IP: {} \n" \
               "Destination IP: {} \n" \
               "Destination Port: {} \n" \
               "Date: {} \n" \
               "Connection Duration ms: {} \n" \
               "Orig Bytes: {} \n" \
               "Resp Bytes: {} \n".format(self.host_ip,
                                          self.destination_ip,
                                          self.destination_port,
                                          self.date,
                                          self.connection_duration_ms,
                                          self.orig_bytes,
                                          self.resp_bytes)
