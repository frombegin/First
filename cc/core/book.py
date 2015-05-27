#!/usr/bin/python
# -*- coding: utf-8 -*-


class Book(object):

    def __init__(self):
        super(Book, self).__init__()
        self.__name = u''
        self.__description = u''
        self.__tags = u''
        self.__user_id = None
        self.__creation_time = None
        self.__id = None
        self.__cards = []

    def add_card(self, card):
        pass

    def remove_card(self, card):
        pass

    def clear(self):
        pass

    def load(self, io):
        pass

    def save(self, io):
        pass
