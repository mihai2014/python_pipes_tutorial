from __future__ import print_function
import os, time, select
from ansi_codes import *
from sys import argv

msg = "Choose argument:\n1 - non-blocking pipes\n2 - select"

try:
    script, option  = argv
    if option not in ["1","2"]:
        print(msg)
        sys.exit()
except:
    print(msg)
    sys.exit()

import fcntl
def setNonBlock(fd):
    flag = fcntl.fcntl(fd, fcntl.F_GETFD)
    fcntl.fcntl(fd, fcntl.F_SETFL, flag | os.O_NONBLOCK)
    return fd

def child1(w):
    for n in range(10):
        os.write(w, str(n).encode())
        time.sleep(1)
    os._exit(0)

def child2(w):
    for n in range(10):
        os.write(w, str(n).encode())
        time.sleep(2)
    os._exit(0)

def stopCondition():
    """ collect zombies and end parent
        when all children stops
    """
    try:
        print(Green,XY(3,0),EraseLine,end = '')
        pidEnd = os.waitpid(-1, os.WNOHANG)
        if pidEnd[0] : 
            print(">> Process ended : {}".format(pidEnd[0]))
        return 0
    except:
        print("All children stops. Bye.")
        return 1

def parent():

    # file descriptors r, w for reading and writing
    r1, w1 = os.pipe() 
    r2, w2 = os.pipe()

    children = {}

    pid = os.fork()

    if pid == 0:
        child1(w1)
    else:
        print("parent:", os.getpid(), "has a child :", pid)
        children[r1] = 1 

    pid = os.fork()
       
    if pid == 0:
        child2(w2)
    else:
        print("parent:", os.getpid(), "has a child :", pid)
        children[r2] = 2

    # closing file descriptors we don't need
    os.close(w1)
    os.close(w2)

    print(EraseDisplay)

    if option == '1':

        #non-blocking pipe
        #refresh every n sec: depending on timing, there could be no data from children
        #other parent actions NOT BLOCKED until data availability from pipes
        setNonBlock(r1)
        setNonBlock(r2)
        while True:
            #some other actions here ...
            if stopCondition(): break
            for r in [r1, r2]:
                try:
                    data = os.read(r, 5).decode()
                except OSError:
                    data = "--"
                #print("pipe",r,"data",data)

                if r == r1:
                    print(EraseLine,Green,XY(1,0),end = '')
                    name = 1
                if r == r2:
                    print(EraseLine,Green,XY(2,0),end = '')
                    name = 2
                print("child",name,"pipe",r,"data",data.decode())

            time.sleep(.5)

    if option == '2':

        #blocking pipe and select
        #refresh only when data available from children
        #other parent actions are BLOCKED until data available on pipes
        while True:
            if stopCondition(): break
            i, o, e = select.select([r1,r2], [], [] ) # no excepts nor timeout
            for r in i:
                data = os.read(r, 5)
                if children[r] == 1:
                    print(EraseLine,Green,XY(1,0),end = '')
                if children[r] == 2:
                    print(EraseLine,Green,XY(2,0),end = '')
                print("child",children[r],"pipe",r,"data",data.decode())

    print(Reset)

parent()
