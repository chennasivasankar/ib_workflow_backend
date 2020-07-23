from django.db import models

from ib_tasks.models import Stage


class TaskStage(models.Model):
    task = models.CharField()
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('stage', 'task')
