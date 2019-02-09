#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""
import serial
import time
from pyfingerprint.pyfingerprint import PyFingerprint
from settings.models import *

## Добавляет новый палец
##
def Add_finger(uart):
    try:
        Delay_add = time.time() + 5
        ID = ""
        while Check_status("add"):
            Save_step("wait_1")
            while Check_status("add") and Check_step("wait_1"):
                if uart.readImage():
                    uart.convertImage(0x01)
                    result = uart.searchTemplate()
                    positionNumber = result[0]
                    if positionNumber < 0:
                        print('Уберите палец...')
                        Save_step("remove")
                        time.sleep(2)
                        print('Снова прикладите палец...')
                        Save_step("wait_2")
                    else:
                        Save_step("exists")
                        Save_status("no")
                        print('Шаблон уже существует в позиции #' + str(positionNumber))


            while Check_status("add") and Check_step("wait_2"):
                if uart.readImage():
                    uart.convertImage(0x02)
                    if uart.compareCharacteristics() == 0:
                        Save_step("not_match")
                        Save_status("no")
                        print('Пальцы не совпадают')
                    else:
                        uart.createTemplate()
                        positionNumber = uart.storeTemplate(1)
                        Save_step("add")
                        Save_status("no")
                        print('Палец успешно зарегистрирован!')
                        print('Новая позиция шаблона #' + str(positionNumber))



    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)



def Check_status(var):
    status = My_variable.objects.get(name = "finger_status")
    return (status.value == var)

def Check_step(var):
    step = My_variable.objects.get(name = "finger_step")
    return (step.value == var)

def Save_status(value):
    status = My_variable.objects.get(name = "finger_status")
    status.value = value
    status.save()
    return True

def Save_step(value):
    step = My_variable.objects.get(name = "finger_step")
    step.value = value
    step.save()
    return True
