from django.db import models

from ib_tasks.models import Stage
from ib_tasks.models.task import Task


class TaskStage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    stage_assignee_id = models.CharField(max_length=50, null=True)

    class Meta:
        unique_together = ('stage', 'task')
