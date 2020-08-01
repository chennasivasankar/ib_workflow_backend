# your django admin
from django.contrib import admin

from ib_iam.models import UserRole, Role, UserDetails, Company

admin.site.register(UserRole)
admin.site.register(Role)
admin.site.register(UserDetails)
admin.site.register(Company)