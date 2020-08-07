from django.db import models
from ib_tasks.models.task import Task
from ib_tasks.models.stage_actions import StageAction


class TaskLog(models.Model):
    task_json = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)
    action = models.ForeignKey(StageAction, on_delete=models.CASCADE)
    acted_at = models.DateTimeField(auto_now_add=True)
