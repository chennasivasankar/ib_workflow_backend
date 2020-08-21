from django.db import models


class ElasticUserIntermediary(models.Model):
    user_id = models.CharField(max_length=32)
    elastic_user_id = models.CharField(max_length=50)

    class Meta:
        unique_together = ('user_id', 'elastic_user_id')
