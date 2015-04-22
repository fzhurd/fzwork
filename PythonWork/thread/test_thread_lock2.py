#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import time
import logging

final_results=[]

lock = threading.Lock()
con = threading.Condition()

def main():
  keep_run_thread = threading.Thread(target=keep_run, name='alarm_thread') 
  keep_run_thread.setDaemon(False)
  keep_run_thread.start()
  time.sleep(3)
  keep_run_thread.join(1)
  print final_results
  # time.sleep(4)
  # if lock.acquire():

    # print final_results
    # con.notify()
    # con.wait()
    # lock.release()


def keep_run():
    i=0
  # if lock.acquire():
  # if con.acquire():
    while i<10:
      print i
      i=i+1
      time.sleep(1)
      
      final_results.append(i)
      print final_results, '*******************************'
      print calculate_sum(final_results),'ssssssssssssssssssssssss'
      print calculate_avg(final_results),'vvvvvvvvvvvvvvvvvvvvvvvvvv'
      # con.notify()
      # con.wait()
    # lock.release()
def calculate_sum(input):
  return sum(input)

def calculate_avg(input):
  return reduce(lambda x, y: x + y, input) / len(input)



if __name__=='__main__':
  main()
 
# num = 0
# lock = threading.Lock()
 
# def func(st):
#     global num
#     print (threading.currentThread().getName() + ' try to acquire the lock')
#     if lock.acquire():
#         print (threading.currentThread().getName() + ' acquire the lock.' )
#         print (threading.currentThread().getName() +" :%s" % str(num) )
#         num += 1
#         time.sleep(st)
#         print (threading.currentThread().getName() + ' release the lock.'  )        
#         lock.release()
 
# t1 = threading.Thread(target=func, args=(8,))
# t2 = threading.Thread(target=func, args=(4,))
# t3 = threading.Thread(target=func, args=(2,))
# t1.start()
# t2.start()
# t3.start()



# semaphore = threading.Semaphore(2)
 
# def func():
#     if semaphore.acquire():
#         for i in range(5):
#           print (threading.currentThread().getName() + ' get semaphore')
#         semaphore.release()
#         print (threading.currentThread().getName() + ' release semaphore')
        
        
# for i in range(4):
#   t1 = threading.Thread(target=func)
#   t1.start()


# logging.basicConfig(level=logging.DEBUG,
# format="(%(threadName)-10s : %(message)s",
# )

# def wait_for_event_timeout(e, t):
#     """Wait t seconds and then timeout"""
#     while not e.isSet():
#       logging.debug("wait_for_event_timeout starting")
#       event_is_set = e.wait(t)
#       logging.debug("event set: %s" % event_is_set)
#     if event_is_set:
#       logging.debug("processing event")
#     else:
#       logging.debug("doing other work")
      
# e = threading.Event()
# t2 = threading.Thread(name="nonblock",
# target=wait_for_event_timeout,args=(e, 2))
# t2.start()
# logging.debug("Waiting before calling Event.set()")
# time.sleep(7)
# e.set()
# logging.debug("Event is set")


# exitapp = False
# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         exitapp = True
#         raise

# def threadCode(...):
#     while not exitapp:
#       pass