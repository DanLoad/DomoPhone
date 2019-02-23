#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import time
#import binascii
import logging
from own.models import *
#from settings.models import *
#from users.models import *
from users.templates.users.run_db import *
import re

timePause = 0;

def Read_uid(uart):
    logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )
    if uart.isOpen():
        if uart.inWaiting() > 0:
            value = ""
            try:
                read_byte = uart.read()
            except:
                read_byte = "?"
            # logging.info("redb >>>>>>>>>>")
            # logging.info(read_byte)
            # logging.info("redb >>>>>>>>>>")
            if read_byte == b'\x02':
                for Counter in range(12):
                    try:
                        read_add = uart.read()
                    except:
                        read_add = "?"
                        break
                    value = value + read_add.decode('utf8')
                logging.info(value)
                if re.match("^[A-Za-z0-9]*$", value):
                    # logging.info(RunCheckStatus("rfid", "rec", "no"))
                    global timePause
                    if RunCheckStatus("rfid", "rec", "no"):
                        # logging.info(RunCheckValue("rfid", value))
                        if RunCheckValue("rfid", value):
                            RunSave("rfid", value)
                    elif time.time() > timePause:
                        if RunAccess("rfid", value):
                            logging.info("Open door >>>>>>>>>>")
                            timePause = time.time() + 1
                        else:
                            logging.info("no open door >>>>>>>>>>>")
                    else:
                        uart.flushInput()
                else:
                    uart.flushInput()
