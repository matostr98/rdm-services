from django.http import HttpResponse, JsonResponse
from django.views import View
from person.models import Person


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