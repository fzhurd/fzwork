#! /usr/bin/python
# -*- coding: utf-8 -*-

from nose.plugins import Plugin
# from nose.plugins.plugintest import run_buffered as run
import nose
from config import ConfigData

class CustomerParameters(Plugin):

    name = 'customer_parameters'
    score = 1
    enabled = True

    def options(self, parser, env={}):

        super(CustomerParameters, self).options(parser, env)
        parser.add_option('--param',
                         dest='param',
                         action='append',
                         help='Input all required parameters')

    def configure(self, options, config):

        super(CustomerParameters, self).configure(options, config)
        self.param = options.param

        params=self.param[0].split(',')
        dbconfig=dict()

        for p in params:
            k, v=p.split(':')
            dbconfig[k]=v

        self.config=dbconfig

    def begin(self):
        ConfigData.config = self.config

def suite():
     return unittest.TestSuite([TestSql('testb')])

if __name__ == '__main__':
    nose.main(addplugins=[CustomerParameters()])

# ./test_plugin.py -sv test1.py --with-customer_parameters --param HOST:'localhost',PORT:3306,SQLUSER:'test',PASSWD:'test',DATABASE:'test'
