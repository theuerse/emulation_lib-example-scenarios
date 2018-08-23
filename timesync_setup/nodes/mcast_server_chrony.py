# based on https://pymotw.com/2/socket/multicast.html (big thanks!)
import subprocess
import sys
import socket
import struct
import datetime

BUFFER_SIZE = 4096
MULTICAST_GROUP = '224.0.0.10'
SERVER_ADDRESS = ('', 10000)

"""
Remotely callable methods
"""
def chrony_offset():
    trackin_info = subprocess.check_output(["chronyc", "tracking"])
    access_time = datetime.datetime.now()
    lines = trackin_info.split('\n')
    if len(lines) < 5 or not lines[4].startswith("Last offset"):
        return ""
    else:
        return '{}|{}'.format(access_time, lines[4].split()[3])


"""
UDP-Multicast stuff
"""
# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(SERVER_ADDRESS)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(MULTICAST_GROUP)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
print >>sys.stderr, "mcast", MULTICAST_GROUP, SERVER_ADDRESS[1], 'ready'


# Receive/respond loop
while True:
    request, address = sock.recvfrom(BUFFER_SIZE) # request contains the function to be called
    try:
        response = locals()[request]() # dispatch remote procedure call
    except Exception as e:
        sock.sendto(str(e),address)
    else:
        try:
            sock.sendto(response, address)
        except Exception:
            pass