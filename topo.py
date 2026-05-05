from mininet.topo import Topo

class CustomTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        self.addLink(h1, s1, bw=10)
        self.addLink(h2, s3, bw=10)

        # two paths: s1-s2-s3 (longer) and s1-s3 (shorter/direct)
        self.addLink(s1, s2, bw=10)
        self.addLink(s2, s3, bw=10)
        self.addLink(s1, s3, bw=10)

topos = {'mytopo': CustomTopo}