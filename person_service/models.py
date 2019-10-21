from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    pesel = models.CharField(max_length=11)
    sex = models.CharField(max_length=1)
    birthday = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.pesel
