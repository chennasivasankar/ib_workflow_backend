
from django.db import models


class ElasticUserIntermediary(models.Model):
    user_id = models.CharField(max_length=32, unique=True)
    elastic_user_id = models.CharField(max_length=50, unique=True)
