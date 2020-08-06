from django.db import models
from ib_common.models.abstract_date_time_model \
    import AbstractDateTimeModel

from ib_tasks.constants.enum import Priority


class Task(AbstractDateTimeModel):
    template_id = models.CharField(max_length=100)
    created_by = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=20, choices=Priority)
