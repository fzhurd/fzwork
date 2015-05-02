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


print '****************************************'

import multiprocessing as multipro  
  
def proc1(pipe):  
    pipe.send('hello')  
    print('proc1 recv:', pipe.recv())  
  
def proc2(pipe):  
    print('proc2 recv:', pipe.recv())  
    pipe.send('hello, too')  
  
# Build a pipe  
pipe = multipro.Pipe()  
  
# Pass an end of the pipe to process 2  
p1 = multipro.Process(target=proc1, args=(pipe[0],))  
# Pass the other end of the pipe to process 1  
p2 = multipro.Process(target=proc2, args=(pipe[1],))  
  
p1.start()  
p2.start()  
p1.join()  
p2.join()  


print '***************************************************'

import time  
  
# input worker  
def inputQ(queue):  
    info = str(os.getpid()) + ' (put): ' + str(time.strftime("%Y-%m-%d__%H:%M:%S", time.localtime(time.time())))  
    queue.put(info)  
  
# output worker  
def outputQ(queue, lock):  
    info = queue.get()  
    lock.acquire()  
    print (str(os.getpid()) + '(get):' + info + "\n")  
    lock.release()  
      
# Main  
record1 = []                        # store input processes  
record2 = []                        # store output processes  
lock = multiprocessing.Lock()       # To prevent messy print  
queue = multiprocessing.Queue(3)  
  
# input processes  
for i in range(10):  
    process = multiprocessing.Process(target=inputQ, args=(queue,))  
    process.start()  
    record1.append(process)  
  
# output processes  
for i in range(10):  
    process = multiprocessing.Process(target=outputQ, args=(queue, lock))  
    process.start()  
    record2.append(process)  
  
for p in record1:  
    p.join()  
  
queue.close()  # No more object will come, close the queue  
  
for p in record2:  
    p.join()  