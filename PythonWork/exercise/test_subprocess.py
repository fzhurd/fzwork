#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
from subprocess import Popen, PIPE


def main():

    process = Popen(['ls'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    print process


    out = subprocess.call("ls -l", shell=True)
    print out, 'xxxxxxxxxxx'

    child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
    child2 = subprocess.Popen(["wc"], stdin=child1.stdout,stdout=subprocess.PIPE)
    out = child2.communicate()
    print(out, ' popen results') 


    out2 = subprocess.call("wrongls -l", shell=True)
    print out2, 'raise error'


if __name__ == '__main__':
    main()