from django.db import models

from ib_tasks.models.task import Task


class CurrentTaskStage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    stage = models.ForeignKey("Stage", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('stage', 'task')