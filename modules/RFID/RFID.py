#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time
import binascii
from own.models import *
from settings.models import *
from users.models import *

Tag1 = str('22009C45F40F')
uart = serial.Serial("/dev/ttyS2", baudrate=9600, timeout=3000)
Delay_read = 0
activ_add_uid = False

def Read_uid():
    status = My_variable.objects.get(name = "add_new_rfid")
    if status.value == "add":
        print ("okkk")
        val = My_variable.objects.get(name = "user")
        print ("okkk2")
        contact = Contact.objects.get(id = val.value)
        print ("okkk3")
        Delay_read = time.time() + 5
        while status.value == "add":
            if time.time() > Delay_read:
                status.value = "time"
                status.save()
            print (">>>")
            if uart.inWaiting() > 0:
                ID = ""
                read_byte = uart.read()
                print (read_byte)
                if read_byte == b'\x02':
                    for Counter in range(12):
                        read_byte=uart.read()
                        ID = ID + read_byte.decode('utf8')
                        print (read_byte.decode('utf8'))

                    add_uid = Rrfid()
                    add_uid.rfid = ID
                    add_uid.contact = contact
                    add_uid.save()
                    status.value = "add_rfid"
                    status.save()
    else:
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

                    status = My_variable.objects.get(name = "add_new_rfid")
                    status.value = ID
                    status.save()
                    
                    if ID == Tag1:
                        print ("matched")
                    else:
                        print ("Access Denied")
                        uart.flushInput()
                    Delay_read = time.time() + 3
        else:
            uart.flushInput()
