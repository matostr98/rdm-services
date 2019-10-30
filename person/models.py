from datetime import datetime

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    pesel = models.CharField(max_length=11)
    sex = models.CharField(max_length=1)
    birthday = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name + " " + self.surname + " " + self.pesel + " " + self.sex

    class Meta:
        db_table = "peselgen_person"