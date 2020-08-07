import uuid

from django.db import models

from ib_utility_tools.constants.enum import TimerEntityType


def generate_uuid():
    return uuid.uuid4()


class Timer(models.Model):
    timer_id = models.UUIDField(primary_key=True,
                                default=generate_uuid,
                                editable=False)
    entity_id = models.CharField(max_length=200)
    entity_type_choices = TimerEntityType.get_list_of_tuples()
    entity_type = models.CharField(max_length=10, choices=entity_type_choices)
    start_datetime = models.DateTimeField(null=True)
    duration_in_seconds = models.IntegerField(default=0)
    is_running = models.BooleanField(default=False)

    class Meta:
        unique_together = ("entity_id", "entity_type")
