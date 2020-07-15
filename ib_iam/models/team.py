import uuid

from django.db import models
from ib_common.models import AbstractDateTimeModel


class Team(AbstractDateTimeModel):
    team_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)


class TeamMember(models.Model):
    team = models.ForeignKey("Team", on_delete=models.CASCADE, related_name="members")
    member_id = models.CharField(max_length=200)
