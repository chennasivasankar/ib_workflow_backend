from django.db import models
from .stage import Stage


class StageAction(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    button_text = models.TextField()
    button_color = models.TextField(null=True)
    logic = models.TextField()
    py_function_import_path = models.TextField()
