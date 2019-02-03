#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time
import binascii

Tag1 = str('22009C45F40F')
uart = serial.Serial("/dev/ttyS2", baudrate=9600, timeout=3000)
Delay_read = 0

def Read_uid():
    global Delay_read
    if time.time() > Delay_read:
        if uart.inWaiting() > 0:
            ID = ""
            read_byte = uart.read()
            print (read_byte)
            if read_byte == b'\x02':
                for Counter in range(12):
                    read_byte=uart.read()
                    ID = ID + read_byte.decode('utf8')
                    print (read_byte.decode('utf8'))
                print (ID)
                if ID == Tag1:
                    print ("matched")
                else:
                    print ("Access Denied")
                    uart.flushInput()
                Delay_read = time.time() + 3
    else:
        uart.flushInput()
