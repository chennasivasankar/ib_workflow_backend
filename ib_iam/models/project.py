import uuid

from django.db import models


def generate_project_id():
    from ib_iam.constants.config import PROJECT_ID_PREFIX
    suffix = str(uuid.uuid4()).replace("-", "")
    project_id = PROJECT_ID_PREFIX.format(suffix)
    return project_id


class Project(models.Model):
    project_id = models.CharField(
        default=generate_project_id,
        primary_key=True,
        max_length=100
    )
    display_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    logo_url = models.TextField(null=True, blank=True)


class ProjectTeam(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    class Meta:
        unique_together = ("team", "project")
