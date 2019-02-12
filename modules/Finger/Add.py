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
from own.models import *
from modules.Finger.DB import *

## Добавляет новый палец
##
def Add_finger2(uart):
    try:
        Delay_add = time.time() + 15
        while Check_status("add"):
            Save_step("wait_1")
            while Check_status("add") and Check_step("wait_1"):
                if Delay_add < time.time():
                    Save_step("time")
                    Save_status("no")
                    continue
                if uart.readImage():
                    uart.convertImage(0x01)
                    result = uart.searchTemplate()
                    positionNumber = result[0]
                    if positionNumber > 0:
                        Save_step("exists")
                        Save_status("no")
                        print('Шаблон уже существует в позиции #' + str(positionNumber))

                        # if Finger.objects.filter(number = positionNumber).count() >= 1:
                        #     Save_step("exists")
                        #     Save_status("no")
                        #     print('Шаблон уже существует в позиции #' + str(positionNumber))
                        # else:
                        #     if uart.deleteTemplate(positionNumber):
                        #         print('Уберите палец...')
                        #         Save_step("remove")
                        #         time.sleep(2)
                        #         print('Снова прикладите палец...')
                        #         Save_step("wait_2")
                        #         Delay_add = time.time() + 15
                    else:
                        print('Уберите палец...')
                        Save_step("remove")
                        time.sleep(2)
                        print('Снова прикладите палец...')
                        Save_step("wait_2")
                        Delay_add = time.time() + 15


            while Check_status("add") and Check_step("wait_2"):
                if Delay_add < time.time():
                    Save_step("time")
                    Save_status("no")
                    continue
                if uart.readImage():
                    uart.convertImage(0x02)
                    if uart.compareCharacteristics() == 0:
                        Save_step("not_match")
                        Save_status("no")
                        print('Пальцы не совпадают')
                    else:



                        fin = Finger.objects.all()

                        print(">>>>>>>>>>>>")
                        for place in range(6):
                            if not(any(place == id.number for id in fin)):
                                print(">>>>>>>>>>>>")
                                Save_step("add")
                                Save_status("yes")
                                uart.createTemplate()
                                positionNumber = uart.storeTemplate(place)
                                # if positionNumber == place:
                                #     user = My_variable.objects.get(name = "finger_user")
                                #     contact = Contact.objects.get(id = user.value)
                                #     Save_finger = Finger()
                                #     Save_finger.contact = contact
                                #     Save_finger.number = place
                                #     Save_finger.finger = "Information"
                                #     Save_finger.save()
                                #     print('Палец успешно зарегистрирован!')
                                #     print('Новая позиция шаблона #' + str(positionNumber))
                                #     continue
                        Save_step("full")
                        Save_status("no")



    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        Save_step("error")
        Save_status("no")
        exit(1)


def Add_finger(uart):

    print('Currently used templates: ' + str(uart.getTemplateCount()) +'/'+ str(uart.getStorageCapacity()))

    try:
        Delay_add = time.time() + 15
        place = Find_place()
        if place >= 0:
            Save_step("wait_1")
            while Check_status("add") and Check_step("wait_1"):
                if time.time() > Delay_add:
                    Save_step("time")
                    Save_status("no")
                    continue

                if uart.readImage():
                    uart.convertImage(0x01)

                    result = uart.searchTemplate()
                    positionNumber = result[0]

                    if ( positionNumber >= 0 ):
                        if Finger.objects.filter(number = positionNumber).count() >= 1:
                            Save_step("exists")
                            Save_status("no")
                            print('Template already exists at position #' + str(positionNumber))
                            continue
                        else:
                            if ( uart.deleteTemplate(positionNumber) == True ):
                                Save_step("wait_1")
                                Save_status("add")
                                continue
                            else:
                                Save_step("error")
                                Save_status("no")
                                continue

                    Save_step("remove")
                    print('Remove finger...')
                    time.sleep(2)

                    print('Waiting for same finger again...')
                    Delay_add = time.time() + 15
                    Save_step("wait_2")

            while Check_status("add") and Check_step("wait_2"):
                if time.time() > Delay_add:
                    Save_step("time")
                    Save_status("no")
                    continue

                if uart.readImage():

                    uart.convertImage(0x02)

                    if ( uart.compareCharacteristics() == 0 ):
                        Save_step("not_match")
                        Save_status("no")
                        continue

                    uart.createTemplate()

                    positionNumber = uart.storeTemplate(place)
                    if positionNumber == place:

                        if Save_finger(User_id(), place):
                            Save_step("add")
                            Save_status("yes")
                            print('Палец успешно зарегистрирован!')
                            print('Новая позиция шаблона #' + str(positionNumber))
                    else:
                        Save_step("error")
                        Save_status("no")
        else:
            Save_step("full")
            Save_status("no")

    except Exception as e:
        Save_step("error")
        Save_status("no")
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
