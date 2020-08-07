
from django.db import models

from .task_template import TaskTemplate
from ..constants.enum import Status


class Filter(models.Model):
    created_by = models.CharField(max_length=30)
    name = models.CharField(max_length=120)
    template = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)
    is_selected = models.CharField(max_length=100, choices=[
        (item.value, item.value) for item in Status
    ])
