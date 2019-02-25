from django.shortcuts import render
from django.http import HttpResponse
from users.models import *
from own.models import *
from users.settings import *
from settings.models import *
from users.templates.users.run_db import *
import json

def index(request):
    if not request.GET:
        contact = Contact.objects.filter()
        rfid = Rfid.objects.filter()
        rf = RF.objects.filter()
        finger = Finger.objects.filter()
        return render(request, 'users/users.html', locals())

def user_owned(request):
    if request.GET and "user" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]
        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        return render(request, 'users/includes/own_user.html', locals())
    else:
        pass

def all_owned(request):
    if request.GET and "all" == request.GET["cmd"]:
        contact = Contact.objects.filter()
        rfid = Rfid.objects.filter()
        rf = RF.objects.filter()
        finger = Finger.objects.filter()

        return render(request, 'users/includes/info_all.html', locals())
    else:
        pass

def Run_rfid(request):
    if request.GET and "start" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]
        RunStart(user, "rfid", "rec", "no")
        return HttpResponse("Поднесите RFID метку к считывателю")
    elif request.GET and "stop" == request.GET["cmd"]:
        RunStop()
        return HttpResponse("Отменено")

    elif request.GET and "delete" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[5:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        RunDelete("rfid", index)

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "activ" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[11:]

        RunActiv("rfid", index)
        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "check" == request.GET["cmd"]:
        status = Status.objects.get(comand = "run")
        if status.status == "rec":
            return HttpResponse('{"cmd": "rec"}')
        elif status.status == "no":
            return HttpResponse('{"cmd": "no", "data": "' + RunRead() + '"}')
        elif status.status == "time":
            return HttpResponse('{"cmd": "time"}')
        elif status.status == "save":
            return HttpResponse('{"cmd": "save"}')
        else:
            return HttpResponse('{"cmd": "xxx"}')

def Run_rf(request):
    if request.GET and "open" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]
        RunStart(user, "rf", "open", "no")
        return HttpResponse("ok")
    elif request.GET and "stop" == request.GET["cmd"]:
        RunStop()
        return HttpResponse("Отменено")
    elif request.GET and "delete" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[3:]

        RunDelete("rf", index)

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        return render(request, 'users/includes/own_user.html', locals())
    elif request.GET and "up" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]
        RunStart(user, "rf", "up", "no")
        return HttpResponse("Нажмите на кнопку брелка рядом с приемником")
    elif request.GET and "down" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]
        RunStart(user, "rf", "down", "no")
        return HttpResponse("Нажмите на кнопку брелка рядом с приемником")
    elif request.GET and "save" == request.GET["cmd"]:
        if RunCheckValue("rf", " "):
            RunSave("rf", " ")
            return HttpResponse("Сохнанино")
        else:
            run = Status.objects.get(comand = "run")
            return HttpResponse(run.print)
    elif request.GET and "activ" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[9:]
        RunActiv("rf", index)
        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)
        return render(request, 'users/includes/own_user.html', locals())
    elif request.GET and "delete" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[3:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        RunDelete("rf", index)

        return render(request, 'users/includes/own_user.html', locals())
    elif request.GET and "check" == request.GET["cmd"]:
        status = Status.objects.get(comand = "run")
        if status.status == "up":
            return HttpResponse('{"cmd": "up"}')
        elif status.status == "down":
            return HttpResponse('{"cmd": "down"}')
        elif status.status == "ok_up":
            return HttpResponse('{"cmd": "ok_up", "data": "' + RunReadId("rf", "up") + '"}')
        elif status.status == "ok_down":
            return HttpResponse('{"cmd": "ok_down", "data": "' + RunReadId("rf", "down") + '"}')
        elif status.status == "no":
            return HttpResponse('{"cmd": "no", "data": "' + RunRead() + '"}')
        elif status.status == "time":
            return HttpResponse('{"cmd": "time"}')
        elif status.status == "save":
            return HttpResponse('{"cmd": "save"}')
        elif status.status == "open":
            return HttpResponse('{"cmd": "wait", "data": "Запишите в 2 параметра"}')
        else:
            return HttpResponse('{"cmd": "xxx"}')

def Run_finger(request):
    if request.GET and "start" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]
        RunStart(user, "finger", "rec", "wait")
        return HttpResponse("Подождите")
    elif request.GET and "stop" == request.GET["cmd"]:
        RunStop()
        return HttpResponse("Отменено")
    elif request.GET and "activ" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[13:]
        RunActiv("finger", index)
        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)
        return render(request, 'users/includes/own_user.html', locals())
    elif request.GET and "delete" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[7:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        RunStart(user, "finger", "delete", "no")
        RunDelete("start", index)

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "check" == request.GET["cmd"]:
        status = Status.objects.get(comand = "run")
        if status.status == "rec":
            return HttpResponse('{"cmd": "rec", "step": "' + status.step + '"}')
        elif status.status == "no":
            return HttpResponse('{"cmd": "no", "step": "' + status.step + '", "data": "' + RunRead() + '"}')
        elif status.status == "time":
            return HttpResponse('{"cmd": "time"}')
        elif status.status == "save":
            return HttpResponse('{"cmd": "save"}')
        elif status.status == "delete":
            if status.step == "delete":
                return HttpResponse('{"cmd": "delete", "step": "delete"}')
            elif status.step == "ok":
                return HttpResponse('{"cmd": "delete", "step": "ok"}')
        else:
            return HttpResponse('{"cmd": "xxx", "???": "' + status.status + '"}')
