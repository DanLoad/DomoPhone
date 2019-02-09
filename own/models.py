from django.db import models
from users.models import Contact

class Rfid(models.Model):
    contact = models.ForeignKey(Contact, blank=True, null=True, default=None, on_delete=models.CASCADE)
    rfid = models.CharField(max_length = 15)
    activ = models.BooleanField(default=True)

    def __str__(self):
        return str(self.contact.id)


class RF(models.Model):
    contact = models.ForeignKey(Contact, blank=True, null=True, default=None, on_delete=models.CASCADE)
    rf = models.CharField(max_length = 15)
    activ = models.BooleanField(default=True)

    def __str__(self):
        return str(self.contact.id)


class Finger(models.Model):
    contact = models.ForeignKey(Contact, blank=True, null=True, default=None, on_delete=models.CASCADE)
    number = models.DecimalField(blank=True, default=0, max_digits=15, decimal_places=0)
    finger = models.CharField(max_length = 15)
    activ = models.BooleanField(default=True)

    def __str__(self):
        return str(self.contact.id)
