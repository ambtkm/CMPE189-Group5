#!/usr/bin/env python3
"""Run all test plan steps: ping, iperf, flow dump."""

import os
import time
from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.link import TCLink
from mininet.log import setLogLevel, info
from topo import CustomTopo

def run():
    setLogLevel('info')

    net = Mininet(
        topo=CustomTopo(),
        controller=RemoteController('c0', ip='127.0.0.1', port=6633),
        switch=OVSKernelSwitch,
        link=TCLink,
        autoSetMacs=True
    )
    net.start()

    info('\n=== Waiting for controller to discover topology ===\n')
    time.sleep(3)

    # Test 1: ping
    info('\n=== Test 1: Ping All ===\n')
    result = net.pingAll()
    info(f'Packet loss: {result}%\n')

    time.sleep(1)

    # Test 2: iperf
    info('\n=== Test 2: iPerf Throughput (h1 -> h2) ===\n')
    h1, h2 = net.get('h1', 'h2')
    net.iperf([h1, h2], seconds=5)

    # Test 3: flow rules
    info('\n=== Test 3: Flow Rules Per Switch ===\n')
    for sw in ['s1', 's2', 's3']:
        info(f'\n--- {sw} ---\n')
        os.system(f'ovs-ofctl dump-flows {sw}')

    # Test 4: traceroute to confirm path
    info('\n=== Test 4: Path Verification (traceroute h1 -> h2) ===\n')
    h1.cmdPrint('traceroute -n 10.0.0.2')

    net.stop()

if __name__ == '__main__':
    run()
