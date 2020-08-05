
from django.db import models
from .filter import Filter
from .field import Field
from ib_tasks.constants.constants import OPERATOR_TYPES


class FilterCondition(models.Model):
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    field_id = models.ForeignKey(Field, on_delete=models.CASCADE)
    operator = models.CharField(max_length=100, choices=OPERATOR_TYPES)
    value = models.TextField()