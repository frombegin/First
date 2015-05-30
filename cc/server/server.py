#!/usr/bin/python
# -*- coding: utf-8 -*-

from twisted.internet import protocol, reactor, endpoints
from twisted.protocols.basic import Int32StringReceiver
import json
import logging
import time
import uuid

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

## sqlite_mem = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('mysql+mysqlconnector://root@localhost/my', echo=True)

metadata = MetaData()
users = Table('users', metadata,
              Column('id', Integer, primary_key=True, doc = u'这是主键!'),
              Column('name', String(32)),
              Column('fullname', String(128)),
              )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String(128), nullable=False))

metadata.drop_all(engine)
print '-' * 80
metadata.create_all(engine)
print '-' * 80
for tab in metadata.sorted_tables:
    print tab
print '-' * 80
for tab in metadata.tables:
    print tab
print '-' * 80

class JsonProtocol(Int32StringReceiver):
    def stringReceived(self, string):
        try:
            d = json.loads(string)
            print d
            # self.send_json({'server-now':time.clock()});
            # self.send_json('hello');
            if isinstance(d, dict):
                if d.has_key('login'):
                    self.send_json(uuid.uuid4().hex)
                    self.send_json({'sid': uuid.uuid4().hex})
        except Exception, e:
            logging.warning('invalid json, %s', e)
            self.connectionLost()

    def send_json(self, d):
        self.sendString(json.dumps(d))


class JsonFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return JsonProtocol()


def run_server(port=1234):
    endpoints.serverFromString(reactor, "tcp:%d" % 1234).listen(JsonFactory())
    reactor.run()


if __name__ == '__main__':
    run_server()
