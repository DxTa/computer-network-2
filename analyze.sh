#!/usr/bin/env bash
trap "set +x; sleep 5; set -x" DEBUG

python bin/analyze.py -p 5001 -f cubic_0.01Mbit_500ms_0_tcpprobe.txt  -o  cubic_0.01Mbit_500ms_0_tcpprobe.p
python bin/analyze.py -p 5001 -f cubic_2Mbit_2ms_5_tcpprobe.txt       -o  cubic_2Mbit_2ms_5_tcpprobe.png  
python bin/analyze.py -p 5001 -f cubic_2Mbit_500ms_0_tcpprobe.txt     -o  cubic_2Mbit_500ms_0_tcpprobe.png 
python bin/analyze.py -p 5001 -f reno_0.01Mbit_500ms_0_tcpprobe.txt   -o  reno_0.01Mbit_500ms_0_tcpprobe.pn
python bin/analyze.py -p 5001 -f reno_2Mbit_2ms_5_tcpprobe.txt        -o  reno_2Mbit_2ms_5_tcpprobe.png 
python bin/analyze.py -p 5001 -f reno_2Mbit_500ms_0_tcpprobe.txt      -o  reno_2Mbit_500ms_0_tcpprobe.png 
python bin/analyze.py -p 5001 -f vegas_0.01Mbit_500ms_0_tcpprobe.txt  -o  vegas_0.01Mbit_500ms_0_tcpprobe.p
python bin/analyze.py -p 5001 -f vegas_2Mbit_2ms_5_tcpprobe.txt       -o  vegas_2Mbit_2ms_5_tcpprobe.png 
python bin/analyze.py -p 5001 -f vegas_2Mbit_500ms_0_tcpprobe.txt     -o  vegas_2Mbit_500ms_0_tcpprobe.png
