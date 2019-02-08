from django.contrib import admin
from .models import My_variable

class AdminVariable (admin.ModelAdmin):
    list_display = ["name","value"]
    class Meta:
        model = My_variable

admin.site.register(My_variable, AdminVariable)
