from django.db import models

from ib_tasks.models.task_template import TaskTemplate


class GoF(models.Model):
    gof_id = models.CharField(max_length=50, primary_key=True)
    display_name = models.CharField(max_length=50)
    task_template = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)
    order = models.IntegerField()
    max_columns = models.IntegerField(default=2)
    enable_multiple_gofs = models.BooleanField(default=False)
