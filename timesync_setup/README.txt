# https://chrony.tuxfamily.org/

# This time synchronization setup is intended to be used in a Local Area Network
# and with a local time server.

# It is assumed, that the gatway/nodes are Debian based (e.g. Debian or Ubuntu).

# The gateway (192.168.0.1), acting as local time server and the nodes 
# (192.168.0.x, clients of the localtime server) have to have the NTP daemon 
# "chrony" installed.

sudo apt install chrony

# Be sure to get chrony in version 3.1-5 or up (the provided config files are 
# based on this version).

# You may want to remove the possibly preinstalled NTP daemon from the nodes:
sudo apt-get remove ntp

# Create a copy of the default chrony configuration file (server/nodes)
sudo mv /etc/chrony/chrony.conf /etc/chrony/chrony.conf.bak


# Modify the config files to suit your network
# -> See examples below / on the end of the document.


# update / replace the default configuration with the modified configurations
sudo cp gateway/chrony.conf /etc/chrony/chrony.conf     	# on the gateway 
# or sudo cp nodes/chrony.conf /etc/chrony/chrony.conf     	# on the nodes



# on the nodes, you may check the status of the timesync using
chronyc tracking

# example output:
# Reference ID    : C0A80002 (192.168.0.1)
# Stratum         : 11
# Ref time (UTC)  : Tue Aug 14 12:56:24 2018
# System time     : 0.000000522 seconds fast of NTP time
# Last offset     : +0.000001665 seconds
# RMS offset      : 0.000001106 seconds
# Frequency       : 65.088 ppm fast
# Residual freq   : +0.000 ppm
# Skew            : 0.015 ppm
# Root delay      : 0.000104 seconds
# Root dispersion : 0.000041 seconds
# Update interval : 12.2 seconds
# Leap status     : Normal







#
# nodes/chrony.conf
#
# You may want to change "server 192.168.0.1" to fit the IP of your gateway.
# The polling interval is low, allowing for a more accurate time sync.
# The higher polling frequncy is no problem due to the LAN and own timeserver.
 
# Welcome to the chrony configuration file. See chrony.conf(5) for more
# information about usuable directives.
#pool 2.debian.pool.ntp.org iburst
server 192.168.0.1 minpoll 0 maxpoll 2 polltarget 60 maxdelaydevratio 2 xleave

# This directive specify the location of the file containing ID/key pairs for
# NTP authentication.
keyfile /etc/chrony/chrony.keys

# This directive specify the file into which chronyd will store the rate
# information.
driftfile /var/lib/chrony/chrony.drift

# Uncomment the following line to turn logging on.
# log tracking measurements statistics

# Log files location.
logdir /var/log/chrony

# Stop bad estimates upsetting machine clock.
maxupdateskew 100.0

# This directive tells 'chronyd' to parse the 'adjtime' file to find out if the
# real-time clock keeps local time or UTC. It overrides the 'rtconutc' directive.
hwclockfile /etc/adjtime

# This directive enables kernel synchronisation (every 11 minutes) of the
# real-time clock. Note that it can’t be used along with the 'rtcfile' directive.
rtcsync

# Step the system clock instead of slewing it if the adjustment is larger than
# one second, but only in the first three clock updates.
makestep 1 3







#
# gateway/chrony.conf
#
# It is notable here, that we have not defined an external time server and 
# fully rely on the local clock (avoid jumps due to adjustments to external
# time server: "local stratum 10").
# You may want to change "allow 192.168.0/24" to be the subnet interconnecting
# the gateway and the nodes.

# Welcome to the chrony configuration file. See chrony.conf(5) for more
# information about usuable directives.
#pool 2.debian.pool.ntp.org iburst
local stratum 10

# This directive specify the location of the file containing ID/key pairs for
# NTP authentication.
keyfile /etc/chrony/chrony.keys

# This directive specify the file into which chronyd will store the rate
# information.
driftfile /var/lib/chrony/chrony.drift

# Uncomment the following line to turn logging on.
#log tracking measurements statistics

# Log files location.
logdir /var/log/chrony

# Stop bad estimates upsetting machine clock.
maxupdateskew 100.0

# This directive enables kernel synchronisation (every 11 minutes) of the
# real-time clock. Note that it can’t be used along with the 'rtcfile' directive.
rtcsync

# Step the system clock instead of slewing it if the adjustment is larger than
# one second, but only in the first three clock updates.
makestep 1 3

allow 192.168.0/24

