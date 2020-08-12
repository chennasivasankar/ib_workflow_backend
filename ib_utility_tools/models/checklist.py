import uuid

from django.db import models

from ib_utility_tools.constants.enum import EntityType


def generate_uuid():
    return uuid.uuid4()


class Checklist(models.Model):
    checklist_id = models.UUIDField(primary_key=True, default=generate_uuid,
                                    editable=False)
    entity_id = models.CharField(max_length=200)
    entity_type_choices = EntityType.get_list_of_tuples()
    entity_type = models.CharField(max_length=10, choices=entity_type_choices)

    class Meta:
        unique_together = ("entity_id", "entity_type")