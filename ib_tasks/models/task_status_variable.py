from django.db import models

class TaskStatusVariable(models.Model):
    task_id = models.IntegerField()
    variable = models.TextField()
    value = models.TextField()
