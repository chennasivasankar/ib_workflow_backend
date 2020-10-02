from django.db import models

from ib_tasks.models.stage_actions import StageAction
from ib_tasks.models.task import Task


class TaskLog(models.Model):
    task_json = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)
    action = models.ForeignKey(StageAction, on_delete=models.CASCADE,
                               null=True, blank=True)
    acted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Task {} log on action {}".format(self.task.task_display_id,
                                                 self.action_id)
