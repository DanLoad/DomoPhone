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
    info = My_variable.objects.get(name = "finger_info")
    info.value = "wait_1"
    info.save()
    ## Пытается зарегестрировать палец
    try:
        print('Прикладите палец...')
        Delay_add = time.time() + 5
        ID = ""
        status = My_variable.objects.get(name = "finger_status")
            ## Ждать пока не прочитается палец
        print(info.value)
        while status.value == "add" and info.value == "wait_1":
            if uart.readImage() == True:
                ## Преобразует изображение и сохраняет в буфер №1
                uart.convertImage(0x01)

                ## Проверяет, зарегистрирован ли палец
                result = uart.searchTemplate()
                positionNumber = result[0]

                if not positionNumber >= 0:
                    print('Уберите палец...')
                    info.value = "remove"
                    info.save()
                    time.sleep(2)

                    print('Снова прикладите палец...')
                    info.value = "wait_2"
                    info.save()
                else:
                    info.value = "exists"
                    info.save()
                    status.value = "no"
                    status.save()
                    print('Шаблон уже существует в позиции #' + str(positionNumber))


                ## Ждет пока снова не прочитает пале
        while status.value == "add" and info.value == "wait_2":
            if uart.readImage() == True:
                ## Преобразует изображение и сохраняет в буфер №2
                uart.convertImage(0x02)

                ## Сравнивает из двух буферов
                if uart.compareCharacteristics() == 0:
                    info.value = "not_match"
                    info.save()
                    status.value = "no"
                    status.save()
                    print('Пальцы не совпадают')
                else:
                    ## Создает шаблон
                    uart.createTemplate()

                    ## Сохраняет шаблон
                    positionNumber = uart.storeTemplate(1)
                    info.value = "add"
                    info.save()
                    status.value = "no"
                    status.save()
                    print('Палец успешно зарегистрирован!')
                    print('Новая позиция шаблона #' + str(positionNumber))



    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
