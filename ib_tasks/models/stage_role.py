from django.db import models

from ib_tasks.models import Stage


class StageRole(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
