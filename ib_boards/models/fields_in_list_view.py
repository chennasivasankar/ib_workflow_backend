"""
Created on: 05/09/20
Author: Pavankumar Pamuru

"""
from django.db import models

from .column import Column
from ib_boards.constants.constants import DISPLAY_STATUSES
from ib_boards.constants.enum import DisplayStatus


class FieldDisplayStatus(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=400)
    display_status = models.CharField(
        max_length=20, choices=DISPLAY_STATUSES, default=DisplayStatus.SHOW.value
    )
    field_id = models.CharField(max_length=200)


class FieldOrder(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=400)
    fields_order = models.TextField()