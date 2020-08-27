from django.db import models


class UserDetails(models.Model):
    user_id = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000, null=True)
    is_admin = models.BooleanField(default=False)
    cover_page_url = models.URLField(max_length=1000, null=True, blank=True)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL,
                                null=True,
                                blank=True, related_name="users")


# TODO: Link to UserDetails to have flexibility to get user details
class UserTeam(models.Model):
    user_id = models.CharField(max_length=1000)
    team_member_level = models.ForeignKey(
        "TeamMemberLevel", on_delete=models.SET_NULL,
        null=True, blank=True
    )
    immediate_superior_team_user = models.ForeignKey(
        "self", on_delete=models.SET_NULL,
        null=True, blank=True, related_name="subordinate_members"
    )
    team = models.ForeignKey('Team', on_delete=models.CASCADE,
                             related_name="users")

    class Meta:
        unique_together = ('user_id', 'team')


class UserRole(models.Model):
    user_id = models.CharField(max_length=1000)
    project_role = models.ForeignKey('ProjectRole', on_delete=models.CASCADE,
                                     null=True)

    def __str__(self):
        return f"{self.user_id} have {self.project_role.role_id}"
