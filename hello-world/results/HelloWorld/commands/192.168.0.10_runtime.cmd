0.0	echo emulation-start &
1.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 10738kbit burst 13423 latency 100ms peakrate 10739kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.2ms loss random 0.0\n" | sudo tc -batch -
2.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 12235kbit burst 15294 latency 100ms peakrate 12236kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.3ms loss random 0.0\n" | sudo tc -batch -
3.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 12149kbit burst 15187 latency 100ms peakrate 12150kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.3ms loss random 0.0\n" | sudo tc -batch -
4.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 12014kbit burst 15018 latency 100ms peakrate 12015kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.3ms loss random 0.0\n" | sudo tc -batch -
5.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 11388kbit burst 14235 latency 100ms peakrate 11389kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.4ms loss random 0.0\n" | sudo tc -batch -
6.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 9830kbit burst 12288 latency 100ms peakrate 9831kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.6ms loss random 0.0\n" | sudo tc -batch -
7.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 9143kbit burst 11429 latency 100ms peakrate 9144kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.6ms loss random 0.0\n" | sudo tc -batch -
8.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 8639kbit burst 10799 latency 100ms peakrate 8640kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.8ms loss random 0.0\n" | sudo tc -batch -
9.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 8014kbit burst 10018 latency 100ms peakrate 8015kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.9ms loss random 0.0\n" | sudo tc -batch -
10.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 7240kbit burst 9050 latency 100ms peakrate 7241kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 1.1ms loss random 0.0\n" | sudo tc -batch -
11.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 4774kbit burst 5968 latency 100ms peakrate 4775kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 1.7ms loss random 0.0\n" | sudo tc -batch -
12.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 4872kbit burst 6090 latency 100ms peakrate 4873kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 1.8ms loss random 0.25\n" | sudo tc -batch -
13.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 3264kbit burst 4080 latency 100ms peakrate 3265kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 2.5ms loss random 1.48\n" | sudo tc -batch -
14.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 3252kbit burst 4065 latency 100ms peakrate 3253kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 2.1ms loss random 2.58\n" | sudo tc -batch -
15.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 2393kbit burst 2992 latency 100ms peakrate 2394kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 2.4ms loss random 4.39\n" | sudo tc -batch -
16.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 2099kbit burst 2624 latency 100ms peakrate 2100kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 3.2ms loss random 5.52\n" | sudo tc -batch -
17.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 1448kbit burst 1810 latency 100ms peakrate 1449kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 4.4ms loss random 9.92\n" | sudo tc -batch -
18.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 1104kbit burst 1520 latency 100ms peakrate 1105kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 4.9ms loss random 12.75\n" | sudo tc -batch -
19.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 785kbit burst 1520 latency 100ms peakrate 786kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 8.1ms loss random 17.72\n" | sudo tc -batch -
20.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 638kbit burst 1520 latency 100ms peakrate 639kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 5.0ms loss random 30.67\n" | sudo tc -batch -
21.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 430kbit burst 1520 latency 100ms peakrate 431kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 5.0ms loss random 40.68\n" | sudo tc -batch -
22.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 503kbit burst 1520 latency 100ms peakrate 504kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 6.2ms loss random 36.51\n" | sudo tc -batch -
23.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 270kbit burst 1520 latency 100ms peakrate 271kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 6.9ms loss random 55.1\n" | sudo tc -batch -
24.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 196kbit burst 1520 latency 100ms peakrate 197kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 5.7ms loss random 62.79\n" | sudo tc -batch -
25.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 184kbit burst 1520 latency 100ms peakrate 185kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 14.1ms loss random 63.41\n" | sudo tc -batch -
26.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 209kbit burst 1520 latency 100ms peakrate 210kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 7.8ms loss random 64.58\n" | sudo tc -batch -
27.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 184kbit burst 1520 latency 100ms peakrate 185kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 6.3ms loss random 60.98\n" | sudo tc -batch -
28.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 196kbit burst 1520 latency 100ms peakrate 197kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 7.9ms loss random 65.91\n" | sudo tc -batch -
29.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 147kbit burst 1520 latency 100ms peakrate 148kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 11.1ms loss random 69.23\n" | sudo tc -batch -
30.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 184kbit burst 1520 latency 100ms peakrate 185kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 4.9ms loss random 69.39\n" | sudo tc -batch -
31.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 110kbit burst 1520 latency 100ms peakrate 111kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 5.8ms loss random 76.32\n" | sudo tc -batch -
32.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 86kbit burst 1520 latency 100ms peakrate 87kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 5.4ms loss random 82.5\n" | sudo tc -batch -
33.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 98kbit burst 1520 latency 100ms peakrate 99kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 6.8ms loss random 78.38\n" | sudo tc -batch -
34.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 49kbit burst 1520 latency 100ms peakrate 50kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 19.5ms loss random 88.57\n" | sudo tc -batch -
35.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 37kbit burst 1520 latency 100ms peakrate 38kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 17.4ms loss random 91.43\n" | sudo tc -batch -
36.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 25kbit burst 1520 latency 100ms peakrate 26kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 13.5ms loss random 94.12\n" | sudo tc -batch -
37.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 37kbit burst 1520 latency 100ms peakrate 38kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 8.1ms loss random 91.67\n" | sudo tc -batch -
38.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 25kbit burst 1520 latency 100ms peakrate 26kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 3.3ms loss random 94.12\n" | sudo tc -batch -
39.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 12kbit burst 1520 latency 100ms peakrate 13kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 28.9ms loss random 97.3\n" | sudo tc -batch -
40.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 12kbit burst 1520 latency 100ms peakrate 13kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 11.6ms loss random 97.06\n" | sudo tc -batch -
41.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 12kbit burst 1520 latency 100ms peakrate 13kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 6.3ms loss random 97.14\n" | sudo tc -batch -
42.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 37kbit burst 1520 latency 100ms peakrate 38kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 13.9ms loss random 90.91\n" | sudo tc -batch -
43.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 25kbit burst 1520 latency 100ms peakrate 26kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 1.8ms loss random 94.12\n" | sudo tc -batch -
44.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 0kbit burst 1520 latency 100ms peakrate 1kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0ms loss random 100.0\n" | sudo tc -batch -
48.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 25kbit burst 1520 latency 100ms peakrate 26kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 19.1ms loss random 94.12\n" | sudo tc -batch -
49.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 12kbit burst 1520 latency 100ms peakrate 13kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.1ms loss random 97.22\n" | sudo tc -batch -
50.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 0kbit burst 1520 latency 100ms peakrate 1kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0ms loss random 100.0\n" | sudo tc -batch -
55.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 25kbit burst 1520 latency 100ms peakrate 26kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 2.0ms loss random 94.59\n" | sudo tc -batch -
56.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 12kbit burst 1520 latency 100ms peakrate 13kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 3.5ms loss random 97.06\n" | sudo tc -batch -
57.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 0kbit burst 1520 latency 100ms peakrate 1kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0ms loss random 100.0\n" | sudo tc -batch -
58.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 61kbit burst 1520 latency 100ms peakrate 62kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 6.1ms loss random 86.49\n" | sudo tc -batch -
59.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 12kbit burst 1520 latency 100ms peakrate 13kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 14.4ms loss random 97.22\n" | sudo tc -batch -
60.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 25kbit burst 1520 latency 100ms peakrate 26kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 2.7ms loss random 94.29\n" | sudo tc -batch -
61.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 61kbit burst 1520 latency 100ms peakrate 62kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 13.1ms loss random 85.71\n" | sudo tc -batch -
62.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 25kbit burst 1520 latency 100ms peakrate 26kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 4.2ms loss random 90.91\n" | sudo tc -batch -
63.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 74kbit burst 1520 latency 100ms peakrate 75kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 12.3ms loss random 86.49\n" | sudo tc -batch -
64.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 61kbit burst 1520 latency 100ms peakrate 62kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 12.2ms loss random 87.5\n" | sudo tc -batch -
65.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 86kbit burst 1520 latency 100ms peakrate 87kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 10.6ms loss random 79.41\n" | sudo tc -batch -
66.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 98kbit burst 1520 latency 100ms peakrate 99kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 5.6ms loss random 78.38\n" | sudo tc -batch -
67.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 123kbit burst 1520 latency 100ms peakrate 124kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 6.1ms loss random 75.0\n" | sudo tc -batch -
68.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 209kbit burst 1520 latency 100ms peakrate 210kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 6.6ms loss random 58.54\n" | sudo tc -batch -
69.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 221kbit burst 1520 latency 100ms peakrate 222kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 12.9ms loss random 55.0\n" | sudo tc -batch -
70.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 245kbit burst 1520 latency 100ms peakrate 246kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 8.3ms loss random 54.55\n" | sudo tc -batch -
71.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 172kbit burst 1520 latency 100ms peakrate 173kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 8.6ms loss random 68.18\n" | sudo tc -batch -
72.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 160kbit burst 1520 latency 100ms peakrate 161kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 8.5ms loss random 69.77\n" | sudo tc -batch -
73.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 233kbit burst 1520 latency 100ms peakrate 234kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 8.1ms loss random 57.78\n" | sudo tc -batch -
74.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 221kbit burst 1520 latency 100ms peakrate 222kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 7.7ms loss random 60.0\n" | sudo tc -batch -
75.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 515kbit burst 1520 latency 100ms peakrate 516kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 5.6ms loss random 37.31\n" | sudo tc -batch -
76.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 503kbit burst 1520 latency 100ms peakrate 504kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 6.9ms loss random 31.15\n" | sudo tc -batch -
77.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 724kbit burst 1520 latency 100ms peakrate 725kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 5.6ms loss random 25.64\n" | sudo tc -batch -
78.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 1129kbit burst 1520 latency 100ms peakrate 1130kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 4.3ms loss random 14.02\n" | sudo tc -batch -
79.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 1043kbit burst 1520 latency 100ms peakrate 1044kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 5.2ms loss random 12.37\n" | sudo tc -batch -
80.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 1154kbit burst 1520 latency 100ms peakrate 1155kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 5.4ms loss random 10.48\n" | sudo tc -batch -
81.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 1509kbit burst 1887 latency 100ms peakrate 1510kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 3.9ms loss random 9.49\n" | sudo tc -batch -
82.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 2479kbit burst 3099 latency 100ms peakrate 2480kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 4.0ms loss random 1.94\n" | sudo tc -batch -
83.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 3080kbit burst 3850 latency 100ms peakrate 3081kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 2.4ms loss random 2.33\n" | sudo tc -batch -
84.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 3694kbit burst 4618 latency 100ms peakrate 3695kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 2.5ms loss random 0.66\n" | sudo tc -batch -
85.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 4393kbit burst 5492 latency 100ms peakrate 4394kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 2.1ms loss random 0.28\n" | sudo tc -batch -
86.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 5621kbit burst 7027 latency 100ms peakrate 5622kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 1.5ms loss random 0.22\n" | sudo tc -batch -
87.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 7560kbit burst 9450 latency 100ms peakrate 7561kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 1.0ms loss random 0.0\n" | sudo tc -batch -
88.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 7118kbit burst 8898 latency 100ms peakrate 7119kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 1.1ms loss random 0.0\n" | sudo tc -batch -
89.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 7830kbit burst 9788 latency 100ms peakrate 7831kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.9ms loss random 0.0\n" | sudo tc -batch -
90.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 9364kbit burst 11705 latency 100ms peakrate 9365kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.6ms loss random 0.0\n" | sudo tc -batch -
91.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 9719kbit burst 12149 latency 100ms peakrate 9720kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.5ms loss random 0.0\n" | sudo tc -batch -
92.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 11352kbit burst 14190 latency 100ms peakrate 11353kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.4ms loss random 0.0\n" | sudo tc -batch -
93.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 12063kbit burst 15079 latency 100ms peakrate 12064kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.3ms loss random 0.0\n" | sudo tc -batch -
94.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 11904kbit burst 14880 latency 100ms peakrate 11905kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.3ms loss random 0.0\n" | sudo tc -batch -
95.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 12382kbit burst 15478 latency 100ms peakrate 12383kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.2ms loss random 0.0\n" | sudo tc -batch -
96.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 12812kbit burst 16015 latency 100ms peakrate 12813kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.2ms loss random 0.0\n" | sudo tc -batch -
97.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 13094kbit burst 16368 latency 100ms peakrate 13095kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.2ms loss random 0.0\n" | sudo tc -batch -
98.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 13106kbit burst 16383 latency 100ms peakrate 13107kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.2ms loss random 0.0\n" | sudo tc -batch -
99.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 0kbit burst 1520 latency 100ms peakrate 1kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0ms loss random 0.0\n" | sudo tc -batch -
100.0	printf "qdisc change dev eth0.102 parent 1:11 handle 11: tbf rate 10738kbit burst 13423 latency 100ms peakrate 10739kbit mtu 1520\nqdisc change dev eth0.102 parent 11: handle 110: netem delay 0.2ms loss random 0.0\n" | sudo tc -batch - & pkill -KILL iperf & echo emulation-end &
