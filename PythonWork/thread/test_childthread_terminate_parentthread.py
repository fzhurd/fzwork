import threading
import time
import os
from subprocess import call

def check_Temp(temp, delay, run_event,pid, endit):
    while run_event.is_set():
        time.sleep(delay)
        ##code for checking temperature will go here.
        print "temp is %s \n"%temp
        temp=temp-1
        #print os.getpid()
        if temp<=38:
            print 'LowTemp %s!' % (temp, )
            endit()
            run_event.clear()

if __name__ == "__main__":
    run_ok = True
    def Terminator():
        global run_ok
        print "Terminating"
        run_ok = False

    run_event = threading.Event()
    run_event.set()
    temp =45
    d1=.1
    #print os.getpid()
    pid=os.getpid();
    run_ok = True
    t1 = threading.Thread(target = check_Temp, args = (temp,d1,run_event,pid, Terminator))
    t1.start()
    print "Starting"

 ########## main code will go here, just have a simple counter here to test the functionality.

    x=25
    try:
        while run_ok:
            time.sleep(.1)
            x=x-1
            print "x is %s "%x
            if x<0:
                print "x is %s"%x
                raise Exception('spam', 'eggs')
            #exit()
        t1.join()
        print 'Finished!'