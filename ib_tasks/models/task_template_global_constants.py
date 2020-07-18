from django.db import models

from ib_tasks.models import TaskTemplate


class TaskTemplateGlobalConstants(models.Model):
    task_template_id = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)
    variable = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=100)
    data_type = models.CharField(max_length=50)
