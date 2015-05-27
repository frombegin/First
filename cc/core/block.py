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
        assert isinstance(parent, (Block, None))
        if parent:
            parent.add_child(self)
        self.__parent = parent

    def _accept(self, block):
        assert isinstance(block, Block)
        return False

    def _changed(self):
        pass

    def add_child(self, block):
        if self._accept(block):
            self.__children.append(block)
            self._changed()

    def remove_child(self, block):
        assert isinstance(block, Block)
        self.__children.remove(block)

    @property
    def parent(self):
        return self.__parent

    @property
    def level(self):
        result = 0
        p = self.__parent
        while p:
            p = p.__parent
            result += 1
        return result

    @property
    def bounds(self):
        return self.__bounds

    @property
    def margin(self):
        return self.__margin

    def __str__(self):
        pass
