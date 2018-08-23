#!/bin/sh
sudo killall cmdScheduler
sudo iptables --flush
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT DROP
sudo iptables -A INPUT -s localhost -d localhost  -j ACCEPT
sudo iptables -A FORWARD -d localhost -s localhost -j ACCEPT
sudo iptables -A OUTPUT -d localhost -s localhost -j ACCEPT
sudo iptables -A INPUT -s 192.168.0.2 -j ACCEPT
sudo iptables -A FORWARD -j ACCEPT
sudo iptables -A OUTPUT -d 192.168.0.2 -j ACCEPT
sudo tc qdisc del dev eth0.102 root
sudo tc qdisc del dev eth0.102 ingress
sudo tc qdisc del dev ifb0 root
sudo tc filter del dev eth0.102 root
sudo tc filter del dev ifb0 root
sudo tc class del eth0.102 root
sudo tc class del ifb0 root
sudo tc qdisc add dev eth0.102 root handle 1: htb default 7
sudo tc class add dev eth0.102 parent 1: classid 1:7 htb rate 100mbit

sudo iptables -A INPUT -d 192.168.1.11 -s 192.168.1.10 -j ACCEPT
sudo iptables -A OUTPUT -d 192.168.1.10 -s 192.168.1.11 -j ACCEPT
sudo tc class add dev eth0.102 parent 1: classid 1:10 htb rate 100mbit
sudo tc filter add dev eth0.102 protocol ip parent 1:0 prio 1 u32 match ip dst 192.168.1.10 match ip src 192.168.1.11 flowid 1:10
sudo tc qdisc add dev eth0.102 parent 1:10 handle 10: tbf rate 24421kbit burst 30527 latency 100ms peakrate 24422kbit mtu 1520
sudo tc qdisc add dev eth0.102 parent 10: handle 100: netem delay 0.1ms loss random 0.0
pkill -KILL iperf
