from django.db import models
from ib_tasks.models.task import Task


class TaskGoF(models.Model):
    order = models.IntegerField()
    gof_id = models.CharField(max_length=100)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
