from typing import List

from ib_iam.adapters.dtos import SearchQueryWithPaginationDTO
from ib_iam.interactors.storage_interfaces.dtos import UserDTO, UserTeamDTO, \
    UserRoleDTO, UserCompanyDTO, RoleIdAndNameDTO, TeamIdAndNameDTO, \
    CompanyIdAndNameDTO, UserIdAndNameDTO, TeamDTO, TeamUserIdsDTO, CompanyDTO, \
    CompanyIdWithEmployeeIdsDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface \
    import UserStorageInterface


class UserStorageImplementation(UserStorageInterface):

    def get_user_ids_who_are_not_admin(self) -> List[str]:
        from ib_iam.models import UserDetails
        return list(UserDetails.objects.filter(
            is_admin=False).values_list("user_id", flat=True))

    def get_user_ids(self, role_ids: List[str]) -> List[str]:
        from ib_iam.models import UserRole
        return list(UserRole.objects.filter(
            role__role_id__in=role_ids).values_list('user_id', flat=True))

    def get_valid_role_ids(self, role_ids: List[str]) -> List[str]:
        from ib_iam.models import Role
        return list(Role.objects.filter(
            role_id__in=role_ids).values_list('role_id', flat=True))

    def is_user_admin(self, user_id: str) -> bool:
        from ib_iam.models.user import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        return user.is_admin

    def is_user_exist(self, user_id: str) -> bool:
        from ib_iam.models import UserDetails
        is_exists = UserDetails.objects.filter(user_id=user_id).exists()
        return is_exists

    def get_role_objs_ids(self, role_ids: List[str]) -> List[str]:
        from ib_iam.models import Role
        role_obj_ids = Role.objects.filter(role_id__in=role_ids) \
            .values_list('id', flat=True)
        return role_obj_ids

    def check_are_valid_role_ids(self, role_ids):
        from ib_iam.models import Role
        role_objs_count = Role.objects.filter(
            role_id__in=role_ids).count()
        are_exists = role_objs_count == len(role_ids)
        return are_exists

    def check_is_exists_company_id(self, company_id):
        from ib_iam.models import Company
        is_exist = Company.objects.filter(company_id=company_id).exists()
        return is_exist

    def check_are_valid_team_ids(self, team_ids):
        from ib_iam.models import Team
        team_objs_count = Team.objects.filter(
            team_id__in=team_ids).count()
        are_exists = team_objs_count == len(team_ids)
        return are_exists

    def remove_roles_for_user(self, user_id: str):
        from ib_iam.models import UserRole
        UserRole.objects.filter(user_id=user_id).delete()

    def remove_teams_for_user(self, user_id: str):
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

    def update_user_details(self, company_id: str, user_id: str, name: str):
        from ib_iam.models import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        user.company_id = company_id
        user.name = name
        user.save()

    def create_user(self, is_admin: bool, user_id: str, name: str,
                    company_id: str = None):
        from ib_iam.models import UserDetails
        UserDetails.objects.create(
            user_id=user_id, is_admin=is_admin,
            company_id=company_id, name=name
        )

    def update_user_name(self, user_id: str, name: str):
        from ib_iam.models import UserDetails
        UserDetails.objects.filter(user_id=user_id).update(name=name)

    def get_users_who_are_not_admins(
            self, offset: int, limit: int,
            name_search_query: str) -> List[UserDTO]:
        from ib_iam.models import UserDetails
        users = UserDetails.objects.filter(
            is_admin=False,
            name__icontains=name_search_query
        )[offset: offset + limit]
        user_dtos = [self._convert_to_user_dto(user_object=user_object) for
                     user_object in users]
        return user_dtos

    @staticmethod
    def _convert_to_user_dto(user_object):
        if user_object.company is None:
            user_dto = UserDTO(
                user_id=user_object.user_id, is_admin=user_object.is_admin,
                company_id="")
        else:
            user_dto = UserDTO(
                user_id=user_object.user_id, is_admin=user_object.is_admin,
                company_id=str(user_object.company_id))
        return user_dto

    def get_total_count_of_users_for_query(self, name_search_query: str):
        from ib_iam.models import UserDetails
        total_count_of_users = \
            UserDetails.objects.filter(
                is_admin=False, name__icontains=name_search_query
            ).count()
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
        role_dtos = [self._convert_to_user_role_dto(user_role)
                     for user_role in user_roles]
        return role_dtos

    @staticmethod
    def _convert_to_user_role_dto(user_role):
        role = user_role.role
        return UserRoleDTO(
            user_id=user_role.user_id, role_id=role.role_id,
            name=role.name, description=role.description)

    def get_company_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserCompanyDTO]:
        from ib_iam.models import UserDetails
        user_companies = UserDetails.objects.filter(user_id__in=user_ids) \
            .select_related('company')
        user_company_dtos = [self._convert_user_company_dto(user_company)
                             for user_company in user_companies]
        return user_company_dtos

    @staticmethod
    def _convert_user_company_dto(user_company) -> UserCompanyDTO:
        company = user_company.company
        if company is None:
            return UserCompanyDTO(user_id=user_company.user_id,
                                  company_id="", company_name="")
        else:
            return UserCompanyDTO(
                user_id=user_company.user_id,
                company_id=str(company.company_id), company_name=company.name)

    def get_companies(self) -> List[CompanyIdAndNameDTO]:
        from ib_iam.models import Company
        company_query_set = Company.objects.values('company_id', 'name')
        company_dtos = [CompanyIdAndNameDTO(
            company_id=str(company_object['company_id']),
            company_name=company_object['name']) for company_object in
            company_query_set]
        return company_dtos

    def get_teams(self) -> List[TeamIdAndNameDTO]:
        from ib_iam.models import Team
        team_query_set = Team.objects.values('team_id', 'name')
        team_dtos = [TeamIdAndNameDTO(
            team_id=str(team_object['team_id']),
            team_name=team_object['name']) for team_object in team_query_set]
        return team_dtos

    def get_roles(self) -> List[RoleIdAndNameDTO]:
        from ib_iam.models import Role
        role_query_set = Role.objects.values('role_id', 'name')
        role_dtos = [RoleIdAndNameDTO(
            role_id=str(role_object['role_id']),
            name=role_object['name']) for role_object in role_query_set]
        return role_dtos

    def validate_user_id(self, user_id):
        from ib_iam.models import UserDetails
        user_details_object = UserDetails.objects.filter(user_id=user_id)
        is_user_details_object_not_exist = not user_details_object.exists()
        if is_user_details_object_not_exist:
            from ib_iam.exceptions.custom_exceptions import InvalidUserId
            raise InvalidUserId
        return

    def validate_user_ids(self, user_ids: List[str]):
        from ib_iam.models import UserDetails
        valid_user_ids = UserDetails.objects.filter(
            user_id__in=user_ids
        ).values_list("user_id", flat=True)
        invalid_user_ids = [
            user_id
            for user_id in user_ids if user_id not in valid_user_ids
        ]
        if invalid_user_ids:
            from ib_iam.exceptions.custom_exceptions import InvalidUserIds
            raise InvalidUserIds(user_ids=invalid_user_ids)
        return

    def get_valid_user_ids(self, user_ids: List[str]) -> List[str]:
        from ib_iam.models import UserDetails
        valid_user_ids = UserDetails.objects.filter(
            user_id__in=user_ids
        ).values_list("user_id", flat=True)
        return list(valid_user_ids)

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

    def get_valid_user_ids_among_the_given_user_ids(self, user_ids: List[str]):
        from ib_iam.models import UserDetails
        user_ids = UserDetails.objects.filter(user_id__in=user_ids) \
            .values_list('user_id', flat=True)
        return list(user_ids)

    def _convert_to_user_details_dtos(self, user_details_objects):
        user_details_dtos = [
            self._convert_to_user_details_dto(
                user_details_object=user_details_object)
            for user_details_object in user_details_objects
        ]
        return user_details_dtos

    def get_all_distinct_user_db_role_ids(self) -> List[str]:
        from ib_iam.models import UserRole
        user_roles_queryset = \
            UserRole.objects.all().distinct().values_list('role_id', flat=True)
        user_roles_list = list(user_roles_queryset)
        return user_roles_list

    def get_user_ids_for_given_role_ids(self,
                                        role_ids: List[str]) -> List[str]:
        from ib_iam.models import UserRole
        user_ids_queryset = \
            UserRole.objects.filter(
                role__in=role_ids).distinct().values_list('user_id', flat=True)
        user_ids_list = list(user_ids_queryset)
        return user_ids_list

    def get_user_ids_based_on_given_query(
            self, user_ids: List[str],
            search_query_with_pagination_dto: SearchQueryWithPaginationDTO
    ) -> List[str]:
        limit = search_query_with_pagination_dto.limit
        offset = search_query_with_pagination_dto.offset
        search_query = search_query_with_pagination_dto.search_query

        from ib_iam.models import UserDetails
        user_ids_queryset = UserDetails.objects.filter(
            name__icontains=search_query, user_id__in=user_ids,
        ).values_list('user_id', flat=True)[offset: limit + offset]

        user_ids_list = list(user_ids_queryset)
        return user_ids_list

    def get_db_role_ids(self, role_ids: List[str]) -> List[str]:
        from ib_iam.models import Role
        db_role_ids_queryset = \
            Role.objects.filter(
                role_id__in=role_ids).values_list('id', flat=True)
        db_role_ids_list = list(db_role_ids_queryset)
        return db_role_ids_list

    @staticmethod
    def _convert_to_user_details_dto(user_details_object):
        user_details_dto = UserIdAndNameDTO(
            user_id=user_details_object.user_id,
            name=user_details_object.name
        )
        return user_details_dto

    def get_user_related_team_dtos(self, user_id: str) -> List[TeamDTO]:
        from ib_iam.models import Team
        team_objects = Team.objects.filter(users__user_id=user_id)
        team_dtos = self._get_team_dtos(team_objects=team_objects)
        return team_dtos

    def get_team_user_ids_dtos(self, team_ids: List[str]) -> \
            List[TeamUserIdsDTO]:
        from ib_iam.models import UserTeam
        team_users = UserTeam.objects.filter(
            team__team_id__in=team_ids
        ).values_list('team__team_id', 'user_id')
        from collections import defaultdict
        team_user_ids_dictionary = defaultdict(list)
        for team_user in team_users:
            team_id = str(team_user[0])
            team_user_ids_dictionary[team_id].extend([team_user[1]])
        team_user_ids_dtos = [
            TeamUserIdsDTO(
                team_id=team_id,
                user_ids=team_user_ids_dictionary[team_id]
            ) for team_id in team_ids
        ]
        return team_user_ids_dtos

    def get_user_related_company_dto(self, user_id: str) -> CompanyDTO:
        from ib_iam.models import Company
        try:
            company_object = Company.objects.get(users__user_id=user_id)
        except Company.DoesNotExist:
            return None
        company_dto = self._convert_company_object_to_company_dto(
            company_object=company_object)
        return company_dto

    def get_company_employee_ids_dtos(self, company_ids: List[str]) \
            -> List[CompanyIdWithEmployeeIdsDTO]:
        from ib_iam.models import UserDetails
        company_employees = \
            UserDetails.objects.filter(company_id__in=company_ids) \
                .values_list('company_id', 'user_id')
        from collections import defaultdict
        company_employee_ids_dictionary = defaultdict(list)
        for company_employee in company_employees:
            company_id = str(company_employee[0])
            company_employee_ids_dictionary[company_id].extend([
                company_employee[1]])
        company_employee_ids_dtos = [
            CompanyIdWithEmployeeIdsDTO(
                company_id=company_id,
                employee_ids=company_employee_ids_dictionary[company_id]
            ) for company_id in company_ids
        ]
        return company_employee_ids_dtos

    @staticmethod
    def _convert_company_object_to_company_dto(company_object) -> CompanyDTO:
        company_dto = CompanyDTO(
            company_id=str(company_object.company_id),
            name=company_object.name,
            description=company_object.description,
            logo_url=company_object.logo_url)
        return company_dto

    @staticmethod
    def _get_team_dtos(team_objects):
        team_dtos = [
            TeamDTO(
                team_id=str(team_object.team_id),
                name=team_object.name,
                description=team_object.description
            )
            for team_object in team_objects
        ]
        return team_dtos
