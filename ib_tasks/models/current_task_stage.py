from django.db import models

from ib_tasks.models.task import Task


class CurrentTaskStage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    stage = models.ForeignKey("Stage", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('stage', 'task')

    def __str__(self):
        return "{} with {}".format(
            self.task.task_display_id,
            self.stage.stage_id)
