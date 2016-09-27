import sys

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import lg, setLogLevel, info
from mininet.link import TCLink
from mininet.node import Node
from mininet.util import waitListening

def buildNet():
    net = Mininet()
    net.addController( 'c0' )
    h1 = net.addHost( 'h1' )
    h2 = net.addHost( 'h2' )
    s1 = net.addSwitch( 's1' )
    link1 = net.addLink( h1, s1, cls=TCLink )
    link2 = net.addLink( h2, s1, cls=TCLink )
    return net, link1, link2

def netTest(network):

    # flush out latency from reactive forwarding delay
    net.pingAll()

    info( '\n*** Configuring one intf with bandwidth of 100 Mb\n' )
    link1.intf1.config( bw=100 )
    info( '\n*** Running iperf to test\n' )
    net.iperf()

    info( '\n*** Configuring one intf with delay of 1ms\n' )
    link1.intf1.config( delay='1ms' )
    info( '\n*** Run a ping to confirm delay\n' )
    net.pingPairFull()

    info( '\n*** Done testing\n' )
    net.stop()

def connectToRootNS( network, switch, ip, routes ):
    root = Node('root', inNamespace=False)
    intf = network.addLink( root, switch ).intf1
    root.setIP( ip, intf=intf )
    network.start()
    for route in routes:
        root.cmd( 'route add -net ' + route + ' dev ' + str( intf ) )

def sshd( network, cmd='/usr/sbin/sshd', opts='-D',
          ip='10.123.123.1/32', routes=None, switch=None ):
    """Start a network, connect it to root ns, and run sshd on all hosts.
       ip: root-eth0 IP address in root namespace (10.123.123.1/32)
       routes: Mininet host networks to route to (10.0/24)
       switch: Mininet switch to connect to root namespace (s1)"""
    if not switch:
        switch = network[ 's1' ]  # switch to use
    if not routes:
        routes = [ '10.0.0.0/24' ]
    connectToRootNS( network, switch, ip, routes )
    for host in network.hosts:
        host.cmd( cmd + ' ' + opts + '&' )
    info( "*** Waiting for ssh daemons to start\n" )
    for server in network.hosts:
        waitListening( server=server, port=22, timeout=5 )

    info( "\n*** Hosts are running sshd at the following addresses:\n" )
    for host in network.hosts:
        info( host.name, host.IP(), '\n' )
    """info( "\n*** Type 'exit' or control-D to shut down network\n" )
    CLI( network )
    for host in network.hosts:
        host.cmd( 'kill %' + cmd )"""

if __name__ == '__main__':
    setLogLevel( 'info' )
    net, link1, link2 = buildNet()
    argvopts = ' '.join( sys.argv[ 1: ] ) if len( sys.argv ) > 1 else (
        '-D -o UseDNS=no -u0' )
    sshd( net, opts=argvopts )
    netTest(net)
