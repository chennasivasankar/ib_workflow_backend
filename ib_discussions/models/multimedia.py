import uuid

from django.db import models

from ib_discussions.constants.enum import MultiMediaFormatEnum


def generate_uuid():
    return uuid.uuid4()


class MultiMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid,
                          editable=False)
    multimedia_choices = (
        (MultiMediaFormatEnum.IMAGE.value, MultiMediaFormatEnum.IMAGE.value),
        (MultiMediaFormatEnum.VIDEO.value, MultiMediaFormatEnum.VIDEO.value)
    )
    format_type = models.CharField(
        max_length=30, choices=multimedia_choices
    )
    url = models.TextField()
