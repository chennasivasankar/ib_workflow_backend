from django.db import models
from ib_tasks.constants.constants import FIELD_TYPES


class Field(models.Model):
    field_id = models.CharField(max_length=100, primary_key=True)
    field_display_name = models.CharField(max_length=100)
    required = models.BooleanField()
    field_type = models.CharField(max_length=100, choices=FIELD_TYPES)
    field_values = models.TextField(null=True)
    allowed_formats = models.TextField(null=True)
    read_permission_roles = models.TextField()
    write_permission_roles = models.TextField()
    help_text = models.CharField(max_length=200, null=True)
    tooltip = models.TextField(null=True)
    placeholder_text = models.CharField(max_length=100, null=True)
    error_messages = models.CharField(max_length=200, null=True)
    validations = models.CharField(max_length=200, null=True)
