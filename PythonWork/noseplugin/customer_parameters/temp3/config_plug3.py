#! /usr/bin/python
# -*- coding: utf-8 -*-

from nose.plugins import Plugin
import nose
import unittest

import os
cfg_path = os.path.join(os.path.dirname(__file__), 'example.cfg')
cfg_file = open(cfg_path, 'w')
bytes = cfg_file.write("""\
[DEFAULT]
can_frobnicate = 1
likes_cheese = 0
""")
cfg_file.close()


class ConfigurableWidget(object):
    cfg = None
    def can_frobnicate(self):
        print self.cfg
        return self.cfg.get('can_frobnicate', True)

    def likes_cheese(self):
        return self.cfg.get('likes_cheese', True)

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

class ConfiguringPlugin(Plugin):
    enabled = True
    def configure(self, options, conf):
        pass

    def begin(self):
        ConfigurableWidget.cfg = {}

class BetterConfiguringPlugin(Plugin):

    def options(self, parser, env={}):
        parser.add_option('--widget-config', action='store',
            dest='widget_config', default=None,
            help='Specify path to widget config file')

    def configure(self, options, conf):
        if options.widget_config:
            self.load_config(options.widget_config)
            self.enabled = True

    def begin(self):

        ConfigurableWidget.cfg = self.cfg

    def load_config(self, path):
        from ConfigParser import ConfigParser
        p = ConfigParser()
        p.read([path])
        self.cfg = dict(p.items('DEFAULT'))

def suite():
    return unittest.TestSuite([
        TestConfigurableWidget('test_can_frobnicate'),
        TestConfigurableWidget('test_likes_cheese')])

if __name__ == '__main__':
    # argv = [__file__, '-v']
    # nose.run(argv=argv, suite=suite(),plugins=[ConfiguringPlugin()])  
    # nose.main(addplugins=[ConfiguringPlugin()], argv=argv, suite=suite())
    ConfigurableWidget.cfg = None
    argv = [__file__, '-v', '--widget-config', cfg_path]
    nose.run(argv=argv, suite=suite(),plugins=[BetterConfiguringPlugin()])

