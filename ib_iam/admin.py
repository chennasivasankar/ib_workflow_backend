# your django admin
from django.contrib import admin

from ib_iam.models import UserDetails, UserTeam, UserRole, Company, Role, Team


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("company_id", "name", "description", "logo_url")
    search_fields = ["name"]


class TeamAdmin(admin.ModelAdmin):
    list_display = ("team_id", "name", "description")


class RoleAdmin(admin.ModelAdmin):
    list_display = ("role_id", "name", "description")
    search_fields = ["role_id", "name"]


class IAMUserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "name", "is_admin")
    search_fields = ["user_id", "name"]
    list_filter = ["is_admin"]


class UserRoleAdmin(admin.ModelAdmin):
    list_display = ("user_id", "_role_id")
    search_fields = ["user_id"]
    list_filter = ["user_id"]
    raw_id_fields = ("role",)

    @staticmethod
    def _role_id(obj):
        return obj.role.role_id


class UserTeamAdmin(admin.ModelAdmin):
    list_display = ("user_id", "team_id")
    search_fields = ["user_id"]
    raw_id_fields = ("team",)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(UserDetails, IAMUserAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(UserTeam, UserTeamAdmin)
