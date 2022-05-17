from mininet.topo import Topo

class MyTopo( Topo ):
    "9 host 4 switch - custom topology"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )


        # Add hosts and switches
        h1a = self.addHost('h1')
        h1b = self.addHost('h2')
        h1c = self.addHost('h3')
        s1 = self.addSwitch('s1')

        h2a = self.addHost('h4')
        h2b = self.addHost('h5')
        s2 = self.addSwitch('s2')

        h3a = self.addHost('h6')
        h3b = self.addHost('h7')
        s3 = self.addSwitch('s3')

        h4a = self.addHost('h8')
        h4b = self.addHost('h9')
        s4 = self.addSwitch('s4')


         # Add links
        self.addLink(h1a, s1)
        self.addLink(h1b, s1)
        self.addLink(h1c, s1)

        self.addLink(h2a, s2)
        self.addLink(h2b, s2)

        self.addLink(h3a, s3)
        self.addLink(h3b, s3)

        self.addLink(h4a, s4)
        self.addLink(h4b, s4)

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)

topos = { 'mytopo': ( lambda: MyTopo() ) }
