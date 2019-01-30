## -*- coding: utf-8 -*-

import serial
import time

Tag1 = str('2200B8D3C28B')
uart = serial.Serial("/dev/ttyS2", baudrate=9600, timeout=3000)

print ("OK")
while True:
    ID = ""
    read_byte = uart.read()
    if str(read_byte.decode('utf-8')) == '\x02':
        for Counter in range(12):
            read_byte=uart.read()
            ID = ID + str(read_byte.decode('utf-8'))
            #print (read_byte)
        print (ID)
        if ID == Tag1:
            print ("matched")
            time.sleep(5)
        else:
            print ("Access Denied")
            time.sleep(5)
            uart.flushInput()
