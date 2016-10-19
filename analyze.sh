#!/usr/bin/env bash
trap "set +x; sleep 5; set -x" DEBUG

python bin/analyze.py
