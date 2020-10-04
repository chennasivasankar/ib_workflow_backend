from django.db import models

from ib_tasks.models import Task, StageAction


class TransitionTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_by = models.CharField()
    action = models.ForeignKey(StageAction, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.task.task_display_id} transition checklist by {self.created_by}"
