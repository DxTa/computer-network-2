#!/usr/bin/env bash
trap "set +x; sleep 5; set -x" DEBUG

python bin/analyze.py -p 5001 -f outputs/cubic_0.01Mbit_2ms_0_tcpprobe.txt  -o  plots/cubic_0.01Mbit_2ms_0_tcpprobe.png
python bin/analyze.py -p 5001 -f outputs/cubic_2Mbit_500ms_5_tcpprobe.txt       -o  plots/cubic_2Mbit_500ms_5_tcpprobe.png
python bin/analyze.py -p 5001 -f outputs/cubic_2Mbit_2ms_0_tcpprobe.txt     -o  plots/cubic_2Mbit_2ms_0_tcpprobe.png
python bin/analyze.py -p 5001 -f outputs/reno_0.01Mbit_2ms_0_tcpprobe.txt   -o  plots/reno_0.01Mbit_2ms_0_tcpprobe.png
python bin/analyze.py -p 5001 -f outputs/reno_2Mbit_500ms_5_tcpprobe.txt        -o  plots/reno_2Mbit_500ms_5_tcpprobe.png
python bin/analyze.py -p 5001 -f outputs/reno_2Mbit_2ms_0_tcpprobe.txt      -o  plots/reno_2Mbit_2ms_0_tcpprobe.png
python bin/analyze.py -p 5001 -f outputs/vegas_0.01Mbit_2ms_0_tcpprobe.txt  -o  plots/vegas_0.01Mbit_2ms_0_tcpprobe.png
python bin/analyze.py -p 5001 -f outputs/vegas_2Mbit_500ms_5_tcpprobe.txt       -o  plots/vegas_2Mbit_500ms_5_tcpprobe.png
python bin/analyze.py -p 5001 -f outputs/vegas_2Mbit_2ms_0_tcpprobe.txt     -o  plots/vegas_2Mbit_2ms_0_tcpprobe.png
