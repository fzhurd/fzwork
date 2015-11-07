#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
from subprocess import Popen, PIPE


def main():

    process = Popen(['ls'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    print process


    out = subprocess.call("ls -l", shell=True)
    print out, 'oooooooooooo'

if __name__ == '__main__':
    main()