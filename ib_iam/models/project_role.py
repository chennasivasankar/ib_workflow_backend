import uuid

from django.db import models
from ib_common.models import AbstractDateTimeModel


def generate_role_id():
    from ib_iam.constants.config import ROLE_ID_PREFIX
    role_id = ROLE_ID_PREFIX.format(str(uuid.uuid4()))
    return role_id


class ProjectRole(AbstractDateTimeModel):
    role_id = models.CharField(default=generate_role_id,
                               primary_key=True,
                               max_length=100)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=120, null=True, blank=True)

    class Meta:
        unique_together = ('role_id', 'project')

    def __str__(self):
        return f"{self.role_id}"
