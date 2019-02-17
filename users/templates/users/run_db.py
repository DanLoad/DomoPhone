from users.settings import *
from users.models import *
from own.models import *
import time

def RunStart(iuser, module, status, istep):
    run = Status.objects.get(comand = "run")
    user = Contact.objects.get(id = iuser)
    run.module = module
    run.user = user
    run.time = time.time()
    run.status = status
    run.step = step
    run.number = " "
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
    return run.module == module and run.status == status and run.step == step


def RunSave(modules, value):
    run = Status.objects.get(comand = "run")
    if (module == "rfid"):
        add = Rfid()
        add.rfid = value
        add.contact = run.contact
        add.save()
        run.status = "save"
        run.save()
    elif (module == "rfup"):
        add = RF()
        add.up = value
        add.contact = run.contact
        add.save()
        run.status = "save"
        run.save()
    elif (module == "rfdown"):
        add = RF()
        add.down = value
        add.contact = run.contact
        add.save()
        run.status = "save"
        run.save()



def RunTime():
    run = Status.objects.get(comand = "run")
    if time.time() > run.time:
        run.status = "time"
        run.save()



def RunCheckValue(module, value):
    run = Status.objects.get(comand = "run")
    if (module == "rfid"):
        list = Rfid.objects.filter(rfid = value)
        quantity = list.count()
        if quantity == 0:
            return True
        else:
            run.print = Run_print("Метка", list)
            run.status = "no"
            run.save()
            return False
    elif (module == "rf"):
        list = RF.objects.filter(up = value).filter(down = value)
        quantity = list.count()
        if quantity == 0:
            return True
        else:
            run.print = Run_print("Брелок", list)
            run.status = "no"
            run.save()
            return False
    elif (module == "finger"):
        return False
    else:
        return False
def RunPrint(name, list):
    str = '<div style=\\"color:red\\">' + name + ': <br/>'+ID+"<br/>Принадлежит:"
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
    run.step = step
    run.save()


def RunAccess(module, value):
    if (module == "rfid"):
        rfids = Rfid.objects.all()
        if any(str(uid) == id.rf for id in rfids):
            return True
        else:
            return False


def RunDelete(module, value):
    if (module == "rfid"):
        rfid = Rfid.objects.get(id = value)
        rfid.delete()

def RunActiv(module, value):
    bool = " "
    if (module == "rfid"):
        bool = Rfid.objects.get(id = value)
    elif (module == "rf"):
        bool = RF.objects.get(id = value)
    elif (module == "finger"):
        bool = Finger.objects.get(id = value)
    if bool.activ:
        bool.activ = False
    else:
        bool.activ = True
    bool.save()
