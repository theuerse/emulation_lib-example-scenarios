import os
SSH_USER = "nfd"
SSH_PASSWORD = "nfd"
REMOTE_EMULATION_DIR = "/home/nfd/emulation"
REMOTE_CONFIG_DIR = os.path.join(REMOTE_EMULATION_DIR,"config")
REMOTE_RESULT_DIR = os.path.join(REMOTE_EMULATION_DIR,"results")
REMOTE_DATA_DIR = os.path.join(REMOTE_EMULATION_DIR,"data")
MIN_START_TIME_OFFSET = 20

GATEWAY_SERVER = "192.168.0.4"
MNG_PREFIX = "192.168.0."
EMU_PREFIX = "192.168.1."
MULTICAST_NETWORK = "224.0.0.1/16"
HOST_IP_START = 10
EMU_INTERFACE = "eth0.102"

PI_CONFIG_HZ = 100
LATENCY = 100 #queue length of tbf in ms
HANDLE_OFFSET=11
LINK_MTU = 1520   # 1500 according to "ip ad | grep mtu", but 1520 actually works

# subtracted from artifical introduced (target-) delay to (try to) mask the one-way-delay of the physical connection
PHYS_LINK_DELAY_COMPENSATION = 0.000150  # seconds with microsecond precision (e.g. 0.000100 for 100 microseconds)