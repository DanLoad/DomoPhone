from django.contrib import admin
from .models import *

class AdminVariable (admin.ModelAdmin):
    list_display = ["name","value"]
    class Meta:
        model = My_variable

admin.site.register(My_variable, AdminVariable)



class AdminStatus (admin.ModelAdmin):
    list_display = ["comand","module","user","status","step","time","number","up","down","print"]
    class Meta:
        model = Status

admin.site.register(Status, AdminStatus)
