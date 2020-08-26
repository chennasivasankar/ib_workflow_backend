import uuid

from django.db import models
from ib_common.models import AbstractDateTimeModel


def generate_uuid4():
    return uuid.uuid4()


class ProjectRole(AbstractDateTimeModel):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    role_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=120)

    def __str__(self):
        return f"{self.role_id}"
