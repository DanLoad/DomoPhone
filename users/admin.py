from django.contrib import admin
from own.models import Rfid, RF, Finger
from users.models import Contact

class RfidInline(admin.TabularInline):
    model = Rfid
    extra = 0

class RFInline(admin.TabularInline):
    model = RF
    extra = 0

class FingerInline(admin.TabularInline):
    model = Finger
    extra = 0

class AdminContact (admin.ModelAdmin):
    list_display = ["name","firstname","lastname", "activ", "email"]
    inlines = [RfidInline, RFInline, FingerInline]

    class Meta:
        model = Contact


admin.site.register(Contact, AdminContact)
