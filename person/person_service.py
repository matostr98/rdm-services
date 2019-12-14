from datetime import datetime
from random import randrange
from datetime import timedelta
import random

from person.models import Person







class PersonService:

    def generate_person(self):
        person = Person()
        person.sex, pPPP = self._sex_()
        person.name = self._name_(person)
        person.surname = self._surname_(person)
        person.pesel = self.generatingPesel(person, pPPP)
        return person

    def random_date(self, start, end):
        """
        This function will return a random datetime between two datetime
        objects.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    def generating_date(self):
        rand = random.randint(0, 3655)
        d1 = datetime.strptime('1/1/1970 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.strptime('12/31/1975 4:50 AM', '%m/%d/%Y %I:%M %p')
        # TODO Mozna dodawac wiecej lat
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

        date = self.random_date(d1, d2)
        # TODO TUTAJ MOZE SIE WYWALAC BO TO MA JESZCZE CZAS TA DATE,
        # person.birthday = date
        return date

        # choose which sex is the person

    def _sex_(self):
        rand = random.randint(0, 206)
        print("test")
        while (1):
            pPPP = random.randint(1000, 9999)
            # assist = int(pPPP)
            if rand < 100:
                # person.sex = 1
                if pPPP % 2 == 1:
                    print(pPPP)
                    return 1, pPPP
            else:
                # person.sex = 0
                if pPPP % 2 == 0:
                    print(pPPP)
                    return 0, pPPP

    def _name_(self, person):
        names = []
        if person.sex == 1:
            names = [line.rstrip('\n') for line in open('mens_name.txt', encoding="utf8")]
        else:
            names = [line.rstrip('\n') for line in open('girls_name.txt', encoding="utf8")]
        rand = random.randint(0, len(names) - 1)
        return names[rand]

        # generating surname

    def _surname_(self, person):
        # creating variable
        vowel = ["a", "e", "i", "o", "u", "y"]
        consonants = ["b", "c", "d", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "z"]
        male_surname_ends = ["ski", "cki", "dzki", "ak", "ek", "ik", "yk", "ki", "owicz", "eowicz","ewicz","el","ny","uk","in","ny"]
        female_surname_ends = ["ska", "cka", "dzka", "ak", "ek", "ik", "yk", "ka", "owicz", "eowicz","na","ul","uk"]
        surname = ""
        # generating the first 2 letters of surname
        surname = consonants[random.randint(0, len(consonants) - 1)].upper() \
                  + vowel[random.randint(0, len(vowel) - 1)]\
                +consonants[random.randint(0, len(consonants) - 1)]
            # adding "koncowka" basic on sex
        if (person.sex == 1):
            surname = surname + male_surname_ends[random.randint(0, len(male_surname_ends) - 1)]
        else:
            surname = surname + female_surname_ends[random.randint(0, len(female_surname_ends) - 1)]
        return surname

    def save_person(self, person):
        """
        Saves person to database
        """
        person.save()

    def generatingPesel(self, person, pPPP):
        # this is very stupid way but i need this date to pesel
        data = self.generating_date()
        print(f"date: {data}")
        if 1900 < data.year < 2000:
            # adding year to pesel
            year = str(data.year % 1900)
            if len(year) != 2:
                year = "0" + year
            print(f"year function: {year}")
            person.pesel += year
            # adding month to pesel

            month = str(data.month)
            if len(month) != 1:
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
        Suma_kontrolna = int(person.pesel[0]) * 1 + int(person.pesel[1]) * 3 \
                         + int(person.pesel[2]) * 7 + int(person.pesel[3]) * 9
        Suma_kontrolna = Suma_kontrolna + int(person.pesel[4]) * 1 + int(person.pesel[5]) * 3\
                         + int(person.pesel[6]) * 7 + int(person.pesel[7]) * 9 + int(person.pesel[8]) * 1 + int(person.pesel[9]) * 3
        if (Suma_kontrolna > 10):
            Suma_kontrolna = 10 - Suma_kontrolna % 10
        else:
            Suma_kontrolna = 10 - Suma_kontrolna
        print("-----------------------")
        return person.pesel + str(Suma_kontrolna)



