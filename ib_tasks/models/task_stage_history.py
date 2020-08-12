from django.db import models

from ib_tasks.models.task import Task


class TaskStageHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    stage = models.ForeignKey("Stage", on_delete=models.CASCADE)
    assignee_id = models.CharField(max_length=50, null=True, blank=True)
    joined_at = models.DateTimeField(auto_now=True, null=True)
    left_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{} with {} and assigned to {}".format(
            self.task__task_display_id,
            self.stage__stage_id,
            self.assignee_id)