#! /usr/bin/python
# -*- coding: utf-8 -*-

class ConfigData(object):

    config={'a':1}

    def store_data(self, data):
        self.config=data
        print self.config, 'sssssssss'
        return self.config

    def get_data(self):
        return self.config