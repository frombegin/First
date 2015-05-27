#!/usr/bin/python
# -*- coding: utf-8 -*-


class Margin(object):
    def __init__(self):
        super(Margin, self).__init__()
        self.__left = 0
        self.__right = 0
        self.__top = 0
        self.__bottom = 0

    def __str__(self):
        return 'L: %d, T: %d, R: %d, B: %d' % (self.__left, self.__top, self.__right, self.__bottom)
