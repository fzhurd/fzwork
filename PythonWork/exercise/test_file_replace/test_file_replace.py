#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import unittest
import psutil
import os
import sys
import re

from tempfile import mkstemp
from shutil import move
from os import remove, close

HOST='127.0.0.1'
USER='test'
PASSWD='test'
DATABASE='test'
PORT=3307

class Test_Proc_Log(unittest.TestCase):
    def setUp(self):
        pass

    # def replace(self,file_path, pattern, subst):
    #     #Create temp file
    #     fh, abs_path = mkstemp()
    #     with open(abs_path,'w') as new_file:
    #         with open(file_path) as old_file:
    #             for line in old_file:
    #                 print line, 'lllllllllllll'
    #                 new_file.write(line.replace(pattern, subst))
                    
    #     close(fh)

    #     remove(file_path)

    #     move(abs_path, file_path)

    # def replace(self,file_path, pattern, subst):
    def replace(self,file_path):
        regex = re.compile(r"^ROOT_PWHASH=", re.IGNORECASE)

        #Create temp file
        fh, abs_path = mkstemp()
        with open(abs_path,'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    # print line, 'lllllllllllll'
                    # new_file.write(line.replace(pattern, subst))
                    
                    # line = regex.sub( 'ROOT_PWHASH=', line)
                    if line.startswith("ROOT_PWHASH="):
                        # print 'need to handle'
                        line_comment = '#'+line
                        new_file.write(line.replace(line, line_comment))
                        length = len('ROOT_PWHASH=')
                        line_new=line[0:length]+'\n'
                        new_file.write(line_new)
                        continue
                    new_file.write(line)
                    
        close(fh)

        remove(file_path)

        move(abs_path, file_path)

    # def recover(self,file_path, pattern, subst):
    def recover(self,file_path):
        
        fh, abs_path = mkstemp()
        with open(abs_path,'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    # print line, 'lllllllllllll'

                    if line.startswith("#ROOT_PWHASH="):
                        print 'need to recover'
                        line_remove_comment = line[1:]
                        new_file.write(line.replace(line, line_remove_comment))
                        
                        continue
                    if line.startswith("ROOT_PWHASH="):
                        print 'need to remove'
                        new_file.write(line.replace(line, " "))
                        continue

                    new_file.write(line)
                    
        close(fh)

        remove(file_path)

        move(abs_path, file_path)

    def test_password(self):
        # os.chdir('/etc/default/')
        # if not os.geteuid()==0:
        #     sys.exit("\nOnly root user can run this test\n")

        # os.setuid(0)
        # self.replace('./test.conf', 'ROOT_PWHASH=', 'DONE')


        # self.replace('./test.conf')
        self.recover('./test.conf')

    