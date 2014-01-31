#!/usr/bin/env python

import serial
import threading

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=None)
ser.write("$PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*28\r\n")
ser.write("$PMTK220,200*2C\r\n")

GPS_Data = ''

def readgps():
    global GPS_Data
    while 1:
        current_line = ser.readline()
        if '$GPGGA' in current_line:
            print current_line

def writegps():
    t = threading.Thread(target=readgps)
    t.daemon = True
    t.start()

    while 1:
        if gps_time is not '':
            print gps_time

readgps()
