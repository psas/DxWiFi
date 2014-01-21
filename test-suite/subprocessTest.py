#!/usr/bin/env python
import os
import subprocess
import time


#the file path string needs to be concatinated outside of the subprocess call.


#this works

try:
    os.mkdir( "./runname")
except:
    pass
try:
    os.mkdir( "./runname/first")
except:
    pass
series_dir = "./runname/first/test4.pcap"
print "this works Path = "+ series_dir
tcpdmp = subprocess.Popen(["tcpdump", "-i", "wlan0", "-w", series_dir])

time.sleep(4)

subprocess.Popen.kill(tcpdmp)

#test2
#also works
series_dir = "./runname/first/test5.pcap"
print "will it work again?"+ series_dir
tcpdmp = subprocess.Popen(["tcpdump", "-i", "wlan0", "-w", series_dir])

time.sleep(4)

subprocess.Popen.kill(tcpdmp)


#this does not.
#looks like the file path needs to be built outside the subprocess call.


series_dir2 = "./runname/first/"
print "this doesnt"+ series_dir2

tcpdmp = subprocess.Popen(["tcpdump", "-i", "wlan0", "-w", series_dir2 + "/test6.pcap"])

time.sleep(4)

subprocess.Popen.kill(tcpdmp)
