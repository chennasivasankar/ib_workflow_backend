from django.db import models


class UserDetails(models.Model):
    user_id = models.CharField(max_length=1000)
    is_admin = models.BooleanField(default=False)
    company = models.ForeignKey('Company', on_delete=models.CASCADE,
                                null=True, related_name='users')
