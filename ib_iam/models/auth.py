from django.db import models


class UserAuthToken(models.Model):
    user_id = models.CharField(max_length=36)
    token = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user_id} have tokrn = {self.toke}"
