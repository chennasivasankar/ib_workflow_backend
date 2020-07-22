from django.db import models


class TaskTemplateGlobalConstants(models.Model):
    task_template_id = models.IntegerField()
    variable = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=100)
    data_type = models.CharField(max_length=50)
