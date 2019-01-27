from django.shortcuts import render
from users.models import *
from own.models import *

# Create your views here.
def index(request):
    contact = Contact.objects.all()
    return render(request, 'users/users.html', locals())

def user_owned(request):
    if request.GET and "user" == request.GET["cmd"]:
        index = request.GET["index"]
        index = index[5:]

        contact = Contact.objects.get(id = index)
        rfid = Rfid.objects.filter(id = index)
        rf = RF.objects.filter(id = index)
        finger = Finger.objects.filter(id = index)

        return render(request, 'users/includes/own_user.html', locals())
    else:
        pass







def rfid_owned(request):
    if request.GET and "all" == request.GET["cmd"]:
        contact = Contact.objects.filter()
        rfid = Rfid.objects.filter()
        rf = RF.objects.filter()
        finger = Finger.objects.filter()

        return render(request, 'users/includes/info_all.html', locals())
    else:
        pass
