from django.db import models
from ib_tasks.models.task_template import TaskTemplate
from ib_tasks.models.gof import GoF


class Task(models.Model):
    task_id = models.CharField(max_length=100)
    template_id = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)


class TaskTemplateGoFs(models.Model):
    gof = models.ForeignKey(GoF, on_delete=models.CASCADE)
    task_template = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)
    order = models.IntegerField()
    enable_add_another_gof = models.BooleanField(default=False)


class TaskFields(models.Model):
    field_id = models.CharField(max_length=100)
    field_value = models.TextField()
