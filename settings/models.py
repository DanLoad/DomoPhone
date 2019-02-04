from django.db import models

class My_variable(models.Model):
    name = models.CharField(max_length = 15)
    value = models.CharField(max_length = 15)

    def __str__(self):
        return "%s %s" % (self.name, self.value)
