from django.db import models

from ib_tasks.models import GoF, TaskTemplate


class TaskTemplateGoF(models.Model):
    gof_id = models.ForeignKey(GoF, on_delete=models.CASCADE)
    template_id = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)
    order = models.IntegerField()
    enable_multiple_gofs = models.BooleanField(default=False)