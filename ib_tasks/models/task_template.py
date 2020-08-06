from django.db import models


class TaskTemplate(models.Model):
    template_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    is_transition_template = models.BooleanField(default=False)
