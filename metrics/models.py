from datetime import datetime

from django.db import models
from person.models import Person


# Create your models here.
class PatientMetrics(models.Model):
    patient = models.ForeignKey(Person, on_delete=models.CASCADE)
    doctor_id = models.CharField(max_length=30)
    created = models.DateTimeField(default=datetime.now)
    attributes = models.CharField(max_length=30)
    notes = models.CharField(max_length=1024)

    def __str__(self):
        return " " + self.doctor_id + " " + str(self.created) + " " + self.notes

    class Meta:
        db_table = "peselgen_metrics"
