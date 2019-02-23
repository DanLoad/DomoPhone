from users.settings import *
from users.models import *
from own.models import *
from settings.models import *
import time

def RunStart(iuser, module, status, step):
    run = Status.objects.get(comand = "run")
    user = Contact.objects.get(id = iuser)
    run.module = module
    run.user = user
    run.time = time.time()
    run.status = status
    run.step = step
    run.number = " "
    if not(status == "up" or status == "down"):
        run.up = 0
        run.down = 0
    run.print = " "
    run.save()


def RunReset():
    run = Status.objects.get(comand = "run")
    run.module = "no"
    run.time = time.time()
    run.status = "no"
    run.step = "no"
    run.number = " "
    run.up = 0
    run.down = 0
    run.print = " "
    run.save()


def RunStop():
    run = Status.objects.get(comand = "run")
    run.status = "stop"
    run.save()

def RunCheckStatus(module, status, step):
    run = Status.objects.get(comand = "run")
    return run.module == module and run.status == status and (run.step == step or run.step == "wait")


def RunSave(module, value):
    run = Status.objects.get(comand = "run")
    if module == "rfid":
        add = Rfid()
        add.rfid = value
        add.contact = run.user
        add.save()
        run.status = "save"
        run.save()
    elif (module == "up"):
        run.up = value
        run.status = "ok_up"
        run.save()
    elif (module == "down"):
        run.down = value
        run.status = "ok_down"
        run.save()
    elif (module == "rf"):
        add = RF()
        add.up = run.up
        add.down = run.down
        add.contact = run.user
        add.save()
        run.status = "save"
        run.save()
    elif (module == "finger"):
        add = Finger()
        add.finger = value
        add.contact = run.user
        add.save()
        run.status = "save"
        run.step = "yes"
        run.save()



def RunTime():
    run = Status.objects.get(comand = "run")
    if time.time() > run.time:
        run.status = "time"
        run.save()



def RunCheckValue(module, value):
    run = Status.objects.get(comand = "run")
    if module == "rfid":
        list = Rfid.objects.filter(rfid = value)
        quantity = list.count()
        if quantity == 0:
            return True
        else:
            run.print = RunPrint("Метка", value, list)
            run.status = "no"
            # run.step = "exists"
            run.save()
            return False
    elif module == "rf":
        list = RF.objects.filter(up = value).filter(down = value)
        quantity = list.count()
        if quantity == 0:
            return True
        else:
            run.print = RunPrint("Брелок", value, list)
            run.status = "no"
            run.save()
            return False
    elif module == "finger":
        list = Finger.objects.filter(number = value)
        quantity = list.count()
        if quantity == 0:
            return True
        else:
            run.print = RunPrint("Номер", value, list)
            run.status = "no"
            run.step = "exists"
            run.save()
            return False
    else:
        return False
def RunPrint(name, value, list):
    str = '<div style=\\"color:red\\">' + name + ': <br/>' + value + "<br/>Принадлежит:"
    for uid in list:
         str = str + "<br/>" + uid.contact.name + " " + uid.contact.firstname
    str = str + "</div>"
    return str



def RunRead():
    run = Status.objects.get(comand = "run")
    return run.print



def RunChangeStatus(status, step):
    run = Status.objects.get(comand = "run")
    run.status = status
    if not status == "not":
        run.step = step
    run.save()

def RunChangeStep(step):
    run = Status.objects.get(comand = "run")
    run.step = step
    run.save()


def RunAccess(module, value):
    if module == "rfid":
        rfids = Rfid.objects.all()
        if any(str(value) == id.rfid for id in rfids):
            return True
        else:
            return False
    elif module == "rf":
        rf = RF.objects.all()
        if any(str(value) == id.up for id in rf):
            return True
        elif any(str(value) == id.down for id in rf):
            return True
        else:
            return False
    else:
        return False


def RunDelete(module, value):
    if (module == "rfid"):
        rfid = Rfid.objects.get(id = value)
        rfid.delete()
    elif (module == "rf"):
        rf = RF.objects.get(id = value)
        rf.delete()

def RunActiv(module, value):
    bool = " "
    if module == "rfid":
        bool = Rfid.objects.get(id = value)
    elif (module == "rf"):
        bool = RF.objects.get(id = value)
    elif module == "finger":
        bool = Finger.objects.get(id = value)
    if bool.activ:
        bool.activ = False
    else:
        bool.activ = True
    bool.save()

def RunFree():
    fin = Finger.objects.all()
    for place in range(6):
        if not(any(place == id.number for id in fin)):
            return place

    return "full"

def RunReadId(module, value):
    if module == "rf":
        run = Status.objects.get(comand = "run")
        if value == "up":
            return str(run.up)
        elif value == "down":
            return str(run.down)
        else:
            return " "
    else:
        return " "
