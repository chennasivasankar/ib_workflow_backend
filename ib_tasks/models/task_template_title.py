from django.db import models

from ib_tasks.constants.constants import TASK_TEMPLATE_TITLE_DEFAULT_NAME
from ib_tasks.models.task_template import TaskTemplate


class TaskTemplateTitle(models.Model):
    task_template = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)
    title_display_name = models.CharField(
        max_length=100, default=TASK_TEMPLATE_TITLE_DEFAULT_NAME)
    placeholder_text = models.CharField(
        max_length=100, default=TASK_TEMPLATE_TITLE_DEFAULT_NAME)

    def __str__(self):
        return "{} is title of {}".format(
            self.title_display_name, self.task_template_id
        )
