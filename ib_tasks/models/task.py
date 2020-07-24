from django.db import models
from ib_common.models.abstract_date_time_model \
    import AbstractDateTimeModel


class Task(AbstractDateTimeModel):
    template_id = models.CharField(max_length=100)
    created_by_id = models.CharField(max_length=50)
