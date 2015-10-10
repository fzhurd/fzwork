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
        pwd_is_hidden=False
        proc_cmdline = self.find_process('sonarsql')
        print proc_cmdline[2]

        split_parts = proc_cmdline[2].split(":")

        if split_parts[2].startswith('xxxx'):
            pwd_is_hidden=True

        self.assertEquals(pwd_is_hidden, True)

    def tail(f, n, offset=None):
        """Reads a n lines from f with an offset of offset lines.  The return
        value is a tuple in the form ``(lines, has_more)`` where `has_more` is
        an indicator that is `True` if there are more lines in the file.
        """
        avg_line_length = 74
        to_read = n + (offset or 0)

        while 1:
            try:
                f.seek(-(avg_line_length * to_read), 2)
            except IOError:
                # woops.  apparently file is smaller than what we want
                # to step back, go to the beginning instead
                f.seek(0)
            pos = f.tell()
            lines = f.read().splitlines()
            if len(lines) >= to_read or pos == 0:
                return lines[-to_read:offset and -offset or None], \
                       len(lines) > to_read or pos > 0
            avg_line_length *= 1.3


    def test_log(self):
        pass



