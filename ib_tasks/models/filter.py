
from django.db import models
from .task_template import TaskTemplate


class Filter(models.Model):
    created_by = models.CharField(max_length=30)
    name = models.CharField(max_length=120)
    template = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)
    is_selected = models.BooleanField(default=False)
