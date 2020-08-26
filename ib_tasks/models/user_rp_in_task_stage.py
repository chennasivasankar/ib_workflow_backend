from django.db import models

from ib_tasks.models import Task, Stage


class UserRpInTaskStage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    rp_id = models.CharField(max_length=200)
    added_at = models.DateTimeField(auto_now=True)
