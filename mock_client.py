#!/usr/bin/python
# -*- coding: utf-8 -*-

from twisted.internet import protocol, reactor, endpoints
from twisted.protocols.basic import Int32StringReceiver
import json
import logging
import time

# a client protocol
class JsonClient(Int32StringReceiver):
    """Once connected, send a message, then print the result."""

    def connectionMade(self):

        self.send_json({'login': time.clock()})

    def stringReceived(self, string):
        try:
            d = json.loads(string)
            print d, type(d)
            self.send_json({'login': time.clock()})
        except:
            logging.warning('invalid json')
            self.connectionLost()

    def send_json(self, d):
        self.sendString(json.dumps(d))


class JsonFactory(protocol.ClientFactory):
    protocol = JsonClient

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        reactor.stop()


# this connects the protocol to a server runing on port 8000
def main():
    f = JsonFactory()
    reactor.connectTCP("localhost", 1234, f)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
