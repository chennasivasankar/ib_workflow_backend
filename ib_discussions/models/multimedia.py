import uuid

from django.db import models

from ib_discussions.constants.enum import MultimediaFormat


def generate_uuid():
    return uuid.uuid4()


MULTI_MEDIA_CHOICES = (
    (MultimediaFormat.IMAGE.value, MultimediaFormat.IMAGE.value),
    (MultimediaFormat.VIDEO.value, MultimediaFormat.VIDEO.value)
)


class MultiMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid,
                          editable=False)
    format_type = models.CharField(
        max_length=30, choices=MULTI_MEDIA_CHOICES
    )
    url = models.URLField()
    thumbnail_url = models.URLField()
