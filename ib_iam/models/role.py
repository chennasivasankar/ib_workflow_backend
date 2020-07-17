from django.db import models
from ib_common.models import AbstractDateTimeModel


def generate_uuid4():
    import uuid
    return uuid.uuid4()


class Role(AbstractDateTimeModel):
    id = models.UUIDField(primary_key=True, default=generate_uuid4, editable=False)
    role_id = models.CharField(unique=True, max_length=1000)
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
