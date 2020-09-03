from django.db import models

from ib_tasks.models import Task, Stage


class UserTaskDelayReason(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    due_datetime = models.DateTimeField()
    count = models.IntegerField()
    reason_id = models.IntegerField()
    reason = models.TextField(null=True, blank=True)
    user_id = models.CharField(max_length=200)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
