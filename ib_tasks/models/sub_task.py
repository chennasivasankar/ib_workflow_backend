from django.db import models

from ib_tasks.models.task import Task


class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="sub_tasks")
    sub_task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name="parent_task")

    def __str__(self):
        return "{} is sub task of {}".format(self.sub_task_id, self.task_id)
