from django.db import models


class Stage(models.Model):
    stage_id = models.CharField(max_length=200, unique=True)
    task_template_id = models.CharField(max_length=200)
    display_name = models.TextField()
    value = models.IntegerField()
    display_logic = models.TextField()
    field_display_config = models.TextField(max_length=400)
    card_info_kanban = models.TextField()
    card_info_list = models.TextField()
