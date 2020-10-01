from django.db import models

from ib_tasks.models.task_template import TaskTemplate


class GoF(models.Model):
    gof_id = models.CharField(max_length=50, primary_key=True)
    display_name = models.CharField(max_length=50, null=True, blank=True)
    task_template = models.ManyToManyField(
        TaskTemplate, through="TaskTemplateGoFs"
    )
    max_columns = models.IntegerField(default=2)

    def __str__(self):
        return self.gof_id
