from django.db import models

from .stage import Stage


class StageAction(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    button_text = models.TextField()
    button_color = models.TextField(null=True)
    logic = models.TextField()
    action_type = models.CharField(max_length=100)
    transition_template = models.ForeignKey("TaskTemplate", on_delete=models.CASCADE)
    py_function_import_path = models.TextField()

    class Meta:
        unique_together = ('stage', 'name')
