from django.db import models

from .stage_actions import StageAction


class ActionPermittedRoles(models.Model):
    action = models.ForeignKey(StageAction, on_delete=models.CASCADE)
    role_id = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return f"action_id-{self.action_id} of role {self.role_id}"
