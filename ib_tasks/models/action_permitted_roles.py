from django.db import models
from .stage_actions import StageAction

class ActionPermittedRoles(models.Model):
    action = models.ForeignKey(StageAction, on_delete=models.CASCADE)
    role_id = models.CharField(max_length=200)
