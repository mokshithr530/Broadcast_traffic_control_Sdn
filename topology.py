from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel


class AdvancedBroadcastTopo(Topo):
    def build(self):
        # Core switch
        s1 = self.addSwitch('s1')

        # Aggregation switches
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Connect aggregation to core
        self.addLink(s1, s2)
        self.addLink(s1, s3)

        # Hosts under s2
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        # Hosts under s3
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')

        # Connect hosts to aggregation switches
        for h in [h1, h2, h3]:
            self.addLink(h, s2)

        for h in [h4, h5, h6]:
            self.addLink(h, s3)


def run():
    topo = AdvancedBroadcastTopo()

    net = Mininet(
        topo=topo,
        controller=RemoteController,
        autoSetMacs=True
    )

    net.start()
    print("topology started")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()