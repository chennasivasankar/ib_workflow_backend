"""
Created on: 04/10/20
Author: Pavankumar Pamuru

"""
from django.db import models


class District(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
