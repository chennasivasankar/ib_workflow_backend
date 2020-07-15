# from ib_users.models.user_profile import UserProfile
from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)
