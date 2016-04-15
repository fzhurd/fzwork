#! /usr/bin/python
# -*- coding: utf-8 -*-


import unittest
# import dateutil.parser
import os
from nose.tools import *
import nose
# from time import time
from nose.plugins import Plugin
# from paste.script.appinstall import SetupCommand
import logging
import os
import json

log = logging.getLogger('nose.plugins.customer_parameters') 
class Customer_Parameters(Plugin):
  
    name = 'customer_parameters'
    # score = 1
    enabled = True
    # parser=None

    def options(self, parser, env):
        """Sets additional command line options."""
        super(Customer_Parameters, self).options(parser, env)

        
    def add_options(self, parser, env):
        '''Add command-line options for plugin'''
        # env_opt = 'NOSE_PASTE_SETUP_FIRST'
        
        parser.add_option('--param',
                         dest='param',
                         action="append",
                         help='Input all required parameters before running tests' )
        # options2, args = parser.parse_args()
        # print options2
        # print args
        # option_dict = vars(options2)
        # print option_dict, type(option_dict)
 
    def configure(self, options, config):
        """Configures the test timer plugin."""
        super(Customer_Parameters, self).configure(options, config)
        # self.config = config
        # self.param = {}
        # self.config = config
        # self._timed_tests = {}
        # if not self.enabled:
        #     return
        # print options
        self.param = options.param
        
        if self.param:
           param=self.param
           print param, type(param)
           # PORT=parameters['port']
    def begin(self):
        '''Called before any tests are collected or run.  Resets database.'''
        print self.param, 'sssssss'

        for i in self.param:
            print i

    def finalize(self, result):
 
        log.info("Hello from customer_parameters") 

    # def add_options(self, parser, env=os.environ):
    #    '''Add command-line options for plugin'''
    #     env_opt = 'NOSE_PASTE_SETUP_FIRST'
        
    #     parser.add_option('--parameters',
    #                       action='store_true',
    #                       default=env.get('env_opt'),
    #                      dest='parameters',
    #                      help='Run parameters before running tests.  [%s]' % env_opt)
        
    # def configure(self, options, conf):
    #     """Configure the plugin"""
    #     Plugin.configure(self, options, conf)
    #     if options.parameters:
    #         self.enabled = True
    #     print parameters
        
    # def begin(self):
    #     '''Called before any tests are collected or run.  Resets database.'''
    #     # from paste.script.appinstall import SetupCommand

    #     # Select the .ini file to run setup-app on
    #     test_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'test.ini')
    #     SetupCommand('setup-app').run([test_file])
    # def finalize(self, result):
    #     log.info('Plugin finalized!')
 
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

# def test1():
#     assertEqual(2,2)
 
if __name__ == '__main__':
    nose.main(addplugins=[Customer_Parameters()])


# from nose.plugins import Plugin
# import logging
# import os
# import nose

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

# if __name__ == '__main__':
#     nose.main(addplugins=[HelloWorld()])