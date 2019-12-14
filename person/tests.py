from django.test import TestCase
from random import randrange
from datetime import timedelta
from datetime import datetime
import random
# Create your tests here.
class person:
    sex=0
    pesel=""

def random_date( start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    data=start+timedelta(seconds=random_second)
    print(str(data.year)+" " +str(data.month)+"  "+ str(data.day))

    print(data.timetz())

    print(data.time())
    return start + timedelta(seconds=random_second)

def _surname_( person):
        # creating variable
        vowel = ["a", "e", "i", "o", "u", "y"]
        consonants = ["b", "c", "d", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "z"]
        male_surname_ends = ["ski", "cki", "dzki", "ak", "ek", "ik", "yk", "ki", "owicz", "eowicz","ewicz","el","ny","uk","in","ny"]
        female_surname_ends = ["ska", "cka", "dzka", "ak", "ek", "ik", "yk", "ka", "owicz", "eowicz","na","ul","uk"]
        surname = ""
        # generating the first 2 letters of surname
        # TODO Niektore koncowki troche sie gryza z samogloska
        surname = consonants[random.randint(0, len(consonants) - 1)].upper() \
                  + vowel[random.randint(0, len(vowel) - 1)] \
        +consonants[random.randint(0, len(consonants) - 1)]
        # adding "koncowka" basic on sex
        if (person.sex == 1):
            surname = surname + male_surname_ends[random.randint(0, len(male_surname_ends) - 1)]
        else:
            surname = surname + female_surname_ends[random.randint(0, len(female_surname_ends) - 1)]
        return surname
def _name_( person):

        if person.sex == 1:
            names = [line.rstrip('\n') for line in open('mens_name.txt', encoding="utf8")]
            #file = open('mens_name.txt', encoding="utf8")
        else:
            names = [line.rstrip('\n') for line in open('girls_name.txt',encoding="utf8")]
           # file = open('girls_name.txt', encoding="utf8")
        #for a in file.readlines():
         #   names.extend(a)
        rand = random.randint(0, len(names) - 1)
        return names[rand]

def generatingPesel( person, pPPP,data):

        print(f"date: {data}")
        if 1900 < data.year < 2000:
            # adding year to pesel
            year = str(data.year % 1900)
            if len(year) != 2:
                year = "0" + year
            print(f"year function: {year}")
            #there was a bug here that the pesel has infinity len
            person.pesel = year
            # adding month to pesel

            month = str(data.month)
            if int(month) <10:
                month = "0" + month
            person.pesel = person.pesel + str(month)
        elif 2000 <= data.year < 2099:
            # adding year to pesel
            year = str(data.year % 2000)
            if data.year == 2000:
                year = "00"
            else:
                if len(year) == 1:
                    year = "0" + year
            print(f"year function: {year}")
            person.pesel = year
            # adding month to pesel
            month = 20
            month = month + data.month

            person.pesel = person.pesel + str(month)
        print(month)
        print("haha")
        print(f"year: {person.pesel}")
        # adding day to pesel
        if data.day < 10:
            day = "0" + str(data.day)
            print(f"small day: {day}")
            person.pesel += day
        else:
            person.pesel = person.pesel + str(data.day)
        print(f"day: {data.day}")
        person.pesel = person.pesel + str(pPPP)
        print(f"pesel: {person.pesel}")
        # 1-3-7-9-1-3-7-9-1-3
        # creating "Suma kontrolna"
        checksum = (int(person.pesel[0]) * 1)%10 + (int(person.pesel[1]) * 3)%10 \
                                  + (int(person.pesel[2]) * 7)%10 + (int(person.pesel[3]) * 9)%10
        checksum = checksum + (int(person.pesel[4]) * 1)%10 + (int(person.pesel[5]) * 3)%10\
                                  + (int(person.pesel[6]) * 7)%10 + (int(person.pesel[7]) * 9)%10 + (int(person.pesel[8]) * 1)%10 + (int(person.pesel[9]) * 3)%10
        checksum = 10 - checksum% 10
        if(len(person.pesel)>=11):
            print("nie dziala")
            return 0
        print("-----------------------")
        return person.pesel + str(checksum)

if __name__ == '__main__':
    d1 = datetime.strptime('1/1/2000 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('12/31/2005 4:50 AM', '%m/%d/%Y %I:%M %p')
    p=person
    #print(random_date(d1,d2))
    for a in range(0,100):
        #print(_surname_(p))
        print(_name_(p)+" "+_surname_(p))
        p.sex=random.randint(0,1)
        print(generatingPesel(p,"0123",random_date(d1,d2)))