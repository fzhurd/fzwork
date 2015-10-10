#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import unittest
import psutil

HOST='127.0.0.1'
USER='test'
PASSWD='test'
DATABASE='test'
PORT=3307

class Test_Proc_Log(unittest.TestCase):
    def setUp(self):
        pass

    def find_process(self, process_name):
        for proc in psutil.process_iter():
            if proc.name()==process_name:
                process_cmdline = proc.cmdline()
                # print proc.cmdline()
                return process_cmdline


    def test_proc(self):
        proc_cmdline = self.find_process('sonarsql')
        print proc_cmdline[2]

        split_parts = proc_cmdline[2].split(":")

        for s in split_parts:
            print s

        if split_parts[2].startswith('xxxx'):
            print 'pass'
        else:
            print 'fail'



