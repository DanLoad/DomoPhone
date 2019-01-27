from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 15)
    firstname = models.CharField(max_length = 15)
    lastname = models.CharField(max_length = 15)
    birthday = models.DateField()
    email = models.EmailField(blank=True, null=True, default=None)
    phone = models.DecimalField(blank=True, default=0, max_digits=15, decimal_places=0)
    activ = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.name, self.firstname)
