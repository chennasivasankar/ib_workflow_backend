from django.db import models


class Project(models.Model):
    project_id = models.CharField(
        primary_key=True,
        max_length=100
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    logo_url = models.TextField(null=True, blank=True)
