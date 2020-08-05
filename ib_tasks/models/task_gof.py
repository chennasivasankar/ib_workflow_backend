from django.db import models

from ib_tasks.models.task import Task
from ib_tasks.models.gof import GoF


class TaskGoF(models.Model):
    same_gof_order = models.IntegerField()
    gof = models.ForeignKey(GoF, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return "{} of order {}".format(self.gof_id, self.same_gof_order)
