#!/usr/bin/env bash
trap "set +x; sleep 5; set -x" DEBUG

python bin/run.py -bw 0.01 -d 500 -l 0 -a reno
python bin/run.py -bw 2 -d 500 -l 0 -a reno
python bin/run.py -bw 2 -d 2 -l 5 -a reno
python bin/run.py -bw 0.01 -d 500 -l 0 -a cubic
python bin/run.py -bw 2 -d 500 -l 0 -a cubic
python bin/run.py -bw 2 -d 2 -l 5 -a cubic
python bin/run.py -bw 0.01 -d 500 -l 0 -a vegas
python bin/run.py -bw 2 -d 500 -l 0 -a vegas
python bin/run.py -bw 2 -d 2 -l 5 -a vegas
sleep 3 && echo DONE!!
