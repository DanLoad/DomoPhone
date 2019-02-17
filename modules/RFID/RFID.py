import serial
import time
#import binascii
#import logging
from own.models import *
#from settings.models import *
#from users.models import *
from users.template.users.run_db import *
import re


def Read_uid(uart):
    if uart.isOpen():
        if uart.inWaiting() > 0:
            value = ""
            try:
                read_byte = uart.read()
            except:
                read_byte = "?"

            if read_byte == b'\x02':
                for Counter in range(12):
                    try:
                        read_add = uart.read()
                    except:
                        value = "?"
                        break
                    value = value + read_byte.decode('utf8')
                    print (read_byte.decode('utf8'))
                print (value)
                if re.match("^[A-Za-z0-9]*$", value):
                    if RunCheckStatus("rfid", "rec", "no"):
                        if RunCheckValue("rfid", value):
                            RunSave("rfid", value)
                        else:
                            break
                    else:
                        if RunAccess("rfid", value):
                            logging.info("Open door >>>>>>>>>>")
                        else:
                            logging.info("no open door >>>>>>>>>>>")
                else:
                    uart.flushInput()
