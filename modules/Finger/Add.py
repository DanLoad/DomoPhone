#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import time
from pyfingerprint.pyfingerprint import PyFingerprint
from settings.models import *
from own.models import *
#from modules.Finger.DB import *

## Добавляет новый палец
##
def Add_finger(uart):

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

                    if positionNumber >= 0:
                        if RunCheckValue("rfid", positionNumber):
                            print('Template already exists at position #' + str(positionNumber))
                            continue
                        else:
                            if ( uart.deleteTemplate(positionNumber) == True ):
                                RunChangeStatus("rec", "one")
                                continue
                            else:
                                RunChangeStatus("no", "error")
                                continue

                    RunChangeStep("remove")
                    print('Remove finger...')
                    time.sleep(2)

                    print('Waiting for same finger again...')
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
                            print('Палец успешно зарегистрирован!')
                            print('Новая позиция шаблона #' + str(positionNumber))
                        else:
                            RunChangeStatus("no", "error")
        else:
            RunChangeStatus("no", "full")

    except Exception as e:
        RunChangeStatus("no", "error")
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
