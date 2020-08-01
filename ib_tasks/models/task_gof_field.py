from django.db import models
from ib_tasks.models.field import Field
from ib_tasks.models.task_gof import TaskGoF


class TaskGoFField(models.Model):
    task_gof = models.ForeignKey(TaskGoF, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    field_response = models.TextField()

