from django.db import models
from ib_tasks.models.gof import GoF
from ib_tasks.models.task_template import TaskTemplate


class TaskTemplateGoFs(models.Model):
    gof = models.ForeignKey(GoF, on_delete=models.CASCADE)
    task_template = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)
    order = models.IntegerField()
    enable_add_another_gof = models.BooleanField(default=False)

    def __str__(self):
        return "{} gof in template {}".format(
            self.gof_id, self.task_template_id
        )
