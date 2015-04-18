#!/usr/bin/env python
# sig.py
# signal test
import time
import signal
import sys

NEEDEXIT=False
def SignalHandler(sig, id):
    global NEEDEXIT
    if sig == signal.SIGUSR1:
      print 'received signal USR1'
    elif sig == signal.SIGHUP:
      print 'received signal HUP'
    elif sig == signal.SIGTERM:
      print 'received SIGTERM, shutting down'
      NEEDEXIT = True

signal.signal(signal.SIGUSR1, SignalHandler)
signal.signal(signal.SIGHUP, SignalHandler)
signal.signal(signal.SIGTERM, SignalHandler)

while 1:
    if NEEDEXIT:
        sys.exit()
    time.sleep(1)