from django.db import models


def generate_uuid4():
    import uuid
    return uuid.uuid4()


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid4, editable=False)
    role_id = models.CharField(unique=True, max_length=1000)
    role_name = models.CharField(max_length=1000)
    role_description = models.CharField(max_length=1000)
