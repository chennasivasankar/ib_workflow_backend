from django.db import models

from ib_tasks.models.task import Task
from ib_tasks.models.stage import Stage


class TaskStageHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    task_stage_assignee_id = models.CharField(max_length=50)
    joined_at = models.DateTimeField(auto_now=True)
    left_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{} with {} and assigned to {}".format(self.task_id, self.stage_id, self.task_stage_assignee_id)