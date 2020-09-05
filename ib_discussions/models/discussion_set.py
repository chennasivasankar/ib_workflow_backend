import uuid

from django.db import models


def generate_uuid():
    return uuid.uuid4()


class DiscussionSet(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid,
                          editable=False)
    entity_id = models.CharField(max_length=200)
    entity_type = models.CharField(max_length=25)

    class Meta:
        unique_together = ("entity_id", "entity_type")
