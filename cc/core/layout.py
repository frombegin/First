#!/usr/bin/python
# -*- coding: utf-8 -*-

from core.block import Block


class Layout(Block):

    def _relayout(self):
        raise NotImplementedError()


class HorizontalLayout(Layout):
    pass


class VerticalLayout(Layout):
    pass


class StackedLayout(Layout):
    pass


class GridLayout(Layout):
    pass
