# Traffic Engineering in SDN Using Dynamic Path Selection

Implements dynamic path selection in SDN using Ryu and Mininet. The controller monitors topology and routes flows along the shortest path, adapting to the network graph automatically.

## Topology

```
h1 -- s1 -- s2 -- s3 -- h2
       \          /
        \________/
         (direct)
```

Three switches with two paths between h1 and h2. The controller picks the shortest (s1 → s3 direct).

## Requirements

- Python 3
- [Mininet](http://mininet.org/)
- [Ryu SDN Framework](https://ryu.readthedocs.io/)
- NetworkX (`pip install networkx`)
- iPerf (`sudo apt install iperf`)

## Files

| File | Description |
|------|-------------|
| `topo.py` | Mininet topology (3 switches, 2 hosts, 2 paths) |
| `dynamic_routing.py` | Ryu controller with shortest-path forwarding |
| `run_tests.py` | Automated test runner (ping, iperf, flow dump, traceroute) |

## How to Run

**Terminal 1 — start the Ryu controller:**
```bash
ryu-manager dynamic_routing.py --observe-links
```

**Terminal 2 — run all tests:**
```bash
sudo python3 run_tests.py
```

The test script runs:
1. **Ping all** — verifies connectivity between all hosts
2. **iPerf** — measures throughput from h1 to h2 (5 seconds)
3. **Flow dump** — prints installed flow rules on each switch
4. **Traceroute** — confirms packets follow the shortest path

## Manual Mininet (optional)

```bash
sudo mn --custom topo.py --topo mytopo --controller remote --link tc --mac
```

Then inside the Mininet CLI:
```
mininet> pingall
mininet> iperf h1 h2
mininet> sh ovs-ofctl dump-flows s1
mininet> sh ovs-ofctl dump-flows s2
mininet> sh ovs-ofctl dump-flows s3
```
