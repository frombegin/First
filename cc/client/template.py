#!/usr/bin/python
# -*- coding: utf-8 -*-
from core.card import Card


class Template(object):
    def __init__(self):
        super(Template, self).__init__()
        self.__description = u''
        self.__card = Card()
        self.__tags = u''