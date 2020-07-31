from django.db import models

class TaskTemplateStatusVariable(models.Model):
    task_template_id = models.CharField(max_length=200)
    variable = models.TextField()
    value = models.TextField()
