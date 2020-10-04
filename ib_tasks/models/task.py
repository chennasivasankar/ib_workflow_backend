from django.db import models
from ib_common.models.abstract_date_time_model \
    import AbstractDateTimeModel

from ib_tasks.constants.constants import PRIORITY_TYPES


class Task(AbstractDateTimeModel):
    project_id = models.CharField(
        max_length=50, db_index=True, null=True, blank=True)
    task_display_id = models.CharField(
        max_length=50, unique=True, null=True, blank=True, db_index=True)
    template = models.ForeignKey("ib_tasks.TaskTemplate", on_delete=models.CASCADE)
    created_by = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(
        max_length=20, choices=PRIORITY_TYPES, default=PRIORITY_TYPES[0][0],
        null=True, blank=True)

    def __str__(self):
        return "{}".format(self.task_display_id)


class ElasticSearchTask(models.Model):
    elasticsearch_id = models.CharField(max_length=200, unique=True)
    task_id = models.IntegerField(unique=True)

    class Meta:
        unique_together = ('elasticsearch_id', 'task_id')
