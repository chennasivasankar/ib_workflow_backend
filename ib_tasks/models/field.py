from django.db import models

from ib_tasks.constants.constants import Field_Types
from ib_tasks.models.gof import GoF


class Field(models.Model):
    field_id = models.CharField(max_length=100, primary_key=True)
    display_name = models.CharField(max_length=100)
    required = models.BooleanField(default=True)
    field_type = models.CharField(max_length=100, choices=Field_Types)
    field_values = models.TextField(null=True, blank=True)
    allowed_formats = models.TextField(null=True, blank=True)
    help_text = models.CharField(max_length=200, null=True, blank=True)
    tooltip = models.TextField(null=True, blank=True)
    placeholder_text = models.CharField(max_length=100, null=True, blank=True)
    error_messages = models.CharField(max_length=200, null=True, blank=True)
    validation_regex = models.CharField(max_length=200, null=True, blank=True)
    order = models.IntegerField()
    gof = models.ForeignKey(GoF, on_delete=models.CASCADE)
    is_unique = models.BooleanField(default=False)

    def __str__(self):
        return "{} in {} of type  {}".format(
            self.field_id, self.gof_id, self.field_type
        )
