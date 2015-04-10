#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading


class MyThread(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(0.5):
            print "my thread"

class MyThread2(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run2(self):
        while not self.stopped.wait(0.5):
            print "my thread"
            # call a function
      

def main():
    stopFlag = threading.Event()
    thread = MyThread(stopFlag)
    thread.start()
    stopFlag.set()


    # stopFlag = Event()
    # thread = MyThread(stopFlag)
    # thread.start()
    # # this will stop the timer
    # stopFlag.set(


if __name__=='__main__':
    main()