from django.db import models

from ib_tasks.constants.constants import Field_Types, Permission_Types
from ib_tasks.models import gof


class Field(models.Model):
    field_id = models.CharField(max_length=100, primary_key=True)
    display_name = models.CharField(max_length=100)
    required = models.BooleanField(default=True)
    field_type = models.CharField(max_length=100, choices=Field_Types)
    field_values = models.TextField(null=True)
    allowed_formats = models.TextField(null=True)
    help_text = models.CharField(max_length=200, null=True)
    tooltip = models.TextField(null=True)
    placeholder_text = models.CharField(max_length=100, null=True)
    error_messages = models.CharField(max_length=200, null=True)
    validation_regex = models.CharField(max_length=200, null=True)
    gof = models.ForeignKey(gof, on_delete=models.CASCADE)
