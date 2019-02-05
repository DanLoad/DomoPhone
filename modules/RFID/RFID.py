
import serial
import time
import binascii
from own.models import *
from settings.models import *
from users.models import *
import re

Tag1 = str('22009C45F40F')
uart = serial.Serial("/dev/ttyS2", baudrate=9600, timeout=3000)
Delay_read = 0
activ_add_uid = False

def Read_uid():
    if uart.isOpen():
        status = My_variable.objects.get(name = "add_new_rfid")
        if status.value == "add":
            print ("add")
            uart.flushInput()
            Delay_add = time.time() + 10
            find = status.value
            while find == "add":
                if uart.inWaiting() > 0:
                    ID = ""
                    try:
                        read_add = uart.read()
                    except:
                        read_add = "?"
                        break

                    print (read_add)
                    if read_add == b'\x02':
                        for Counter in range(12):
                            try:
                                read_add = uart.read()
                            except:
                                ID = "?"
                                break
                            ID = ID + read_add.decode()
                            print (read_add.decode())

                        if re.match("^[A-Za-z0-9]*$", ID):
                            add_uid = Rfid()
                            dis = My_variable.objects.get(name = "user")
                            contact = Contact.objects.get(id = dis.value)
                            dis = " "
                            add_uid.rfid = ID
                            add_uid.contact = contact
                            add_uid.save()
                            print (">>>>>>>>>>>>>>>+++++++")
                            status.value = "add_rfid"
                            find = "add_rfid"
                            print (find)
                            status.save()
                            uart.flushInput()

                if time.time() > Delay_add:
                    status.value = "time"
                    status.save()
        else:
            global Delay_read
            if time.time() > Delay_read:
                if uart.inWaiting() > 0:
                    ID = ""
                    try:
                        read_byte = uart.read()
                    except:
                        read_byte = "?"

                    if read_byte == b'\x02':
                        for Counter in range(12):
                            try:
                                read_add = uart.read()
                            except:
                                ID = "?"
                                break
                            ID = ID + read_byte.decode('utf8')
                            print (read_byte.decode('utf8'))
                        print (ID)
                        if re.match("^[A-Za-z0-9]*$", ID):
                            #status = My_variable.objects.get(name = "add_new_rfid")
                            #status.value = ID
                            #status.save()
                            print("open door>>>>>>>>>>>>>")
                        else:
                            uart.flushInput()
                        Delay_read = time.time() + 3
            else:
                uart.flushInput()
