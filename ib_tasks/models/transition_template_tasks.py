from django.db import models

from ib_tasks.models import Task, StageAction


class TransitionTemplateTasks(models.Model):
    task = models.ForeignKey(
        Task, null=True, on_delete=models.SET_NULL)
    action = models.ForeignKey(
        StageAction, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Transition Task of task {}".format(self.task_id)
