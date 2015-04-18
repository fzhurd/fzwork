#!/usr/bin/python
# -*- coding: utf-8 -*-

import signal
import time
import threading


def signal_handler(num, stack):
    print time.ctime(), 'Alarm in', threading.currentThread()


def use_alarm():
    print time.ctime(), 'Setting alarm in', threading.currentThread()
    signal.alarm(10)
    print time.ctime(), 'Sleeping in', threading.currentThread()
    # time.sleep(3)
    print time.ctime(), 'Done with sleep'


def keep_run():

  i=0
  while 1:
    print i
    i=i+1
    time.sleep(1)

def main():
  alarm_thread = threading.Thread(target=use_alarm, name='alarm_thread') 
  alarm_thread.start()
  # time.sleep(0.1)
  
  keep_run()
  signal.signal(signal.SIGALRM, signal_handler)

if __name__=='__main__':
  main()


# def signal_handler(num, stack):
#     print time.ctime(), 'Alarm in', threading.currentThread()


# signal.signal(signal.SIGALRM, signal_handler)



# def use_alarm():
#     print time.ctime(), 'Setting alarm in', threading.currentThread()
#     signal.alarm(1)
#     print time.ctime(), 'Sleeping in', threading.currentThread()
#     time.sleep(3)
#     print time.ctime(), 'Done with sleep'



# alarm_thread = threading.Thread(target=use_alarm, name='alarm_thread') 
# alarm_thread.start()
# time.sleep(0.1)



# print time.ctime(), 'Waiting for', alarm_thread
# alarm_thread.join()



# print time.ctime(), 'Exiting normally'