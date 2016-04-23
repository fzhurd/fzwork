#! /usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from config_plug_v2 import *

# class ConfigurableWidget(object):
#     cfg = None
#     def can_frobnicate(self):
#         return self.cfg.get('can_frobnicate', True)
        

#     def likes_cheese(self):
#         return self.cfg.get('likes_cheese', True)

class TestConfigurableWidget(unittest.TestCase):
    longMessage = False
    def setUp(self):
        self.widget = ConfigurableWidget()

    def test_can_frobnicate(self):
        self.widget.can_frobnicate()

    def test_likes_cheese(self):
        self.widget.likes_cheese()

    def shortDescription(self):
        try:
            doc = self._testMethodDoc
        except AttributeError:
            doc = self._TestCase__testMethodDoc
            return doc and doc.split("\n")[0].strip() or None