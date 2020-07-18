from django.db import models

class Stage(models.Model):
    stage_id = models.CharField(max_length=400, unique=True)
    display_name = models.TextField()
    value = models.IntegerField()
    display_logic = models.TextField()
