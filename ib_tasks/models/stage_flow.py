from django.db import models

from ib_tasks.models import Stage, StageAction


class StageFlow(models.Model):
    previous_stage = models.ForeignKey(
        Stage, on_delete=models.CASCADE, related_name="child_stages"
    )
    action = models.ForeignKey(StageAction, on_delete=models.CASCADE)
    next_stage = models.ForeignKey(Stage, on_delete=models.CASCADE)

    def __str__(self):
        return "{} -- {} -- {}".format(
            self.previous_stage_id, self.action_id, self.next_stage_id
        )

    class Meta:
        unique_together = ('previous_stage', 'action', 'next_stage')