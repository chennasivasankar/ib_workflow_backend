from django.db import models


class TaskStatusVariable(models.Model):
    task_id = models.CharField(max_length=200)
    variable = models.TextField()
    value = models.TextField()
