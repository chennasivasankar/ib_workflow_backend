# your django admin
from django.contrib import admin
from ib_iam.models.user import UserDetails
from ib_iam.models.company import Company
admin.site.register(UserDetails)
admin.site.register(Company)