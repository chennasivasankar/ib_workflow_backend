from django.db import models

from ib_tasks.models.gof import GoF
from ib_tasks.models.stage import Stage


class StageGoF(models.Model):
    gof = models.ForeignKey(GoF, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

    def __str__(self):
        return "{} gof in stage {}".format(
            self.gof_id, self.stage.stage_id
        )
