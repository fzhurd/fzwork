#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
from subprocess import Popen, PIPE



def main():

    res = process = Popen(['ls'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    print res

if __name__ == '__main__':
    main()