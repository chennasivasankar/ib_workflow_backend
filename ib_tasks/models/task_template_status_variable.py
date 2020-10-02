from django.db import models

from ib_tasks.models import TaskTemplate


class TaskTemplateStatusVariable(models.Model):
    task_template = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)
    variable = models.TextField()
    value = models.TextField()
