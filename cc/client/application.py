#!/usr/bin/python
# -*- coding: utf-8 -*-
from client.session import Session


class Application(object):
    program = u''

    def __init__(self):
        super(Application, self).__init__()
        self.__session = Session()

    def run(self):
        pass
