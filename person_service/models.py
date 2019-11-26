from django.db import models
from django.utils import timezone
import random
from datetime import datetime
from random import randrange
from datetime import timedelta
import requests


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    pesel = models.CharField(max_length=11)
    #pPPP its variable response for 7-10number of pesel
    pPPP=""
    #true means that person is a male
    sex = models.CharField(max_length=1)
    birthday = models.DateTimeField(default=timezone.now())

    # choose which sex is the person
    def _sex_(self):
        rand = random.randint(0, 206)
        while(1):
            Person.pPPP = random.randint(1000,9999)
            assist=int(Person.pPPP)
            if rand < 100:
                Person.sex = 1
                if Person.pPPP%2==1:
                    break

            else:
                Person.sex = 0
                if Person.pPPP % 2 == 0:
                    break

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



    def generating_date(self):
        rand=random.randint(0,3655)
        d1 = datetime.strptime('1/1/1970 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('12/31/1975 4:50 AM', '%m/%d/%Y %I:%M %p')
        if(rand<580):
            #YEARS 1970-1976
            d1 = datetime.strptime('1/1/1970 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/1975 4:50 AM', '%m/%d/%Y %I:%M %p')
        if(rand<1280):
            d1 = datetime.strptime('1/1/1976 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/1981 4:50 AM', '%m/%d/%Y %I:%M %p')
            #YEARS 1976-1982
        if(rand<1930):
            d1 = datetime.strptime('1/1/1982 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/1987 4:50 AM', '%m/%d/%Y %I:%M %p')
            #YEARS 1982-1988
        if(rand<2480):
            d1 = datetime.strptime('1/1/1988 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/1993 4:50 AM', '%m/%d/%Y %I:%M %p')
            #YEARS 1988-1994
        if(rand<2880):
            d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('31/12/1999 4:50 AM', '%m/%d/%Y %I:%M %p')
            #YEARS 1994-2000
        if(rand<3255):
            d1 = datetime.strptime('1/1/2000 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/2005 4:50 AM', '%m/%d/%Y %I:%M %p')
            #YEARS 2000-2006
        if(rand<3655):
            d1 = datetime.strptime('1/1/2006 1:30 PM', '%m/%d/%Y %I:%M %p')
            d2 = datetime.strptime('12/31/2013 4:50 AM', '%m/%d/%Y %I:%M %p')
            #YEARS 2006-2014

        Person.birthday=random_date(d1,d2)

    def __str__(self):
        return self.pesel




