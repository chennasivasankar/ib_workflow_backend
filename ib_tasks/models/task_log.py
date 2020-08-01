from django.db import models
from ib_tasks.models.task import Task


class TaskLog(models.Model):
    task_json = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=50)
