#!usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import unittest
import pymongo
import subprocess
import dateutil.parser
import os
from subprocess import call
from multiprocessing import Process
from threading import Thread
from nose.tools import *
from bson.son import SON
import sqlalchemy
from sqlalchemy import create_engine

import logging
import operator
from time import time
import nose
from nose.plugins.base import Plugin

class RegexPicker(Plugin):
    
    name = "RegexPicker"

    def __init__(self):
        Plugin.__init__(self)
        self.verbose = False


    def options(self, parser, env):
        Plugin.options(self, parser, env)
        parser.add_option("--re-pattern",
            dest="pattern", action="store",
            default=env.get("NOSE_REGEX_PATTERN", "test.*"),
            help=("Run test methods that have a method name matching this regular expression"))


    def configure(self, options, conf):

        Plugin.configure(self, options, conf)
        self.pattern = options.pattern
        if options.verbosity >= 2:
            self.verbose = True
            if self.enabled:
                err.write("Pattern for matching test methods is %s\n" % self.pattern)


    def wantMethod(self, method):
        wanted = re.match(self.pattern, method.func_name) is not None

        if self.verbose and wanted:
            err.write("nose will run %s\n" % method.func_name)
            return wanted



if __name__ == "__main__":
    args = ["", "recipe13", "--with-regexpicker", "--re-pattern=test.*|length", "--verbosity=2"]
    print "With verbosity..."
    print "===================="
    nose.run(argv=args, plugin=[RegexPicker()])
    print "Without verbosity..."
    print "===================="
    args = args[:-1]
    nose.run(argv=args, plugin=[RegexPicker()])
