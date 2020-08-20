import uuid

from django.db import models

from ib_iam.models import Team


def generate_uuid():
    return uuid.uuid4()


class TeamMemberLevel(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    level_name = models.CharField(max_length=200)
    level_hierarchy = models.IntegerField()

    class Meta:
        unique_together = ('team', 'level_hierarchy', 'level_name')

