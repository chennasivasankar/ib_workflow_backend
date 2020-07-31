from typing import List

from ib_iam.interactors.storage_interfaces.dtos \
    import UserCompanyDTO, UserDTO, UserTeamDTO, UserRoleDTO, UserIdAndNameDTO
from ib_iam.interactors.storage_interfaces.get_users_list_storage_interface \
    import GetUsersListStorageInterface


class GetUsersListStorageImplementation(GetUsersListStorageInterface):
    def check_is_admin_user(self, user_id: str) -> bool:
        from ib_iam.models.user import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        return user.is_admin

    def get_users_who_are_not_admins(self, offset, limit) -> List[UserDTO]:
        from ib_iam.models import UserDetails
        user_dtos = []
        users = UserDetails.objects. \
                    filter(is_admin=False)[offset: offset + limit]
        for user in users:
            user_dtos.append(UserDTO(
                user_id=user.user_id,
                is_admin=user.is_admin,
                company_id=str(user.company_id)
            ))
        return user_dtos

    def get_total_count_of_users_for_query(self):
        from ib_iam.models import UserDetails
        total_count_of_users = \
            UserDetails.objects.filter(is_admin=False).count()
        return total_count_of_users

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
                name=role.name,
                description=role.description
            )
            role_dtos.append(role_dto)
        return role_dtos

    def get_company_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserCompanyDTO]:
        from ib_iam.models import UserDetails
        user_companies = UserDetails.objects.filter(user_id__in=user_ids) \
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

    def get_user_details_dtos_based_on_limit_offset_and_search_query(
            self, limit: int, offset: int, search_query: str
    ) -> List[UserIdAndNameDTO]:
        from ib_iam.models import UserDetails
        user_details_objects = UserDetails.objects.filter(
            name__icontains=search_query
        )[offset: limit + offset]
        user_details_dtos = self._convert_to_user_details_dtos(
            user_details_objects=user_details_objects
        )
        return user_details_dtos

    def get_user_details_dtos_based_on_search_query(
            self, search_query: str
    ) -> List[UserIdAndNameDTO]:
        from ib_iam.models import UserDetails
        user_details_objects = UserDetails.objects.filter(
            name__icontains=search_query
        )
        user_details_dtos = self._convert_to_user_details_dtos(
            user_details_objects=user_details_objects
        )
        return user_details_dtos

    def _convert_to_user_details_dtos(self, user_details_objects):
        user_details_dtos = [
            self._convert_to_user_details_dto(
                user_details_object=user_details_object)
            for user_details_object in user_details_objects
        ]
        return user_details_dtos

    @staticmethod
    def _convert_to_user_details_dto(user_details_object):
        user_details_dto = UserIdAndNameDTO(
            user_id=user_details_object.user_id,
            name=user_details_object.name
        )
        return user_details_dto
