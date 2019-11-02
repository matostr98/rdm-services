from django.db import models
from django.utils import timezone
import random
import requests

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    pesel = models.CharField(max_length=11)
    #true means that person is a male
    sex = models.CharField(max_length=1)
    birthday = models.DateTimeField(default=timezone.now())

    # choose which sex is the person
    def _sex_(self):
        rand = random.randint(0, 206)
        if rand < 100:
            Person.sex = 1;
        else:
            Person.sex = 0;
    #generating name
    def _name_(self):
        names = []
        if (Person.sex == 1):
            file = open('mens_name.txt')
        else:
            file = open('girls_name.txt')
        for a in file.readlines():
            names.extend(a)

        rand = random.randint(0, len(names) - 1)
        Person.name = names[rand]

    #generating surname
    def _surname_(self):
        surname_1=[]
        surname_2=[]
        file = open('surname_1.txt')
        for a in file.readlines():
            surname_1.extend(a)
        if (Person.sex == 1):
            file = open('surname_1_men.txt')
        else:
            file = open('surname_1_girl.txt')
        for a in file.readlines():
            surname_2.extend(a)
        rand1=random.randint(0,len(surname_1))
        rand2=random.randint(0,len(surname_2))
        Person.surname=rand1+rand2



    def __str__(self):
        return self.pesel




