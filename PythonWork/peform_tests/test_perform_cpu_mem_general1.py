#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import time
from functools import wraps
import pymongo
from pymongo import MongoClient
from memory_profiler import memory_usage
import threading
import psutil
import os



# cpu_percent_running =[]
procids=[]
cpu_percent_usage ={}
mem_usage_psutil ={}
mem_usage_memory_profiler ={}




'''
Decorator that reports the execution time.
'''
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print 'start time: ', start
        func(*args, **kwargs)
        end = time.time()
        print 'end time: ', end
        used_time = end - start
        print 'need time in seconds: ', used_time
        return used_time
    return wrapper


def print_cpu_memory(sec=None):

    mem = psutil.virtual_memory()
    
    print 'CPU used percent: %s' % psutil.cpu_percent(interval=sec)
    print 'Memory Total: %s, Used: %s, Percent: %s,  Available: %s ' % (mem.total, mem.used, mem.percent, mem.available)

def print_avg_max(input_mem):
    total =sum(input_mem)
    num = len(input_mem)
    print 'The Average of Memory Usage is: %s ' % str(total/num)
    print 'The Maximum of Memory Usage is: %s ' % str(max(input_mem))

def print_mem(proc_name, interval, timeout):

    mem_usage_memory_profiler[proc_name] =memory_usage(proc=proc_name, interval=interval, timeout=timeout)

    return mem_usage_memory_profiler

def init_thread_measure(thread_name, target_method, args_tup, daemon=True ):

    thread_name = threading.Thread(target=target_method, args=args_tup )
    thread_name.setDaemon(daemon)
    thread_name.start()



def test_cpu_mem_percent(process_name, interval=0.5):

    while 1:

        time.sleep(interval)

        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['username', 'pid', 'name', 'cpu_percent', 'memory_percent'])
            except psutil.NoSuchProcess:
                pass
            else:
                for i in procids:
                    if pinfo['pid']==i:
                        cpu_percent_usage[i].append(pinfo['cpu_percent'])
                        mem_usage_psutil[i].append(round(pinfo['memory_percent'],4) )


def main():

    print psutil.cpu_percent()
    for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['username', 'pid', 'name', 'cpu_percent', 'memory_percent'])
            except psutil.NoSuchProcess:
                pass
    global mem_usage_memory_profiler
    parser = argparse.ArgumentParser()
    parser.add_argument('--process-name', '-n', dest='process_name_dest', help='which process you want to test CPU and Memory', 
        default='sonard', type=str, required=False)


    args = parser.parse_args()
    process_name = args.process_name_dest

    print psutil.process_iter()
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            print 'test process: %s PID: %s ' % (proc, proc.pid)
            procids.append(proc.pid)
            cpu_percent_usage[proc.pid]=[]
            mem_usage_psutil[proc.pid]=[]

    test_cpu_mem_percent(process_name, interval=0.5)
    print_mem(proc_name, 0.5, 20)
    # init_thread_measure('t_cpu_mem', test_cpu_mem_percent, (process_name,0.5), True )

    percs = psutil.cpu_percent(interval=0, percpu=True)
    print 'CPU Used in %d Processor CPU: %s' % (len(percs),  cpu_percent_usage)

    print 'Memory Percentage Used Tested By psutil: ',  mem_usage_psutil
    print '\n'
   
    print 'Memory Tested By Memory_Profiler: ', mem_usage_memory_profiler
    print '\n'

    print '############################################################'

    print 'Test By psutil'
    # for (k, v) in mem_usage_psutil.items():
        
    #     print 'PID: %d' % k
        # print_avg_max(v)

    print '############################################################'
    print 'Test By Memory_Profiler'
    # for (k, v) in mem_usage_memory_profiler.items():     
    #     print 'PID: %d' % k
    #     print_avg_max(v)


            



if __name__=='__main__':
	main()