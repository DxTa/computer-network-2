#!/usr/bin/env bash
trap "set +x; sleep 2; set -x" DEBUG

rm -rf /usr/local/bin/mn /usr/local/bin/mnexec /usr/local/lib/python*/*/*mininet* /usr/local/bin/ovs-* /usr/local/sbin/ovs-*
apt-get install -y python-setuptools
sudo easy_install pip
apt-get install -y openvswitch-testcontroller && cp /usr/bin/ovs-testcontroller /usr/bin/ovs-controller
modprobe tcp_vegas
modprobe tcp_probe full=1
