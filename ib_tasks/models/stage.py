from django.db import models

from ib_tasks.models.gof import GoF


class Stage(models.Model):
    stage_id = models.CharField(max_length=200, unique=True)
    task_template_id = models.CharField(max_length=200)
    display_name = models.TextField()
    value = models.IntegerField()
    display_logic = models.TextField()
    card_info_kanban = models.TextField()
    card_info_list = models.TextField()
    stage_color = models.CharField(max_length=100, null=True)
    gof = models.ManyToManyField(GoF, through="StageGoF")

    def __str__(self):
        return self.stage_id
