
from django.db import models

from .task_template import TaskTemplate
from ..constants.enum import Status


class Filter(models.Model):
    created_by = models.CharField(max_length=120)
    project_id = models.CharField(max_length=50)
    name = models.CharField(max_length=120)
    template = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)
    is_selected = models.CharField(max_length=100, choices=[
        (item.value, item.value) for item in Status
    ], default=Status.ENABLED.value)

    class Meta:
        indexes = [
            models.Index(fields=['project_id', 'is_selected', 'created_by']),
            models.Index(fields=['project_id', 'created_by']),
        ]
