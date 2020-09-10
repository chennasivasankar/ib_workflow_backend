import uuid

from django.db import models

from ib_discussions.constants.enum import EntityType

ENTITY_CHOICE_FOR_DISCUSSION = [EntityType.TASK.value]


def validate_entity_type_for_discussion(value):
    if value not in ENTITY_CHOICE_FOR_DISCUSSION:
        from django.core.exceptions import ValidationError
        from ib_utility_tools.constants.exception_messages import \
            INVALID_DISCUSSION_ENTITY_TYPE_MESSAGE
        raise ValidationError(
            INVALID_DISCUSSION_ENTITY_TYPE_MESSAGE.format(value))


def generate_uuid():
    return uuid.uuid4()


class Entity(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid,
                          editable=False)
    entity_type = models.CharField(
        max_length=25,
        validators=[validate_entity_type_for_discussion]
    )
