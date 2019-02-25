#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import signal
import sys
import time
import logging
from own.models import *
from settings.models import *
from users.templates.users.run_db import *

from rpi_rf import RFDevice

rfdevice = None


def RF_run():
    logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )


    parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
    parser.add_argument('-g', dest='gpio', type=int, default=4,
                        help="GPIO pin (Default: 4)")
    args = parser.parse_args([])

    signal.signal(signal.SIGINT, exithandler)
    rfdevice = RFDevice(args.gpio)
    rfdevice.enable_rx()
    timestamp = None
    logging.info("Listening for codes on GPIO " + str(args.gpio))

    while True:
        if rfdevice.rx_code_timestamp != timestamp:
            timestamp = rfdevice.rx_code_timestamp
            if rfdevice.rx_code > 100000:


                if RunCheckStatus("rf", "up", "no"):
                    RF_rec("up", rfdevice.rx_code, rfdevice.rx_pulselength, rfdevice.rx_proto)
                elif RunCheckStatus("rf", "down", "no"):
                    RF_rec("down", rfdevice.rx_code, rfdevice.rx_pulselength, rfdevice.rx_proto)
                elif RunCheckStatus("rf", "open", "no"):
                    pass
                else:
                    RF_read(rfdevice.rx_code, rfdevice.rx_pulselength, rfdevice.rx_proto)
                    logging.info("Чтение")
                    logging.info(str(rfdevice.rx_code) +
                                 " [pulselength " + str(rfdevice.rx_pulselength) +
                                 ", protocol " + str(rfdevice.rx_proto) + "]")
        time.sleep(0.01)
    rfdevice.cleanup()


# pylint: disable=unused-argument
def exithandler(signal, frame):
    rfdevice.cleanup()



def RF_rec(cnob, code, pulse, proto):
    logging.info("Запись")
    if cnob == "up":
        if RunCheckValue("rfup", code):
            RunSave("up", code)
    elif cnob == "down":
        if RunCheckValue("rfdown", code):
            RunSave("down", code)


def RF_read(code, pulse, proto):
    if RunAccess("rf", code):
        logging.info("Open door >>>>>>>>>>>>")
    else:
        logging.info("no open door >>>>>>>>>>>")
