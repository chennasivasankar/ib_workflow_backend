from django.db import models
import uuid

from ib_common.models import AbstractDateTimeModel


def generate_uuid4():
    return uuid.uuid4()


class Role(AbstractDateTimeModel):
    id = models.UUIDField(primary_key=True, default=generate_uuid4,
                          editable=False)
    role_id = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=120)

    def __str__(self):
        return f"{self.role_id}"