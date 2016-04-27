#! /usr/bin/python
# -*- coding: utf-8 -*-

from nose.tools import *
from nose.plugins import Plugin
from nose.plugins.plugintest import run_buffered as run
import nose
import sys
import unittest
from unittest import TestCase
# from tests import *

# import pdb
# pdb.set_trace()

PARAMETERS=None

class Parameters_Example(Plugin):
    global PARAMETERS
    name = 'parameters_example'
    score = 1
    enabled = True

    def options(self, parser, env={}):

        super(Parameters_Example, self).options(parser, env)
        parser.add_option('--param',
                         dest='param',
                         action='append',
                         help='Input all required parameters')

    def configure(self, options, config):

        super(Parameters_Example, self).configure(options, config)
        self.config={'x':1}
        # self.load_config(options.widget_config)
        # global PARAMETERS
        # PARAMETERS=options.param
        # print PARAMETERS


    def begin(self):
        # ConfigData.config = {}
        ConfigData.config = self.config
        print ConfigData.config, 'tttt'

        # global PARAMETERS
        # print PARAMETERS, 'bbbbbbbbbb'
        # ConfigurableWidget.cfg = {}
        # ConfigurableWidget.cfg=PARAMETERS

        # t=ConfigData()
        # t.store_data(PARAMETERS)
        # print t.get_data(), 'config'

        # return t

        # return PARAMETERS

    # def load_config(self):
   #     pass

class Test_Example(TestCase):
    def setUp(self):
        # print PARAMETERS, 'parsed' 
        self.widget = ConfigData()
        print self.widget.config, 'zzzzzzzzz'
    def testb(self):   
        # print sys.argv[5], 'vvvvvvvvvvvvvvv'
        print self.widget.config, 'zzzzzzzzz'
        pass


class ConfigData(object):

    config={'a':1}

    def store_data(self, data):
        self.config=data
        print self.config, 'sssssssss'
        return self.config

    def get_data(self):
        return self.config

# class ConfigurableWidget(object):
#     cfg = None
#     def can_frobnicate(self):
#         return self.cfg.get('can_frobnicate', True)
    
#     def likes_cheese(self):
#         return self.cfg.get('likes_cheese', True)
# def suite():
#     return unittest.TestSuite([
#         Test_Example('test_can_frobnicate'),
#         Test_Example('test_likes_cheese')])

def suite():
     # global PARAMETERS
     # print PARAMETERS, 'nnnnnnnnnnnnnnnnnnnnnn'
     print ConfigData.config, 'xxxxxxxxxxxx'
     return unittest.TestSuite([Test_Example('testb')])

if __name__ == '__main__':
    argv = sys.argv[:]
    print argv, 'vvvvvvvvvvvvv'
    # argv.insert(1, "--with-parameters_example")
    # argv.insert(2, "--param")
    nose.main(argv=argv, addplugins=[Parameters_Example()], suite=suite())
    # nose.run(suite=suite(),plugins=[Parameters_Example()])
    # run(argv=argv, addplugins=[Parameters_Example()], suite=suite())
    # argv = [__file__, '-sv', '--parameters_example', '--param', {HOST:'localhost',PORT:3306,SQLUSER:'test',PASSWD:'test',DATABASE:'test'}]
    # print argv, 'vvvvvvvvvvvvv'
    # run(argv=argv, suite=suite(), plugins=[Parameters_Example()]) 


