from django.http import HttpResponse, JsonResponse
from django.views import View
from person.models import Person
from datetime import datetime
from random import randrange
from datetime import timedelta
import random


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def generating_date():
    rand = random.randint(0, 3655)
    d1 = datetime.strptime('1/1/1970 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('12/31/1975 4:50 AM', '%m/%d/%Y %I:%M %p')
    #TODO Mozna dodawac wiecej lat
    if (0 < rand < 580):
        # YEARS 1970-1976
        d1 = datetime.strptime('1/1/1970 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('12/31/1975 4:50 AM', '%m/%d/%Y %I:%M %p')
    if (580 < rand < 1280):
        d1 = datetime.strptime('1/1/1976 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('12/31/1981 4:50 AM', '%m/%d/%Y %I:%M %p')
        # YEARS 1976-1982
    if (1280 < rand < 1930):
        d1 = datetime.strptime('1/1/1982 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('12/31/1987 4:50 AM', '%m/%d/%Y %I:%M %p')
        # YEARS 1982-1988
    if (1930 < rand < 2480):
        d1 = datetime.strptime('1/1/1988 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('12/31/1993 4:50 AM', '%m/%d/%Y %I:%M %p')
        # YEARS 1988-1994
    if (2480 < rand < 2880):
        d1 = datetime.strptime('1/1/1994 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('12/31/1999 4:50 AM', '%m/%d/%Y %I:%M %p')
        # YEARS 1994-2000
    if (2880 < rand < 3255):
        d1 = datetime.strptime('1/1/2000 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('12/31/2005 4:50 AM', '%m/%d/%Y %I:%M %p')
        # YEARS 2000-2006
    if (3255 < rand < 3655):
        d1 = datetime.strptime('1/1/2006 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('12/31/2013 4:50 AM', '%m/%d/%Y %I:%M %p')
        # YEARS 2006-2014

    date = random_date(d1, d2)
    #TODO TUTAJ MOZE SIE WYWALAC BO TO MA JESZCZE CZAS TA DATE, 
    Person.birthday = date
    return date

    # choose which sex is the person
def _sex_(self,Person):
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
def _name_(self,Person):
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
def _surname_(self,Person):
    #creating variable
    samogloski=["a","e","i","o","u","y"]
    spolgloski=["b", "c", "d", " g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "y", "z", "rz", "ch"]
    koncowki_meskie=["ski","cki","dzki","ak","ek","ik","yk","ki","owicz","eowicz"]
    koncowki_zenskie = ["ska", "cka", "dzka", "ak", "ek", "ik", "yk", "ka", "owicz", "eowicz"]
    surname=""
    #generating the first 2 letters of surname
    #TODO Niektore koncowki troche sie gryza z samogloska
    surname=spolgloski[random.randint(0,len(spolgloski-1))]+samogloski[random.randint(0,len(samogloski-1))]
    #adding "koncowka" basic on sex
    if(Person.sex==1):
        surname=surname+koncowki_meskie
    else:
        surname=surname+koncowki_zenskie
    Person.surname=surname


def generatingPesel(self,Person):
    #this is very stupid way but i need this date to pesel
    data=Person.generating_date(Person)

    if(1900<data.year<2000):
        # adding year to pesel
        Person.pesel = Person.pesel + str(data.year%1900)
        # adding month to pesel
        month=80
        month=month+data.month
        Person.pesel=Person.pesel+str(month)
    elif 1999<data.year<3000:
        # adding year to pesel
        Person.pesel = Person.pesel + str(data.year%2000)
        # adding month to pesel
        month=0
        month=month+data.month
        #if month will be smaller than <10
        if(month<10):
            Person.pesel = Person.pesel + str(0)
        else:
            Person.pesel=Person.pesel+str(month)

    #adding day to pesel
    if(data.day<10):
        Person.pesel[4]='0'
        Person.pesel[5]=data.day
    else:
        Person.pesel=Person.pesel+str(data.day)
    Person.pesel=Person.pesel+Person.pPPP
    #1-3-7-9-1-3-7-9-1-3
    #creating "Suma kontrolna"
    Suma_kontrolna=int(Person.pesel[0])*1+int(Person.pesel[1])*3+int(Person.pesel[2])*7+int(Person.pesel[3])*9
    Suma_kontrolna=Suma_kontrolna+int(Person.pesel[4]) * 1+int(Person.pesel[5])*3+int(Person.pesel[6])*7+int(Person.pesel[7])*9+int(Person.pesel[8])*1+int(Person.pesel[9])*3
    if(Suma_kontrolna>10):
        Suma_kontrolna=10-Suma_kontrolna%10
    else:
        Suma_kontrolna=10-Suma_kontrolna
    Person.pesel=Person.pesel+str(Suma_kontrolna)


class PersonView(View):

    def get(self, request):
        """
        Http get method to get all persons or person with given pesel
        Example url to get person by pesel: localhost:8000/person/12345678901
        :param request: has string parameter pesel
        :return: JSON response
        """
        pesel = request.GET.get('pesel')
        if pesel:
            person = list(Person.objects.filter(pesel=pesel).values())[0] #TODO exception if more than one
            return JsonResponse(person, safe=False)
        else:
            person_list = list(Person.objects.all().values())
            return JsonResponse(person_list, safe=False)

    def post(self, request, number=1):
        for i in range(0, number):
            #creating new object
            Person=Person
            _sex_(Person)
            _name_(Person)
            _surname_(Person)
            generatingPesel(Person)

            # TODO: put here generate
            pass
        return HttpResponse(status=201)

    def save_person(self, name, surname, pesel, sex, birthday):
        """
        Saves person to database
        """
        person = Person()
        person.name = name
        person.surname = surname
        person.pesel = pesel
        person.sex = sex
        person.birthday = birthday
        person.save()