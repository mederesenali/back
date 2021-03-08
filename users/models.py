from django.db import models


class Users(models.Model):
    fio = models.CharField(max_length=70, blank=False, default='')
    phone = models.CharField(max_length=70, blank=False, default='')
    address = models.CharField(max_length=70, blank=False, default='')
    inn = models.CharField(max_length=10, blank=False, default='')

    def __str__(self):
        return self.fio
