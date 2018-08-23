Machines:
192.168.0.2  ... gateway
192.168.0.10 ... node #1
192.168.0.11 ... node #2

"nfd" is the user account, which is present on all nodes.

#
# On the gateway:
#

# Create and deploy ssh-key to be able to login to hosts more easily
ssh-keygen # if key does not already exists
ssh-copy-id nfd@192.168.0.10
ssh-copy-id nfd@192.168.0.11

# Install ansible using a ppa (Ubuntu 16.04)
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
ansible --version

# The folder "platform" contains a pre-configured ansible configuration
# which is derived from the one that can be obtained with:
# "cp -R /etc/ansible platform"

# platform/hosts.txt
[nodes]
192.168.0.10 ansible_user=nfd
192.168.0.11 ansible_user=nfd


# You may test the connection using
ansible -m ping nodes
ansible -m shell -a 'hostname' nodes


# Run the playbooks and provide sudo pwds for nodes and gateway as to install necessary software
ansible-playbook -K playbook_gateway.yml
ansible-playbook -K playbook_nodes.yml

# Many of the example-scenarios depend on udperf-applications to be installed on the nodes (a custom traffic generator
# akin to iperf), if you wish to execute these, please issue:
ansible-playbook -K playbook_nodes_plus_udperf.yml

------------------------------------------------------------------------------------------------------------------

# The emulation_lib on the gateway needs some python3 libraries which can be easily set up using a virtual environment.
# On the gateway:

python3 -m venv ~/emulation/emu-venv

source ~/emulation/emu-venv/bin/activate

pip install wheel
pip install paramiko
pip install python-igraph


# before starting emulations, this virtual environment must be activated first (setting shell environment vars) using:
source ~/emulation/emu-venv/bin/activate

# e.g.
source ~/emulation/emu-venv/bin/activate
export PYTHONPATH=$PYTHONPATH:~/emulation
cd ../hello-world
python3 hello_world.py

------------------------------------------------------------------------------------------------------------------

# Additionally, some changes to the /etc/sudoers file on the nodes is necessary
# in order to be able to call following commands without providing the appropriate sudo password for the user "nfd"
# (Users of the OS raspbian usually do not have to do this, as raspbian runs all programs requesting elevated privileges
# as such without asking for passwords.)


# We strongly advise to use the application visudo to perform the changes instead of a normal editor
sudo visudo

# Minimal line allowing necessary operations to be performed without entering the sudo password:
nfd ALL=(ALL) NOPASSWD: /sbin/tc, /usr/bin/chrt, /sbin/iptables, /usr/bin/killall


------------------------------------------------------------------------------------------------------------------


# You may test the basic operational capability of the cmdScheduler by logging in on any node and performing
cd ~/emulation/emulation-cmdscheduler
cmdScheduler examples/example.cmd


------------------------------------------------------------------------------------------------------------------


# You may perform a preliminary test of the installation by executing "test.sh" and "test_ifb.sh" on one of the nodes.
# Copy file to a node:
scp test.sh test_ifb.sh nfd@192.168.0.10:~/emulation/

# on the node:
cd emulation

sh test.sh

# Example output (positive):
# RTNETLINK answers: No such file or directory
# SETUP COMPLETE
# cleaning up ...
# pid 3856's current scheduling policy: SCHED_OTHER
# pid 3856's current scheduling priority: 0
# CLEANUP COMPLETE


------------------------------------------------------------------------------------------------------------------


# If you intend to use link cmd backends which utilize the IFB,
# you have to ensure that at least one IFB-device (ifb0)
# is loaded / usable before starting the emulations.
# To check if the IFB module can be loaded, try to run test_ifb.sh with sudo.

sudo sh test_ifb.sh

# Acceptable outputs are:
# 1: (ifb module is available and could be loaded)
# <IFB module>
# ifb                    ...
# </IFB module>
# ...

# 2: (in case ifb is built/loaded as part of the kernel)
# modprobe: FATAL: Module ifb is builtin.


# At least ifb0 should show up in
<network interfaces>
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether b8:27:eb:db:8a:52 brd ff:ff:ff:ff:ff:ff
3: ifb0: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN mode DEFAULT group default qlen 32
    link/ether 5e:0d:23:1a:f2:c0 brd ff:ff:ff:ff:ff:ff
4: ifb1: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN mode DEFAULT group default qlen 32
    link/ether 76:ba:3d:e4:e5:ed brd ff:ff:ff:ff:ff:ff
</network interfaces>


------------------------------------------------------------------------------------------------------------------


# In order to work properly, the clocks of the nodes have to be syncronized with the gateway.
# A set of instructions to set this up as we did, can be found in "emulation_lib-example-scenarios/timesync_setup"-


------------------------------------------------------------------------------------------------------------------


# Completing this setup should allow to run the "hello-world" example, more complex scenarios may still require
# installation of packages/software on the gateway/nodes.