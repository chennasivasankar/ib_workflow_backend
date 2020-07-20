"""
Created on: 18/07/20
Author: Pavankumar Pamuru

"""
from django.db import models

from .board import Board


class Column(models.Model):
    column_id = models.CharField(max_length=200, primary_key=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    display_order = models.IntegerField()
    task_selection_config = models.TextField(null=True)
    kanban_brief_view_config = models.TextField(null=True)
    list_brief_view_config = models.TextField(null=True)
    is_deleted = models.BooleanField(default=False)


class ColumnPermission(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    user_role_id = models.CharField(max_length=200)
