from django.contrib import admin
from own.models import Rfid, RF, Finger



class AdminRfid (admin.ModelAdmin):
    list_display = ["contact","rfid","activ"]
    list_filter = ['contact']

    class Meta:
        model = Rfid

admin.site.register(Rfid, AdminRfid)


class AdminRF (admin.ModelAdmin):
    list_display = ["contact","rf","activ"]
    list_filter = ['contact']

    class Meta:
        model = RF

admin.site.register(RF, AdminRF)


class AdminFinger (admin.ModelAdmin):
    list_display = ["contact","number","finger","activ"]
    list_filter = ['contact']

    class Meta:
        model = Finger

admin.site.register(Finger, AdminFinger)
