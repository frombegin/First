#!/usr/bin/python
# -*- coding: utf-8 -*-

class BookItem(object):
    def __init__(self):
        super(BookItem, self).__init__()
        self.__user_id = None
        self.__id = None
        self.__num_of_cards = 0
        self.__title = None
        self.__created_time = None


class BookCollection(object):
    def __init__(self, db):
        super(BookCollection, self).__init__()
        self.__items = []
        self.__db = db
