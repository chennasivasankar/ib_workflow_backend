from django.db import models


class Stage(models.Model):
    stage_id = models.CharField(max_length=200, unique=True)
    task_template_id = models.CharField(max_length=200)
    display_name = models.TextField()
    value = models.IntegerField()
    display_logic = models.TextField()