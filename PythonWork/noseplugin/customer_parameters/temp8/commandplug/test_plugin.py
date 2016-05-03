#! /usr/bin/python
# -*- coding: utf-8 -*-

from nose.plugins import Plugin
import nose
from config import ConfigData

class CustomerCommandParameter(Plugin):

    name ='command_parameters'
    score = 1
    enabled=True

    def options(self, parser, env={}):

        super(CustomerCommandParameter, self).options(parser, env)
        parser.add_option('--com',
                         dest='com',
                         action='append',
                         help='Input all required parameters')

    def configure(self, options, config):

        super(CustomerCommandParameter, self).configure(options, config)
        self.param = options.com

        params=self.com[0].split(',')
        dbconfig=dict()

        for p in params:
            k, v=p.split(':')
            dbconfig[k]=v

        self.config=dbconfig

    def begin(self):
        ConfigData.config = self.config

def suite():
     return unittest.TestSuite([TestSql('testb')])

# if __name__ == '__main__':
#     nose.main(addplugins=[CustomerParameters()])

# ./test_plugin.py -sv test1.py --with-customer_parameters --param HOST:'localhost',PORT:3306,SQLUSER:'test',PASSWD:'test',DATABASE:'test'
