#! /usr/bin/python
# -*- coding: utf-8 -*-

class ConfigData(object):

    config={}

    def store_data(self, data):
        self.config=data
        return self.config

    def get_data(self):
        return self.config