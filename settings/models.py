from django.db import models
from users.models import Contact

class My_variable(models.Model):
    name = models.CharField(max_length = 15)
    value = models.CharField(max_length = 100)

    def __str__(self):
        return "%s %s" % (self.name, self.value)

class Status(models.Model):
    comand = models.CharField(max_length = 10)
    module = models.CharField(max_length = 10)
    user = models.ForeignKey(Contact, blank=True, null=True, default=None, on_delete=models.CASCADE)
    status = models.CharField(max_length = 10)
    step = models.CharField(blank=True, max_length = 10)
    time = models.DecimalField(blank=True, default=0, max_digits=20, decimal_places=0)
    number = models.CharField(blank=True, default=" ", max_length = 20)
    up = models.DecimalField(blank=True, default=0, max_digits=15, decimal_places=0)
    down = models.DecimalField(blank=True, default=0, max_digits=15, decimal_places=0)
    print = models.TextField(blank=True, default=" ")

    def __str__(self):
        return "%s %s" % (self.comand, self.module)
