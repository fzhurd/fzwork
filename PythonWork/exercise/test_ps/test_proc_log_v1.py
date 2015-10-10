#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import unittest
import psutil
import os
import sys

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
                return process_cmdline


    def test_proc(self):
        pwd_is_hidden=False
        proc_cmdline = self.find_process('sonarsql')
        print proc_cmdline[2]

        split_parts = proc_cmdline[2].split(":")

        if split_parts[2].startswith('xxxx'):
            pwd_is_hidden=True

        self.assertEquals(pwd_is_hidden, True)

    def tail(self, f, n, offset=None):
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

    def tail2(self, fname, line_num):
        pwd_is_hidden2=False
        with open(fname, "r") as f:
            f.seek (0, 2)           
            fsize = f.tell()        
            f.seek (max (fsize-1024, 0), 0) # Set pos @ last n chars
            lines = f.readlines()       # Read to end

        lines = lines[-line_num:]    # Get last 10 lines

        find_str='sonarsql'
        # This returns True if any line is exactly find_str + "\n"
        # print find_str + "\n" in lines

        # If you're searching for a substring
        # for line in lines:
        for index, line in enumerate(lines):
            cleanedLine = line.strip()
            # print cleanedLine
            if cleanedLine and 'SonarSQL' in line:

                sonarsql_conn_str = lines[index-1]
                sonarsql_conn_split = sonarsql_conn_str.split()
                # print sonarsql_conn_split

                filtered =filter(lambda x: 'mongodb://' in x,sonarsql_conn_split )
                # print filtered
                if filtered:
                    filtered_str= filtered[0].split(':')
                if 'xxxx' in filtered_str[2]:
                    pwd_is_hidden2 = True

        return pwd_is_hidden2



    def test_log(self):
        os.chdir('/var/log/sonarsql')
        if not os.geteuid()==0:
            sys.exit("\nOnly root user can run this test\n")

        os.setuid(0)
        pwd_is_hidden2 =self.tail2('sonarsql.log', 2)

        self.assertEquals(pwd_is_hidden2, True)



