import time
from settings.models import *
from own.models import *

def Find_place():
    finger = Finger.objects.all()
    for place in range(6):
        if not(any(place == id.number for id in finger)):
            print(">>>>>>>>>>>>")
            return place
    return -1

def Check_status(var):
    status = My_variable.objects.get(name = "finger_status")
    return (status.value == var)

def Save_finger(contact, place):
    Save_finger = Finger()
    Save_finger.contact = contact
    Save_finger.number = place
    Save_finger.finger = "Information"
    Save_finger.save()
    return True

def User_id():
    user = My_variable.objects.get(name = "finger_user")
    return Contact.objects.get(id = user.value)

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
