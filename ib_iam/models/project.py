import uuid

from django.db import models


def generate_uuid4():
    return uuid.uuid4()


class Project(models.Model):
    project_id = models.UUIDField(
        default=generate_uuid4,
        editable=False,
        primary_key=True
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    logo_url = models.TextField(null=True, blank=True)
