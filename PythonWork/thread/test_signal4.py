#!/usr/bin/python
# -*- coding: utf-8 -*-
import signal
import os
print signal.SIGALRM
print signal.SIGCONT


# Define signal handler function
def myHandler(signum, frame):
    print('I received: ', signum)

# register signal.SIGTSTP's handler 
signal.signal(signal.SIGTSTP, myHandler)
signal.pause()
print('End of Signal Demo')



# Define signal handler function
def myHandler2(signum, frame):
    print("Now, it's the time")
    print os.getpid()
    exit()

# register signal.SIGALRM's handler 
signal.signal(signal.SIGALRM, myHandler2)
signal.alarm(5)

while True:
    print('not yet')