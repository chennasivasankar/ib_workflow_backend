from django.db import models

from ib_tasks.models import Task


class UserTaskDelayReason(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    due_datetime = models.DateTimeField(auto_now=True)
    count = models.IntegerField()
    reason_id = models.IntegerField()
    reason = models.TextField(null=True, blank=True)
    user_id = models.CharField(max_length=200)
