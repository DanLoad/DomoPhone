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


## Добавляет новый палец
##
def Add_finger(status, uart):
    ## Пытается зарегестрировать палец
    try:
        print('Прикладите палец...')

        ## Ждать пока не прочитается палец
        if uart.readImage() == True:

            ## Преобразует изображение и сохраняет в буфер №1
            uart.convertImage(0x01)

            ## Проверяет, зарегистрирован ли палец
            result = uart.searchTemplate()
            positionNumber = result[0]

            if not positionNumber >= 0:
                print('Уберите палец...')
                time.sleep(2)

                print('Снова прикладите палец...')

                ## Ждет пока снова не прочитает палец
                while ( uart.readImage() == False ):
                    pass

                ## Преобразует изображение и сохраняет в буфер №2
                uart.convertImage(0x02)

                ## Сравнивает из двух буферов
                if ( uart.compareCharacteristics() == 0 ):
                    raise Exception('Пальцы не совпадают')

                ## Создает шаблон
                uart.createTemplate()

                ## Сохраняет шаблон
                positionNumber = f.storeTemplate(1)
                print('Палец успешно зарегистрирован!')
                print('Новая позиция шаблона #' + str(positionNumber))
                exit(0)
            else:
                print('Шаблон уже существует в позиции #' + str(positionNumber))
                exit(0)


    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
