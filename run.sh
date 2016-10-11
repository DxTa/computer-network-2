#!/usr/bin/env bash
trap "set +x; sleep 5; set -x" DEBUG

python bin/run.py -bw 10 -d 10 -l 0 -a cubic
python bin/run.py -bw 10 -d 10 -l 5 -a reno

