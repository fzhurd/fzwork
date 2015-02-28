#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import datetime
import os
import pymongo
import sys
import time
from pymongo import MongoClient
import subprocess

import matplotlib as mpl  
mpl.use('Agg')  
import matplotlib.pyplot as plt  
import datetime as dt  
from matplotlib.font_manager import FontProperties  
import sys  
  
def draw_trend(data_file,object_type):  
    fontP = FontProperties()  
    fontP.set_size('small')  
    data=open(data_file,"r")  
    lines=data.readlines()  
    data.close()  
    lable_list=lines[0].split(None)  
    #data={"lable_name":[x,y1,y2],x:[1,2,4],y1:[2,4],y3:[4,5]}  
    lable_name=[]  
    data_list=[]  
  
    for lable in lable_list:  
        lable_name.append(lable)  
        data_list.append([])  
  
    for line in lines[1:]:  
        line_list=line.strip().split(None)  
        #print line_list  
        #print data_list  
        for i in xrange(len(data_list)):  
            #print data_list  
            if i==0:  
                data_list[0].append(dt.datetime(int(line_list[0][0:4]), int(line_list[0][4:6]),  
                    int(line_list[0][6:8]),int(line_list[0][9:11]),  
                    int(line_list[0][12:14]),int(line_list[0][15:17])))  
            else:  
                if object_type=="mem":  
                    data_list[i].append(float(line_list[i]))  
                else:  
                    data_list[i].append(float(line_list[i]))  
    #print data_list  
    ''''' 
    dates = [dt.datetime.today() + dt.timedelta(days=i) for i in range(10)] 
    values = np.random.rand(len(dates)) 
    '''  
    mpl_date2num=mpl.dates.date2num(data_list[0])  
    for y_value in data_list[1:]:  
        plt.plot_date(mpl_date2num, y_value,"-",label=lable_name[data_list.index(y_value)])  
    xAxis = plt.axes().xaxis  
    dateFmt = mpl.dates.DateFormatter('%H:%M')  
    #daysLoc = mpl.dates.DayLocator()  
    #minLoca=mpl.dates.MinuteLocator(interval=2)  
    #secLoc=mpl.dates.SecondLocator(interval=60)  
    xAxis.set_major_formatter(dateFmt)  
    #xAxis.set_major_locator(minLoca)  
    #xAxis.set_minor_locator(secLoc)  
  
    #plt.legend(loc='upper right',bbox_to_anchor=(1.0, 1.07),prop = fontP,ncol=len(lable_name)-1)  
    #leg=plt.legend(loc='upper right',prop = fontP)  
    leg=plt.legend(loc='upper right',prop={'size':8})  
    leg.get_frame().set_alpha(0.5)  
    plt.tick_params(axis='both', labelsize=8)  
    plt.xlabel('Time')  
    if object_type=="mem":  
        plt.ylabel('Memory/unit M')  
    if  object_type=="io":  
        plt.ylabel('IO Busy')  
    if  object_type=="cpu":  
        plt.ylabel('CPU Usage Percent')  
    plt.savefig(data_file+".png")  
  
    #plt.show()  
try:  
    draw_trend(sys.argv[1],sys.argv[2])  
except:  
    print "error command, right command should be:","python draw_matlab.py datafile  mem/io/cpu"  

# def main():
# 	print 'hi'



# if __name__=='__main__':
# 	main()