#!/usr/bin/python
# -*- coding: utf-8 -*-

import os  
import threading  
import multiprocessing  
  
# worker function  
def worker(sign, lock):  
    lock.acquire()  
    print(sign, os.getpid())  
    lock.release()  
  
# Main  
print('Main:', os.getpid())      # 主进程  
  
# Multi-thread  
record = []  
lock  = threading.Lock()  
for i in range(5):  
    thread = threading.Thread(target=worker,args=('thread', lock))  
    thread.start()  
    record.append(thread)  
  
for thread in record:  
    print(thread)  
    thread.join()  
  
# Multi-process  
record = []  
lock = multiprocessing.Lock()  
for i in range(5):  
    process = multiprocessing.Process(target=worker,args=('process',lock))  
    process.start()  
    record.append(process)  
  
for process in record:  
    print(process)  
    process.join()  