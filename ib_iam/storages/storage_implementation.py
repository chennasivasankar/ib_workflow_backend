from typing import List

from ib_iam.interactors.storage_interfaces.dtos import UserTeamDTO, \
    UserRoleDTO, UserCompanyDTO, UserDTO, CompanyDTO, \
    TeamDTO, RoleIdAndNameDTO, RoleDTO
from ib_iam.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_iam.models import Role


class StorageImplementation(StorageInterface):

    def check_is_admin_user(self, user_id: str) -> bool:
        from ib_iam.models.user import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        return user.is_admin

    def get_role_objs_ids(self, roles):
        role_ids = Role.objects.filter(role_id__in=roles) \
            .values_list('id', flat=True)
        return role_ids

    def add_new_user(self, user_id: str, is_admin: bool, company_id: str,
                     role_ids, team_ids: List[str]):
        self.create_user(company_id, is_admin, user_id)
        self.add_user_to_the_teams(team_ids, user_id)
        self.add_roles_to_the_user(role_ids, user_id)

    @staticmethod
    def add_roles_to_the_user(role_ids, user_id):
        from ib_iam.models import UserRole
        user_roles = [UserRole(user_id=user_id, role_id=str(role_id))
                      for role_id in role_ids]
        UserRole.objects.bulk_create(user_roles)

    @staticmethod
    def add_user_to_the_teams(team_ids, user_id):
        from ib_iam.models import UserTeam
        user_teams = [UserTeam(user_id=user_id, team_id=team_id)
                      for team_id in team_ids]
        UserTeam.objects.bulk_create(user_teams)

    @staticmethod
    def create_user(company_id, is_admin, user_id):
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=is_admin,
                                   company_id=company_id)

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

    def create_roles(self, role_dtos: List[RoleDTO]):
        role_objects = [
            Role(role_id=role_dto.role_id, name=role_dto.name,
                 description=role_dto.description)
            for role_dto in role_dtos]
        Role.objects.bulk_create(role_objects)

    def get_valid_role_ids(self, role_ids: List[str]):
        valid_role_ids = Role.objects.filter(role_id__in=role_ids).values_list(
            "role_id", flat=True
        )
        return list(valid_role_ids)
