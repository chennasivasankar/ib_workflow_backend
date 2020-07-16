from django.db import models

from ib_tasks.constants.constants import Permission_Types
from ib_tasks.models.gof import GoF


class GOFRole(models.Model):
    gof = models.ForeignKey(GoF, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    permission_type = models.CharField(max_length=100,
                                       choices=Permission_Types)
