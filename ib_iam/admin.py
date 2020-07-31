# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ib_iam.models import *

admin.site.register(UserDetails)
admin.site.register(UserTeam)
admin.site.register(Team)
admin.site.register(Company)






