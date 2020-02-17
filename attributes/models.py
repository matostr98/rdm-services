from django.db import models
import jsonfield


class MetricsAttributes(models.Model):
    attributes = jsonfield.JSONField()

    def __str__(self):
        return self.attributes

    class Meta:
        db_table = "peselgen_attributes"
