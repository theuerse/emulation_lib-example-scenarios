import socket
import struct
import sys
import time
import logging
from logging.handlers import TimedRotatingFileHandler

BUFFER_SIZE = 4096
REQUEST = "chrony_offset"
MULTICAST_GROUP = ('224.0.0.10', 10000)
INTERVAL = 1 # fractional seconds

def create_time_rotating_log(path):
    logger = logging.getLogger(path)
    logger.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(path, when="h", interval=48, backupCount=0)
    logger.addHandler(handler)
    return logger

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.2) # should be smaller than INTERVAL

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
loggers = {}

try:
    while True:
        start_time = time.time()

        # Send data to the multicast group
        sent = sock.sendto(REQUEST, MULTICAST_GROUP)

        # Look for responses from all recipients
        while True:
            # waiting to receive
            try:
                data, server = sock.recvfrom(BUFFER_SIZE)
            except socket.timeout:
                # timed out, no more responses
                break
            else:
                print "{}: {}".format(server[0], data)
                if server[0] not in loggers:
                    loggers[server[0]] = create_time_rotating_log("./" + server[0] + ".timing")
                loggers[server[0]].info(data.replace("|"," "))

        time.sleep(INTERVAL - (time.time() - start_time)) # try and correct for elapsed timeout-time

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
