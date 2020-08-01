# your django admin
from django.contrib import admin

from ib_iam.models import UserDetails, UserTeam, UserRole, Company, Role, Team

admin.site.register(UserDetails)
admin.site.register(UserTeam)
admin.site.register(UserRole)
admin.site.register(Company)
admin.site.register(Role)
admin.site.register(Team)
