# We recommend to utilize "Ansible" to set up the gateway and nodes.
# Detailed setup instructions can be found in the folder "../ansible_host_setup"

# obtain (if not already present) the "emulation_lib" framework
# e.g.
# cd mkdir ~/emulation
# cd emulation
# git clone https://github.com/theuerse/emulation-lib.git


# make sure, the information in "./example.config.py matches" your setup
#import os
#SSH_USER = "nfd"                            						... user of the testbed nodes
#SSH_PASSWORD = "nfd"												... password of the user
#REMOTE_EMULATION_DIR = "/home/nfd/emulation"						... directory on testbed nodes where emulation files temp. stored
#REMOTE_CONFIG_DIR = os.path.join(REMOTE_EMULATION_DIR,"config")
#REMOTE_RESULT_DIR = os.path.join(REMOTE_EMULATION_DIR,"results")
#REMOTE_DATA_DIR = os.path.join(REMOTE_EMULATION_DIR,"data")
#MIN_START_TIME_OFFSET = 20											
#
#ITEC_GATEWAY = "192.168.0.2"										... the IP address of the gateway/managment server/machine
#MNG_PREFIX = "192.168.0."											... the subnet address of the nodes used for management
#EMU_PREFIX = "192.168.1." 											... the subnet address of the nodes used for the emulation
#MULTICAST_NETWORK = "224.0.0.1/16"
#HOST_IP_START = 10													... begin of IPs in the subnets
#EMU_INTERFACE = "eth0.102"											... interface name of the nodes (connecting to emulation subnet)
#
#PI_CONFIG_HZ = 100
#LATENCY = 100 #queue length of tbf in ms
#HANDLE_OFFSET=11
#LINK_MTU = 1520   # 1500 according to "ip ad | grep mtu", but 1520 actually works
#
# subtracted from artifical introduced (target-) delay to (try to) mask the one-way-delay of the physical connection
#PHYS_LINK_DELAY_COMPENSATION = 0.000200  # seconds with microsecond precision (e.g. 0.000100 for 100 microseconds)



# (temporarily) export path to emulation_lib (only once per terminal session)
(https://stackoverflow.com/questions/24197970/pycharm-import-external-library)
export PYTHONPATH=$PYTHONPATH:~/emulation

# start using the virtual enviroment (only once per terminal session)
source ~/emulation/emu-venv/bin/activate

# start the emulation process
python3 hello_world.py


# alternatively, you can use the shell script start.sh to set up / start the emulation
bash start.sh


# during the runtime of the emulation, follwing directories and artifacts are created
# |- results/HelloWorld/
# |     |- commands/           ... contains the setup- and runtime command file used in the most recent run
# |     |- intermediates/      ... contains the intermediate files used to emulate the link conditions in the most recent run
# |     |- results/            ... contains the actual results of the emulation
# |           |- 192.168.1.10.server.log_0     ... iperf server log (run #0)
# |           |- 192.168.1.10.server.log_1     ... iperf server log (run #1)
# |           |- 192.168.1.11.client.log_0     ... iperf client log (run #0)
# |           |- 192.168.1.11.client.log_1     ... iperf client log (run #1)
# |           |- start_times.txt               ... informational overview of the time points marking the begin of the runs
# |
# |- log.txt                                   ... holds log messages of the most recently started emulation

# the iperf server logs depict the bandwith measured arriving from the client (== sender)