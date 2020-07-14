from django.db import models


class Role(models.Model):
    role_id = models.CharField(unique=True, max_length=30)
    role_name = models.CharField(max_length=30)
    role_description = models.CharField(max_length=120)