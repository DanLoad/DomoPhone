
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
            Add_uid(status)
        else:
            Check_uid()

#Считывание меток и проверка на разрешение открыть
def Check_uid():
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
                    print("open door>>>>>>>>>>>>>")
                else:
                    uart.flushInput()
                Delay_read = time.time() + 3
    else:
        uart.flushInput()

#Считывание меток и проверка на доступность записи
def Add_uid(status):
    print ("add")
    uart.flushInput()
    Delay_add = time.time() + 5
    ID = ""
    while True:
        if uart.inWaiting() > 0:
            read_add = uart.read()
            if read_add == b'\x02':
                for Counter in range(12):
                    read_add = uart.read()
                    if read_add == b'\x00':
                        ID ="?"
                        continue
                    else:
                        ID = ID + read_add.decode()
                print(ID)
                if re.match("^[A-Za-z0-9]*$", ID):
                    uids = Rfid.objects.filter(rfid = ID)
                    value = uids.count()
                    dis = My_variable.objects.get(name = "user")
                    if value == 0:
                        contact = Contact.objects.get(id = dis.value)
                        add_uid = Rfid()
                        add_uid.rfid = ID
                        add_uid.contact = contact
                        add_uid.save()
                        print (">>>>>>>>>>>>>>>+++++++")
                        print (contact)
                        status.value = "add_rfid"
                        status.save()
                        uart.flushInput()
                        break
                    else:
                        str = "Эта метка принадлежит:"
                        print_info = My_variable.objects.get(name = "print")
                        for uid in uids:
                             str = str + "<br/>" + uid.contact.name + " " + uid.contact.firstname
                        print_info.value = str
                        print_info.save()
                        status.value = "add_no"
                        status.save()
                        break
                else:
                    ID = ""

        if time.time() > Delay_add:
            status.value = "time"
            status.save()
            break
