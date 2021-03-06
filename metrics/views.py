import multiprocessing

from django.http import HttpResponse, JsonResponse
from django.views import View

from metrics.metrics_service import MetricsService
from metrics.models import PatientMetrics


class MetricsView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.metrics_service = MetricsService()

    def get(self, request):
        """
        Http get method to get all persons or person with given pesel
        Example url to get person by pesel: localhost:8000/person/12345678901
        :param request: has string parameter pesel
        :return: JSON response
        """
        metrics_list = list(PatientMetrics.objects.all().values())
        return JsonResponse(metrics_list, safe=False)

    def post(self, request, number=1):
        """
        Http method to generate persons and save them to database
        Example url to generate six persons: localhost:8000/person/6
        :param number: number of generated persons, default is 1
        :return: http status for created
        """
        for i in range(0, number):
            metrics = self.metrics_service.create_metrics()
            metrics.save()

        return HttpResponse(status=201)
