#!/usr/bin/env bash
trap "set +x; sleep 5; set -x" DEBUG

python bin/run.py -bw 10 -d 10 -l 0 -a reno
python bin/run.py -bw 10 -d 10 -l 0 -a cubic
python bin/run.py -bw 10 -d 10 -l 0 -a vegas

sleep 3 && echo DONE!!
