from django.db import models


class ProjectTaskTemplate(models.Model):
    project_id = models.CharField(max_length=50)
    task_template = models.ForeignKey("TaskTemplate", on_delete=models.CASCADE)

    def __str__(self):
        return "{} template of project {}".format(
            self.task_template_id, self.project_id)
