# usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import unittest
import dateutil.parser
import os
from nose.tools import *
from bson.son import SON
import sqlalchemy
from sqlalchemy import create_engine
import operator
from time import time
import nose
from nose.plugins.base import Plugin

 
class TestTimer(Plugin):
  
    name = 'test-timer'
    score = 1
    enabled = True
 
    def _timeTaken(self):
        if hasattr(self, '_timer'):
            taken = time() - self._timer
        else:
            taken = 0.0
        return taken
 
    def options(self, parser, env):
        """Sets additional command line options."""
        super(TestTimer, self).options(parser, env)
 
    def configure(self, options, config):
        """Configures the test timer plugin."""
        super(TestTimer, self).configure(options, config)
        self.config = config
        self._timed_tests = {}
 
    def startTest(self, test):
        """Initializes a timer before starting a test."""
        self._timer = time()
 
    def report(self, stream):
        """Report the test times"""
        if not self.enabled:
            return
        d = sorted(self._timed_tests.iteritems(), key=operator.itemgetter(1))
        for test, time_taken in d:
            stream.writeln("%s: %0.4f" % (test, time_taken))
 
    def _register_time(self, test):
        self._timed_tests[test.id()] = self._timeTaken()
 
    def addError(self, test, err, capt=None):
        self._register_time(test)
 
    def addFailure(self, test, err, capt=None, tb_info=None):
        self._register_time(test)
 
    def addSuccess(self, test, capt=None):
        self._register_time(test)
 
 
if __name__ == '__main__':
    nose.main(addplugins=[TestTimer()])

