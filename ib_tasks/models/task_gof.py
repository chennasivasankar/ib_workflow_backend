from django.db import models

from ib_tasks.models.gof import GoF
from ib_tasks.models.task import Task


class TaskGoF(models.Model):
    same_gof_order = models.IntegerField()
    gof = models.ForeignKey(GoF, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
