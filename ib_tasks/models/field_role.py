from django.db import models

from ib_tasks.constants.constants import Permission_Types
from ib_tasks.models.field import Field


class FieldRole(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    permission_type = models.CharField(max_length=100,
                                       choices=Permission_Types)

    def __str__(self):
        return "{} with {}".format(self.field_id, self.role)
