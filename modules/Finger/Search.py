#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""
import time
import serial
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
from modules.Finger.Add import *
from settings.models import *


## Поиск пальца
##

## Инициализация датчика
def Read_finger(uart):
    status = My_variable.objects.get(name = "finger_status")
    if status.value == "add":
        Add_finger(uart)
    else:
        Check_finger(uart)



def Check_finger(uart):
    ## Пытается найти палец
    try:
        #print('Waiting for finger...')
        ## Ждет пока не прочитает палец
        if uart.readImage() == True:

            ## Преобразует изображение и сохраняет в буфер №1
            uart.convertImage(0x01)

            ## Ищет шаблон
            result = uart.searchTemplate()

            positionNumber = result[0]
            accuracyScore = result[1]

            if not positionNumber == -1:

                print('Найден шаблон в позиции #' + str(positionNumber))
                print('Оценка точности: ' + str(accuracyScore))

                ## OPTIONAL stuff
                ##

                ## Загружает найденый шаблон в буфер №1
                uart.loadTemplate(positionNumber, 0x01)

                ## Скачивает характеристики шаблона, загруженного в charbuffer 1
                characterics = str(uart.downloadCharacteristics(0x01)).encode('utf-8')

                ## Хеширует характеристики шаблона
                print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())
                print("open door>>>>>>>>>>>>>")
            else:
                print('Совпадение не найдено!')


    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
