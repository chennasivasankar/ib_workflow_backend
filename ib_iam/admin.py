# your django admin
from django.contrib import admin

from ib_iam.models import UserDetails, UserTeam, UserRole, Company, Role, Team

admin.site.register(UserDetails)
admin.site.register(UserTeam)
admin.site.register(UserRole)
# admin.site.register(Company)
admin.site.register(Role)
# admin.site.register(Team)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("company_id", "name", "description", "logo_url")
    search_fields = ["name"]


class TeamAdmin(admin.ModelAdmin):
    list_display = ("team_id", "name", "description")


admin.site.register(Company, CompanyAdmin)
admin.site.register(Team, TeamAdmin)
