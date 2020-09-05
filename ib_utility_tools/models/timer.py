import uuid

from django.db import models

from ib_utility_tools.constants.enum import TimerEntityType


def generate_uuid():
    return uuid.uuid4()


def validate_timer_entity_type(value):
    if value not in TimerEntityType.get_list_of_values():
        from django.core.exceptions import ValidationError
        from ib_utility_tools.constants.exception_messages import \
            INVALID_TIMER_ENTITY_TYPE_MESSAGE
        raise ValidationError(INVALID_TIMER_ENTITY_TYPE_MESSAGE.format(value))


class Timer(models.Model):
    timer_id = models.UUIDField(primary_key=True,
                                default=generate_uuid,
                                editable=False)
    entity_id = models.CharField(max_length=200)
    entity_type = models.CharField(
        max_length=25, validators=[validate_timer_entity_type]
    )
    start_datetime = models.DateTimeField(null=True)
    duration_in_seconds = models.IntegerField(default=0)
    is_running = models.BooleanField(default=False)

    class Meta:
        unique_together = ("entity_id", "entity_type")
