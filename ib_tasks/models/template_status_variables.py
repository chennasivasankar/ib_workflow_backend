from django.db import models

class TaskTemplateStatusVariables(models.Model):
    task_template_id = models.IntegerField()
    variable = models.CharField(max_length=200)
