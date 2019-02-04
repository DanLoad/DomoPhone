from django.shortcuts import render
from django.http import HttpResponse
from users.models import *
from own.models import *
from users.settings import *
from settings.models import *

# Create your views here.
def index(request):
    if not request.GET:
        contact = Contact.objects.all()
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

    elif request.GET and "add" == request.GET["cmd"]:
        user = request.GET["user"]
        user = user[5:]

        contact = Contact.objects.get(id = user)
        rfid = Rfid.objects.filter(contact = user)
        rf = RF.objects.filter(contact = user)
        finger = Finger.objects.filter(contact = user)
        status = My_variable.objects.get(name = "add_new_rfid")
        status.value = "add"
        status.save()
        user_rfid = My_variable.objects.get(name = "user")
        user_rfid.value = user
        user_rfid.save()
        while status.value == "add":
            rdd = 0

        return render(request, 'users/includes/own_user.html', locals())
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
    else:
        pass
