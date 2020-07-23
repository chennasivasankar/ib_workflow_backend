from django.db import models
from ib_tasks.models.task_template import TaskTemplate


class GlobalConstant(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    task_template = models.ForeignKey(
        TaskTemplate, on_delete=models.CASCADE,
        related_name="global_constants"
    )
