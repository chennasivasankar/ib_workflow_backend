from typing import List

from ib_iam.interactors.storage_interfaces.edit_user_storage_interface \
    import EditUserStorageInterface


class EditUserStorageImplementation(EditUserStorageInterface):
    def check_is_admin_user(self, user_id: str) -> bool:
        from ib_iam.models.user import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        return user.is_admin

    def is_user_exist(self, user_id: str) -> bool:
        from ib_iam.models import UserDetails
        is_exists = UserDetails.objects.filter(user_id=user_id).exists()
        return is_exists

    def get_role_objs_ids(self, roles):
        from ib_iam.models import Role
        role_ids = Role.objects.filter(role_id__in=roles) \
            .values_list('id', flat=True)
        return role_ids

    def validate_role_ids(self, role_ids):
        from ib_iam.models import Role
        role_objs_count = Role.objects.filter(
            role_id__in=role_ids).count()
        are_exists = role_objs_count == len(role_ids)
        return are_exists

    def validate_company(self, company_id):
        from ib_iam.models import Company
        is_exist = Company.objects.filter(company_id=company_id).exists()
        return is_exist

    def validate_teams(self, team_ids):
        from ib_iam.models import Team
        team_objs_count = Team.objects.filter(
            team_id__in=team_ids).count()
        are_exists = team_objs_count == len(team_ids)
        return are_exists

    def unassign_company_for_user(self, user_id: str):
        from ib_iam.models import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        user.company = None
        user.save()

    def unassign_roles_for_user(self, user_id: str):
        from ib_iam.models import UserRole
        UserRole.objects.filter(user_id=user_id).delete()

    def unassign_teams_for_user(self, user_id: str):
        from ib_iam.models import UserTeam
        UserTeam.objects.filter(user_id=user_id).delete()

    def add_roles_to_the_user(self, user_id: str, role_ids: List[str]):
        from ib_iam.models import UserRole
        user_roles = [UserRole(user_id=user_id, role_id=str(role_id))
                      for role_id in role_ids]
        UserRole.objects.bulk_create(user_roles)

    def add_user_to_the_teams(self, user_id: str, team_ids: List[str]):
        from ib_iam.models import UserTeam
        user_teams = [UserTeam(user_id=user_id, team_id=team_id)
                      for team_id in team_ids]
        UserTeam.objects.bulk_create(user_teams)

    def add_company_to_user(self, company_id: str, user_id: str):
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, company_id=company_id)
