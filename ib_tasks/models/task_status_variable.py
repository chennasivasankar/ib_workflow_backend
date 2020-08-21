
from django.db import models


class TaskStatusVariable(models.Model):
    task_id = models.CharField(max_length=120)
    variable = models.CharField(max_length=120)
    value = models.CharField(max_length=120)

    def __str__(self):
        return "{} with variable {} having value {}".format(
            self.task_id,
            self.variable,
            self.value)