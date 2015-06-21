# usr/bin/python
# -*- coding: utf-8 -*-


import unittest
import dateutil.parser
import os
from nose.tools import *
from time import time
from nose.plugins.base import Plugin

 
class Customer_Parameters(Plugin):
  
    name = 'customer_parameters_plugin'
    score = 1
    enabled = True


    def add_options(self, parser, env=os.environ):
       '''Add command-line options for plugin'''
        env_opt = 'NOSE_PASTE_SETUP_FIRST'
        
        parser.add_option('--paste-setup-first',
                          action='store_true',
                          default=env.get('env_opt'),
                         dest='paste_setup',
                         help='Run setup-app in Paste before running tests.  [%s]' % env_opt)
        
    def configure(self, options, conf):
        """Configure the plugin"""
        Plugin.configure(self, options, conf)
        if options.paste_setup:
            self.enabled = True
        
    def begin(self):
        '''Called before any tests are collected or run.  Resets database.'''
        from paste.script.appinstall import SetupCommand

        # Select the .ini file to run setup-app on
        test_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'test.ini')
        SetupCommand('setup-app').run([test_file])
 
    # def _timeTaken(self):
    #     if hasattr(self, '_timer'):
    #         taken = time() - self._timer
    #     else:
    #         # test died before it ran (probably error in setup())
    #         # or success/failure added before test started probably
    #         # due to custom TestResult munging
    #         taken = 0.0
    #     return taken
 
    # def options(self, parser, env):
    #     """Sets additional command line options."""
    #     super(TestTimer, self).options(parser, env)
 
    # def configure(self, options, config):
    #     """Configures the test timer plugin."""
    #     super(TestTimer, self).configure(options, config)
    #     self.config = config
    #     self._timed_tests = {}
 
    # def startTest(self, test):
    #     """Initializes a timer before starting a test."""
    #     self._timer = time()
 
    # def report(self, stream):
    #     """Report the test times"""
    #     if not self.enabled:
    #         return
    #     d = sorted(self._timed_tests.iteritems(), key=operator.itemgetter(1))
    #     for test, time_taken in d:
    #         stream.writeln("%s: %0.4f" % (test, time_taken))
 
    # def _register_time(self, test):
    #     self._timed_tests[test.id()] = self._timeTaken()
 
    # def addError(self, test, err, capt=None):
    #     self._register_time(test)
 
    # def addFailure(self, test, err, capt=None, tb_info=None):
    #     self._register_time(test)
 
    # def addSuccess(self, test, capt=None):
    #     self._register_time(test)
 
 
if __name__ == '__main__':
    nose.main(addplugins=[TestTimer()])


# from nose.plugins import Plugin

# log = logging.getLogger('nose.plugins.helloworld')

# class HelloWorld(Plugin):
#     name = 'helloworld'

#     def options(self, parser, env=os.environ):
#         super(HelloWorld, self).options(parser, env=env)

#     def configure(self, options, conf):
#         super(HelloWorld, self).configure(options, conf)
#         if not self.enabled:
#             return

#     def finalize(self, result):
#         log.info('Hello pluginized world!')

