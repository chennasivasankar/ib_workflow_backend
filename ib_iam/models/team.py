import uuid

from django.db import models
from ib_common.models import AbstractDateTimeModel


def generate_uuid4():
    return uuid.uuid4()


class Team(AbstractDateTimeModel):
    team_id = models.UUIDField(
        default=generate_uuid4,
        editable=False,
        primary_key=True
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    created_by = models.CharField(max_length=1000)


class TeamMember(models.Model):
    team = models.ForeignKey("Team", on_delete=models.CASCADE, related_name="members")
    member_id = models.CharField(max_length=1000)
