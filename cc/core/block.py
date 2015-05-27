#!/usr/bin/python
# -*- coding: utf-8 -*-

from core.geometry import Rectangle
from core.margin import Margin


class Block(object):
    def __init__(self, parent=None):
        super(Block, self).__init__()
        self.__margin = Margin()
        self.__bounds = Rectangle()
        self.__children = []

        assert isinstance(parent, [Block, None])
        if parent:
            parent.add_child(self)
        self.__parent = parent

    def add_child(self, block):
        assert isinstance(block, Block)
        pass

    def remove_child(self, block):
        assert isinstance(block, Block)
        pass

    def __str__(self):
        pass
