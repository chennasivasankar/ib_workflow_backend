
from django.db import models


class Filter(models.Model):
    created_by = models.CharField(max_length=30)
    name = models.CharField(max_length=120)
    template = models.CharField(max_length=120)
    is_selected = models.BooleanField(default=False)
