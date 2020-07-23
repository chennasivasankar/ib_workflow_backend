"""
Created on: 18/07/20
Author: Pavankumar Pamuru

"""
from django.db import models


class Board(models.Model):
    board_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)
