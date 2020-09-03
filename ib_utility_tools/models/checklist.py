import uuid

from django.db import models

from ib_utility_tools.constants.enum import EntityType


def generate_uuid():
    return uuid.uuid4()


def validate_entity_type(value):
    if value not in EntityType.get_list_of_values():
        from django.core.exceptions import ValidationError
        from ib_utility_tools.constants.exception_messages import \
            INVALID_ENTITY_TYPE_MESSAGE
        raise ValidationError(INVALID_ENTITY_TYPE_MESSAGE.format(value))


class Checklist(models.Model):
    checklist_id = models.UUIDField(primary_key=True, default=generate_uuid,
                                    editable=False)
    entity_id = models.CharField(max_length=200)
    entity_type = models.CharField(
        max_length=10,
        validators=[validate_entity_type]
    )

    class Meta:
        unique_together = ("entity_id", "entity_type")
