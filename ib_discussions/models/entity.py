import uuid

from django.db import models

from ib_discussions.constants.enum import EntityType


def generate_uuid():
    return uuid.uuid4()


class Entity(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid,
                          editable=False)
    entity_choice = (
        (EntityType.TASK.value, EntityType.TASK.value),
    )
    entity_type = models.CharField(
        max_length=50,
        choices=entity_choice
    )
