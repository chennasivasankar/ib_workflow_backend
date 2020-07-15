import uuid

from django.db import models

from ib_iam.models.Role import generate_uuid4


class Company(models.Model):
    company_id = models.UUIDField(primary_key=True, default=generate_uuid4,
                         editable=False)
    name = models.CharField(max_length=30)