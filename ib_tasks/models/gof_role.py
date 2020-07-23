from django.db import models

from ib_tasks.constants.constants import Permission_Types
from ib_tasks.models.gof import GoF


class GoFRole(models.Model):
    gof = models.ForeignKey(GoF, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    permission_type = models.CharField(max_length=100,
                                       choices=Permission_Types)

    def __str__(self):
        return "{} has {} permission on {} gof".format(
            self.role, self.permission_type, self.gof_id
        )
