from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
