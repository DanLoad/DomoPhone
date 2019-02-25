#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import time
import logging
from pyfingerprint.pyfingerprint import PyFingerprint
from settings.models import *
from own.models import *
from users.templates.users.run_db import *

## Добавляет новый палец
##
def Add_finger(uart):

    def Read_uid(uart):
        logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                            format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

    print('Currently used templates: ' + str(uart.getTemplateCount()) +'/'+ str(uart.getStorageCapacity()))

    try:
        place = RunFree()
        if not place == "full":
            RunChangeStep("one")
            while RunCheckStatus("finger", "rec", "one"):
                if uart.readImage():
                    uart.convertImage(0x01)
                    result = uart.searchTemplate()
                    positionNumber = result[0]
                    logging.info("Позиция ..." + str(positionNumber))
                    if positionNumber >= 0:
                        if RunCheckValue("finger", positionNumber):
                            print('Template already exists at position #' + str(positionNumber))
                            logging.info("Такой существует")
                            continue
                        else:
                            if ( uart.deleteTemplate(positionNumber) == True ):
                                RunChangeStatus("rec", "one")
                                logging.info("Сначало удалил и...")
                                continue
                            else:
                                RunChangeStatus("no", "error")
                                continue

                    RunChangeStep("remove")
                    logging.info('Remove finger...')
                    time.sleep(2)

                    logging.info('Waiting for same finger again...')
                    RunChangeStep("two")

            while RunCheckStatus("finger", "rec", "two"):
                if uart.readImage():
                    uart.convertImage(0x02)

                    if ( uart.compareCharacteristics() == 0 ):
                        RunChangeStatus("no", "not_match")
                        continue
                    else:
                        uart.createTemplate()
                        positionNumber = uart.storeTemplate(place)
                        if positionNumber == place:
                            RunSave("finger", place)
                            logging.info("Палец сохранен в " + str(place))
                        else:
                            RunChangeStatus("no", "error")
        else:
            RunChangeStatus("no", "full")

    except Exception as e:
        RunChangeStatus("no", "error")
        logging.info('Operation failed!')
        logging.info('Exception message: ' + str(e))
