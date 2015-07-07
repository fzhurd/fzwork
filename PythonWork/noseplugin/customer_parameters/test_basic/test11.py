# usr/bin/python
# -*- coding: utf-8 -*-


import os
from nose.plugins import Plugin

class MyCustomPlugin(Plugin):
    name = 'myplugin'

    def options(self, parser, env=os.environ):
        parser.add_option('--custom-path', action='store',
                          dest='custom_path', default=None,
                          help='Specify path to widget config file')

    def configure(self, options, conf):
        if options.custom_path:
            self.make_some_configs(options.custom_path)
            self.enabled = True

    def make_some_configs(self, path):
        # do some stuff based on the given path
        pass

    def begin(self):
        pass

    def help(self):
        pass