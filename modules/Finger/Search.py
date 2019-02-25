#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import serial
import hashlib
import logging
from pyfingerprint.pyfingerprint import PyFingerprint
from modules.Finger.Add import *
from settings.models import *
from users.templates.users.run_db import *


## Поиск пальца
##

## Инициализация датчика
def Read_finger(uart):
    logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

    if RunCheckStatus("finger", "rec", "one"):
        Add_finger(uart)
    elif RunCheckStatus("finger", "delete", "delete"):
        Delete_finger(uart)
    else:
        Check_finger(uart)


def Check_finger(uart):
    try:
        ## Ждет пока не прочитает палец
        if uart.readImage() == True:

            ## Преобразует изображение и сохраняет в буфер №1
            uart.convertImage(0x01)

            ## Ищет шаблон
            result = uart.searchTemplate()

            positionNumber = result[0]
            accuracyScore = result[1]

            if not positionNumber == -1:

                logging.info('Найден шаблон в позиции #' + str(positionNumber))
                logging.info('Оценка точности: ' + str(accuracyScore))

                ## Загружает найденый шаблон в буфер №1
                uart.loadTemplate(positionNumber, 0x01)

                ## Скачивает характеристики шаблона, загруженного в charbuffer 1
                characterics = str(uart.downloadCharacteristics(0x01)).encode('utf-8')

                ## Хеширует характеристики шаблона
                logging.info('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())
                logging.info("open door>>>>>>>>>>>>>")
            else:
                logging.info('Совпадение не найдено!')


    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))

def Delete_finger(uart):
    run = Status.objects.get(comand = "run")
    number = int(run.number)
    if number >= 0:
        if ( uart.deleteTemplate(number) == True ):
                 RunDelete("finger", number)
                 RunChangeStatus("delete", "ok")
