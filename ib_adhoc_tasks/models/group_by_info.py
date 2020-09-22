from django.db import models

from ib_adhoc_tasks.constants.constants import View_Types


class GroupByInfo(models.Model):
    user_id = models.CharField(max_length=50)
    group_by = models.CharField(max_length=50)
    order = models.IntegerField()
    view_type = models.CharField(max_length=20, choices=View_Types)
