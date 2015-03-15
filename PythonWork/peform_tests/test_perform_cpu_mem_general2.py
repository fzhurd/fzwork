#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import time
from functools import wraps
import pymongo
from pymongo import MongoClient
from memory_profiler import memory_usage
import threading
import psutil
import datetime


procids=[]
cpu_percent_usage ={}
mem_usage_psutil ={}


def print_avg_max(input_mem):
    total =sum(input_mem)
    num = len(input_mem)
    print 'The Average of Memory Usage Percentage is: %s ' % str(total/num)
    print 'The Maximum of Memory Usage Percentage is: %s ' % str(max(input_mem))


def print_monitor_result(input_data, title):
    num = len(input_data)
    start =0
    x_arr =[]
    for x in xrange(num):
        start = start+0.5
        x_arr.append(start)
    draw(x_arr, input_data, title)

     
def test_cpu_mem_percent(process_name, interval, time_out):
    start_time = datetime.datetime.now()

    while 1:

        current_time =  datetime.datetime.now()

        if (current_time - start_time) > datetime.timedelta(seconds=time_out):
            break

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

                        print 'Test Process: ', pinfo['name'], ' PID: ', pinfo['pid']
                        print 'Current CPU Use: ', pinfo['cpu_percent']
                        print 'Current Memory Used Percent: ', round(pinfo['memory_percent'])
                        print '\n'

def create_process_info_container( proc_pid = None ):
    pass


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--process-name', '-n', dest='process_name_dest', help='which process you want to test CPU and Memory', 
        type=str, required=False)

    parser.add_argument('--process-Id', '-p', dest='pid_dest', help='which PID you want to test CPU and Memory', 
         type=int, required=False)

    parser.add_argument('--interval', '-i', dest='interval_dest', help='Interval time to monitor the CPU and Memory', 
        default=0.5, type=float, required=False)

    parser.add_argument('--time-out', '-t', dest='time_out_dest', help='How long time you want to monitor CPU and Memory', 
        default=10, type=int, required=False)

    args = parser.parse_args()

    process_name = args.process_name_dest
    process_id = args.pid_dest
    interval = args.interval_dest
    time_out =  args.time_out_dest

    print psutil.Process(1185)

    for proc in psutil.process_iter():
        print proc
      
        if proc.name == process_name or proc.pid == process_id :

            print 'test process: %s PID: %s ' % (proc, proc.pid)
            procids.append(proc.pid)
            cpu_percent_usage[proc.pid]=[]
            mem_usage_psutil[proc.pid]=[]

    # test_cpu_mem_percent(process_name, interval, time_out)

   
    percs = psutil.cpu_percent(interval=0, percpu=True)
    print 'CPU Used in %d Processor CPU: %s' % (len(percs),  cpu_percent_usage)

    for (k, v) in cpu_percent_usage.items():
        print 'PID: %d, CPU Maximum Use: %f' % (k, max(v))

    print 'Memory Percentage Used Tested: ',  mem_usage_psutil

    for (k, v) in mem_usage_psutil.items():
        print 'PID: %d' % k
        print_avg_max(v)



if __name__=='__main__':
    main()