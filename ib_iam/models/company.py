import uuid

from django.db import models


def generate_uuid4():
    return uuid.uuid4()


class Company(models.Model):
    company_id = models.UUIDField(primary_key=True, default=generate_uuid4,
                                  editable=False)
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
