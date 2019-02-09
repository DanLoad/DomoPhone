from django.shortcuts import render
from django.http import HttpResponse
from users.models import *
from own.models import *
from users.settings import *
from settings.models import *
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

def rfid_owned(request):

    if request.GET and "delete" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[5:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        del_rfid = Rfid.objects.get(id = index)
        del_rfid.delete()

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "activ" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[11:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        rfid_id = Rfid.objects.get(id = index)
        if rfid_id.activ:
            rfid_id.activ = False
        else:
            rfid_id.activ = True
        rfid_id.save()

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "add_start" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]

        user_rfid = My_variable.objects.get(name = "rfid_user")
        user_rfid.value = user
        user_rfid.save()
        status = My_variable.objects.get(name = "rfid_status")
        status.value = "add"
        status.save()
        return HttpResponse("Поднесите RFID метку к считывателю")

    elif request.GET and "add_check" == request.GET["cmd"]:
        info = My_variable.objects.get(name = "rfid_print")
        status = My_variable.objects.get(name = "rfid_status")
        if status.value == "add":
            #return json.dumps({'cmd': "add"})
            return HttpResponse('{"cmd": "add"}')
            #return HttpResponse("add")
        elif status.value == "add_no":
            My_variable.objects.get(name = "rfid_print")
            #return json.dumps({'cmd': "add_no", 'data': info.value})
            #HttpResponse(My_variable.objects.get(name = "print"))
            return HttpResponse('{"cmd": "add_no", "data": "' + info.value + '"}')
        else:
            user = request.GET["user"]
            user = user[5:]

            contact = Contact.objects.get(id = user)
            rfid = Rfid.objects.filter(contact = user)
            rf = RF.objects.filter(contact = user)
            finger = Finger.objects.filter(contact = user)

            #return render(request, 'users/includes/own_user.html', locals())
            return HttpResponse('{"cmd": "add_off"}')

    else:
        pass

def rf_owned(request):
    if request.GET and "delete" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[3:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        del_rf = RF.objects.get(id = index)
        del_rf.delete()

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "activ" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[9:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        rf_id = RF.objects.get(id = index)
        if rf_id.activ:
            rf_id.activ = False
        else:
            rf_id.activ = True
        rf_id.save()

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "add" == request.GET["cmd"]:
        user = request.GET["user"]
        mom = request.session.get('num')
        return HttpResponse(mom)
    else:
        pass

def finger_owned(request):
    if request.GET and "delete" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[7:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        del_finger = Finger.objects.get(id = index)
        del_finger.delete()

        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "activ" == request.GET["cmd"]:
        user = request.GET["user"]
        index = request.GET["index"]
        user = user[5:]
        index = index[13:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        finger_id = Finger.objects.get(id = index)
        if finger_id.activ:
            finger_id.activ = False
        else:
            finger_id.activ = True
        finger_id.save()
        return render(request, 'users/includes/own_user.html', locals())

    elif request.GET and "add_start" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]

        user_finger = My_variable.objects.get(name = "finger_user")
        user_finger.value = user
        user_finger.save()
        step = My_variable.objects.get(name = "finger_info")
        step.value = "wait_1"
        step.save()
        status = My_variable.objects.get(name = "finger_status")
        status.value = "add"
        status.save()

        return HttpResponse("Подождите...")

    elif request.GET and "add_check" == request.GET["cmd"]:
        info = My_variable.objects.get(name = "finger_print")
        status = My_variable.objects.get(name = "finger_status")
        step = My_variable.objects.get(name = "finger_info")
        if status.value == "add":
            if step.value == "wait":
                return HttpResponse('{"cmd":"add", "step": "wait", "data": "Подождите..."}')
            elif step.value == "wait_1":
                return HttpResponse('{"cmd":"add", "step": "wait_1", "data": "Прикладите палец"}')
            elif step.value == "remove":
                return HttpResponse('{"cmd":"add", "step": "remove", "data": "Уберите палец"}')
            elif step.value == "wait_2":
                return HttpResponse('{"cmd":"add", "step": "wait_2", "data": "Сново прикладите палец"}')
        elif status.value == "no":
            if step.value == "exists":
                return HttpResponse('{"cmd":"add", "step": "exists", "data": "Этот палец существует"}')
            elif step.value == "not_match":
                return HttpResponse('{"cmd":"add", "step": "not_match", "data": "Пальци не совпадают"}')
            elif step.value == "add":
                return HttpResponse('{"cmd":"add", "step": "add", "data": "Палец добавлен"}')
        else:
            user = request.GET["user"]
            user = user[5:]

            contact = Contact.objects.get(id = user)
            rfid = Rfid.objects.filter(contact = user)
            rf = RF.objects.filter(contact = user)
            finger = Finger.objects.filter(contact = user)
            return HttpResponse('{"cmd": "add_off"}')


    elif request.GET and "add_cancel" == request.GET["cmd"]:
        status = My_variable.objects.get(name = "finger_status")
        step = My_variable.objects.get(name = "finger_info")
        status.value = "no"
        status.save()
        step.value = "cancel"
        step.save()
        user = request.GET["user"]
        user = user[5:]
        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)

        return render(request, 'users/includes/own_user.html', locals())


    else:
        pass
