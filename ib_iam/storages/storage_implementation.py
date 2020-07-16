from typing import List

from ib_iam.interactors.storage_interfaces.dtos import UserTeamDTO, UserRoleDTO, UserCompanyDTO
from ib_iam.interactors.storage_interfaces.storage_interface import StorageInterface


class StorageImplementation(StorageInterface):

    def validate_user_is_admin(self, user_id: str) -> bool:
        from ib_iam.models.user_profile import UserProfile
        user = UserProfile.objects.get(user_id=user_id)
        return user.is_admin

    def get_users_who_are_not_admins(self, offset=0, limit=10):
        from ib_iam.models import UserProfile
        user_dtos = []
        users = UserProfile.objects.filter(is_admin=False)[offset:limit]
        from ib_iam.interactors.storage_interfaces.dtos import UserProfileDTO
        for user in users:
            user_dtos.append(UserProfileDTO(
                user_id=user.user_id,
                is_admin=user.is_admin,
                company_id=str(user.company_id)
            ))
        return user_dtos

    def get_team_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserTeamDTO]:
        from ib_iam.models import UserTeam
        user_teams = UserTeam.objects.filter(user_id__in=user_ids) \
            .select_related('team')
        team_dtos = []
        for user_team in user_teams:
            team = user_team.team
            team_dto = UserTeamDTO(
                user_id=user_team.user_id,
                team_id=str(team.team_id),
                team_name=team.name
            )
            team_dtos.append(team_dto)
        return team_dtos

    def get_role_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserRoleDTO]:
        from ib_iam.models import UserRole
        user_roles = UserRole.objects.filter(user_id__in=user_ids) \
            .select_related('role')
        role_dtos = []
        for user_role in user_roles:
            role = user_role.role
            role_dto = UserRoleDTO(
                user_id=user_role.user_id,
                role_id=str(role.id),
                role_name=role.role_name,
                role_description=role.role_description
            )
            role_dtos.append(role_dto)
        return role_dtos

    def get_company_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserCompanyDTO]:
        from ib_iam.models import UserRole
        from ib_iam.models import UserProfile
        user_companies = UserProfile.objects.filter(user_id__in=user_ids) \
            .select_related('company')
        company_dtos = []
        for user_company in user_companies:
            company = user_company.company
            company_dto = UserCompanyDTO(
                user_id=user_company.user_id,
                company_id=str(company.company_id),
                company_name=company.name
            )
            company_dtos.append(company_dto)
        return company_dtos
