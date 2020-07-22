from django.db import models
from .task_template import TaskTemplate


class TaskTemplateStatusVariables(models.Model):
    task_template_id = models.ForeignKey(
        TaskTemplate, on_delete=models.CASCADE)
    variable = models.CharField(max_length=120)
