#!/bin/sh
# Avoid calling this script with "sudo sh ..." or entering the sudo pwd.
# Having set up /etc/sudoers correctly (visudo), everyhting should work
# just fine without entering the sudo password

# please modify according to the actual situation
GATEWAY=192.168.0.2
OWN_IP=192.168.0.4
EMU_INTERFACE=eth0.102

sudo iptables --flush
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT DROP
sudo iptables -A INPUT -s localhost -d localhost  -j ACCEPT
sudo iptables -A FORWARD -d localhost -s localhost -j ACCEPT
sudo iptables -A OUTPUT -d localhost -s localhost -j ACCEPT
sudo iptables -A INPUT -s $GATEWAY -j ACCEPT
sudo iptables -A FORWARD -j ACCEPT
sudo iptables -A OUTPUT -d $GATEWAY -j ACCEPT
sudo tc qdisc del dev $EMU_INTERFACE root
sudo tc qdisc add dev $EMU_INTERFACE root handle 1: htb default 7
sudo tc class add dev $EMU_INTERFACE parent 1: classid 1:7 htb rate 100mbit

sudo tc class add dev $EMU_INTERFACE parent 1: classid 1:11 htb rate 100mbit
sudo tc filter add dev $EMU_INTERFACE protocol ip parent 1:0 prio 1 u32 match ip dst $GATEWAY match ip src $OWN_IP flowid 1:11
sudo tc qdisc add dev $EMU_INTERFACE parent 1:11 handle 11: tbf rate 12149kbit burst 15187 latency 100ms peakrate 12150kbit mtu 1520
sudo tc qdisc add dev $EMU_INTERFACE parent 11: handle 110: netem delay 10ms loss random 10.0
pkill -KILL iperf
(sudo chrt -o -p 0 $BASHPID && iperf -s -i 1 -u > ~/emulation/iperf_test.log 2>&1 &)


echo "SETUP COMPLETE"
#echo "<iptables>"
#sudo iptables --list
#echo "</iptables>"
#echo "<tc>"
#sudo tc qdisc show
#echo "</tc>"
echo "cleaning up ..."


# cleanup
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables --flush
sudo tc qdisc del dev $EMU_INTERFACE root

pkill -KILL iperf


echo "CLEANUP COMPLETE"
#echo "<iptables>"
#sudo iptables --list
#echo "</iptables>"
#echo "<tc>"
#sudo tc qdisc show
#echo "</tc>"

