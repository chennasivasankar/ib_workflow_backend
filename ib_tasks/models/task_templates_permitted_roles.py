from django.db import models

from ib_tasks.models import TaskTemplate


class TaskTemplatePermittedRoles(models.Model):
    task_template = models.ForeignKey(TaskTemplate, on_delete=models.CASCADE)
    role_id = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return f"{self.role_id} of {self.task_template.template_id}"
