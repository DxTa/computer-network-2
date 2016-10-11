from subprocess import Popen, PIPE
from time import sleep, time
from argparse import ArgumentParser

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import OVSController

import sys
import os
import signal
import time

parser = ArgumentParser(description="CWND/Queue Monitor")
parser.add_argument('--bandwidth', '-bw',
                    dest="bandwidth",
                    action="store",
                    help="Bandwidth value in Mbit",
                    required=True)
parser.add_argument('--loss', '-l',
                    dest="loss",
                    action="store",
                    help="Loss rate in percentage",
                    required=False)
parser.add_argument('--delay', '-d',
                    dest="delay",
                    action="store",
                    help="delay value in ms",
                    required=True)
parser.add_argument('--algorithm', '-a',
                    dest="algorithm",
                    action="store",
                    help="Type of algorithm",
                    required=True)

# Expt parameters
args = parser.parse_args()

mn = None
tcpprobe = None

class SingleSwitchTopo(Topo):
        "Single switch connected to n hosts."
        def build(self, n=2, bw=10, delay='5ms', loss=0):
            switch = self.addSwitch('s1')
            for h in range(n):
                # Each host gets 50%/n of system CPU
                host = self.addHost('h%s' % (h + 1),
                   cpu=.5/n)
                # 10 Mbps, 5ms delay, 10% loss, 1000 packet queue
                self.addLink(host, switch,
                   bw=bw, delay=delay, loss=loss, max_queue_size=1000, use_htb=True)

def perf_test(bw,delay,loss):
    "Create network and run simple performance test"
    topo = SingleSwitchTopo(n=2,bw=int(bw),delay='%sms' % delay,loss=int(loss))
    net = Mininet(topo=topo,
                    host=CPULimitedHost, link=TCLink, controller=OVSController)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    print "Testing bandwidth between h1 and h4"
    h1, h2 = net.get('h1', 'h2')
    net.iperf((h1, h2), seconds=10)
    net.stop()

def start_tcpprobe(exp):
    global tcpprobe
    #  Popen("rmmod tcp_probe; modprobe tcp_probe full=1", shell=True)
    #  e = Popen("rmmod tcp_probe >/dev/null 2>&1 && modprobe tcp_probe full=1", shell=True)
    print "Monitoring TCP CWND ... will save it to ./outputs/%s_tcpprobe.txt " % exp
    tcpprobe = Popen("cat /proc/net/tcpprobe > ./outputs/%s_tcpprobe.txt" % exp, shell=True, preexec_fn=os.setsid)

#  def start_mininet(bw,delay,loss):
    #  global mn
    #  print "Starting mininet ..."
    #  mn = Popen("mn --link tc,bw=%s,delay=%sms,loss=%s" % (bw, delay, loss), shell=True, preexec_fn=os.setsid)

def run_iperf(bw, delay, algorithm, loss=0):
    global tcpprobe
    start_tcpprobe("%s_%sMbit_%sms_%s" % (algorithm, bw, delay, loss))
    print "Running iperf ..."
    perf_test(bw,delay,loss)
    #  iperfServer = Popen("h1 iperf -s", shell=True, preexec_fn=os.setsid)
    #  iperfClient = Popen("h2 iperf -c h1 -i 1 -Z %s -t 120" % algorithm, shell=True, preexec_fn=os.setsid)
    #  iperfClient.communicate()
    print "iperf running is completed"
    os.kill(os.getpgid(tcpprobe.pid), signal.SIGTERM)
    print "Clear environment!"

if __name__ == '__main__':
    print args
    "Install tcp_pobe module and dump to file"
    print "Enable tcpprobe ..."
    Popen("rmmod tcp_probe >/dev/null 2>&1 && modprobe tcp_probe full=1", shell=True)
    time.sleep(2)
    Popen("sysctl -w net.ipv4.tcp_congestion_control=%s" % args.algorithm, shell=True)
    Popen("sysctl -w net.ipv4.tcp_congestion_control=%s" % args.algorithm, shell=True)
    run_iperf(args.bandwidth, args.delay, args.algorithm, args.loss)
