from django.db import models

from .task_template import TaskTemplate
from .stage import Stage


class TaskStage(models.Model):
    task_template = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
