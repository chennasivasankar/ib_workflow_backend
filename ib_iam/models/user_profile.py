from django.db import models
from ib_iam.models import Company, Role, Team


class UserDetails(models.Model):
    user_id = models.CharField(max_length=1000)
    is_admin = models.BooleanField(default=False)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)


class UserTeam(models.Model):
    user_id = models.CharField(max_length=1000)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)


class UserRole(models.Model):
    user_id = models.CharField(max_length=1000)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
