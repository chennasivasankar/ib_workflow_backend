from django.db import models
from ib_tasks.models.task import Task


class TaskGoF(models.Model):
    same_gof_order = models.IntegerField()
    gof_id = models.CharField(max_length=100)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.gof_id
