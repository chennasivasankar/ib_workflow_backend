# your django admin
from django.contrib import admin

from ib_iam.models import (
    UserDetails, UserTeam, UserRole, Company,
    Team, ElasticUserIntermediary, TeamMemberLevel, City, State, Country,
    Project, ProjectTeam
)


class ElasticUserIntermediaryAdmin(admin.ModelAdmin):
    list_display = ("user_id", "elastic_user_id")


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
    raw_id_fields = ("project_role",)

    @staticmethod
    def _role_id(obj):
        return obj.project_role.role_id


class UserTeamAdmin(admin.ModelAdmin):
    list_display = ("user_id", "team_id", "team_member_level",
                    "immediate_superior_team_user")
    search_fields = ["user_id"]
    raw_id_fields = ("team",)


class TeamMemberLevelAdmin(admin.ModelAdmin):
    list_display = ("id", "team", "level_name", "level_hierarchy")


class ProjectTeamInline(admin.TabularInline):
    model = ProjectTeam


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_id", "name", "description", "logo_url")
    search_fields = ["name"]
    list_filter = ["project_id"]
    inlines = [
        ProjectTeamInline
    ]


class ProjectTeamAdmin(admin.ModelAdmin):
    list_display = ("project", "team")
    search_fields = ["project"]
    list_filter = ["project"]
    raw_id_fields = ("team", "project")


admin.site.register(Company, CompanyAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(UserDetails, IAMUserAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(UserTeam, UserTeamAdmin)
admin.site.register(TeamMemberLevel, TeamMemberLevelAdmin)
admin.site.register(ElasticUserIntermediary, ElasticUserIntermediaryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectTeam, ProjectTeamAdmin)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
