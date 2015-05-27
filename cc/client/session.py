#!/usr/bin/python
# -*- coding: utf-8 -*-


class Session(object):
    def __init__(self):
        super(Session, self).__init__()
        self.__id = None

    def is_anonymous(self):
        return self.__id is None

    def login(self, identify, password):
        pass

    def logout(self):
        pass

    def register(self, identify, password):
        pass

    def get_book_list(self, key, data):
        # key: top, tag, user
        # data: (popular, newest), tag, user_id
        pass

    def get_tag_cloud(self):
        pass

    def search(self, query):
        pass

    def upload(self, book):
        pass

    def download(self, book):
        pass

