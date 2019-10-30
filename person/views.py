from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.views import View
from rest_framework.utils import json


from person.models import Person

class PersonView(View):

    def get(self, request):
        person_list = list(Person.objects.all().values())
        return JsonResponse(person_list, safe=False)

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        person = self.json_to_person(body["name"], body["surname"], body["pesel"], body["sex"], body["birthday"])
        person.save()
        return HttpResponse(status=201)

    def json_to_person(self, name, surname, pesel, sex, birthday):
        person = Person()
        person.name = name
        person.surname = surname
        person.pesel = pesel
        person.sex = sex
        if birthday is not "":
            person.birthday = birthday
        return person


