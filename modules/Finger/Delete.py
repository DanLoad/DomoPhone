#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time
from pyfingerprint.pyfingerprint import PyFingerprint
from settings.models import *
from own.models import *
from modules.Finger.DB import *


def Delete_finger(uart):
    finger_position = My_variable.objects.get(name = "finger_position")

    positionNumber = int(finger_position.value)
    if positionNumber >= 0:
        if ( uart.deleteTemplate(positionNumber) == True ):

                 del_finger = Finger.objects.get(id = positionNumber)
                 del_finger.delete()

                 finger_position.value = -1
                 finger_position.save()
                 Save_status("delete_ok")
