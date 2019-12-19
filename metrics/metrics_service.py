from datetime import datetime
from random import randrange
from datetime import timedelta
import random
import logging

from metrics.models import PatientMetrics


class MetricsService:

    def create_metrics(self):
        metrics = PatientMetrics()
        metrics.patient_id = "patient id"
        metrics.doctor_id = "doctor id"
        metrics.notes = "some notes"
        return metrics
