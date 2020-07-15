from django.db import models
from ib_iam.models import Company, Role, Team


class UserCompany(models.Model):
    # TODO: Check the field
    user_id = models.CharField(max_length=32)
    is_admin = models.BooleanField(default=False)
    company = models.OneToOneField('Company', on_delete=models.CASCADE)


class UserTeam(models.Model):
    user_id = models.CharField(max_length=32)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)


class UserRole(models.Model):
    user_id = models.CharField(max_length=32)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
