from django.db import models

from ib_tasks.models import Stage


class StagePermittedRoles(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    role_id = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return f"{self.role_id} of {self.stage.stage_id}"
