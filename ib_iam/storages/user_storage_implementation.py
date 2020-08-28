from typing import List, Optional

from ib_iam.adapters.dtos import SearchQueryWithPaginationDTO
from ib_iam.exceptions.custom_exceptions import InvalidUserIdsForProject, \
    InvalidRoleIdsForProject, InvalidProjectId
from ib_iam.interactors.dtos.dtos import UserIdWithRoleIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import UserDTO, UserTeamDTO, \
    UserRoleDTO, UserCompanyDTO, RoleIdAndNameDTO, TeamIdAndNameDTO, \
    CompanyIdAndNameDTO, UserIdAndNameDTO, TeamDTO, TeamUserIdsDTO, \
    CompanyDTO, \
    CompanyIdWithEmployeeIdsDTO, BasicUserDetailsDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface \
    import UserStorageInterface
from ib_iam.models import ProjectRole


class UserStorageImplementation(UserStorageInterface):

    def get_user_ids_who_are_not_admin(self) -> List[str]:
        from ib_iam.models import UserDetails
        return list(UserDetails.objects.filter(
            is_admin=False).values_list("user_id", flat=True))

    def get_user_ids(self, role_ids: List[str]) -> List[str]:
        from ib_iam.models import UserRole
        return list(UserRole.objects.filter(
            project_role__role_id__in=role_ids
        ).values_list('user_id', flat=True))

    def get_valid_role_ids(self, role_ids: List[str]) -> List[str]:
        from ib_iam.models import ProjectRole
        return list(ProjectRole.objects.filter(
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
        from ib_iam.models import ProjectRole
        role_obj_ids = ProjectRole.objects.filter(role_id__in=role_ids) \
            .values_list('id', flat=True)
        return role_obj_ids

    def check_are_valid_role_ids(self, role_ids):
        from ib_iam.models import ProjectRole
        role_objs_count = ProjectRole.objects.filter(
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
        user_roles = [UserRole(user_id=user_id, project_role_id=str(role_id))
                      for role_id in role_ids]
        UserRole.objects.bulk_create(user_roles)

    def add_user_to_the_teams(self, user_id: str, team_ids: List[str]):
        from ib_iam.models import UserTeam
        user_teams = [UserTeam(user_id=user_id, team_id=team_id)
                      for team_id in team_ids]
        UserTeam.objects.bulk_create(user_teams)

    def update_user_details(
            self, company_id: Optional[str], user_id: str, name: str):
        from ib_iam.models import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        user.company_id = company_id
        user.name = name
        user.save()

    def create_user(self, is_admin: bool, user_id: str, name: str,
                    company_id: Optional[str] = None):
        from ib_iam.models import UserDetails
        UserDetails.objects.create(
            user_id=user_id, is_admin=is_admin,
            company_id=company_id, name=name
        )

    def update_user_name_and_cover_page_url(
            self, name: str, cover_page_url: str, user_id: str):
        from ib_iam.models import UserDetails
        UserDetails.objects.filter(user_id=user_id).update(
            name=name,
            cover_page_url=cover_page_url)

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
            .select_related('project_role')
        role_dtos = [self._convert_to_user_role_dto(user_role)
                     for user_role in user_roles]
        return role_dtos

    @staticmethod
    def _convert_to_user_role_dto(user_role):
        project_role = user_role.project_role
        return UserRoleDTO(
            user_id=user_role.user_id, role_id=project_role.role_id,
            name=project_role.name, description=project_role.description)

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
            return UserCompanyDTO(user_id=user_company.user_id)
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
        from ib_iam.models import ProjectRole
        role_query_set = ProjectRole.objects.values('role_id', 'name')
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

    def get_all_distinct_user_db_role_ids(self, project_id: str) -> List[str]:
        # todo: refactor names
        user_roles_queryset = \
            ProjectRole.objects.filter(project_id=project_id).values_list(
                'role_id', flat=True)
        user_roles_list = list(user_roles_queryset)
        return user_roles_list

    def get_user_ids_for_given_role_ids(self,
                                        role_ids: List[str]) -> List[str]:
        from ib_iam.models import UserRole
        user_ids_queryset = \
            UserRole.objects.filter(
                project_role__in=role_ids).distinct().values_list(
                'user_id', flat=True)
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
        from ib_iam.models import ProjectRole
        db_role_ids_queryset = \
            ProjectRole.objects.filter(
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

    def get_company_employee_ids_dto(self, company_id: str) \
            -> CompanyIdWithEmployeeIdsDTO:
        from ib_iam.models import UserDetails
        company_employees = \
            UserDetails.objects.filter(company_id=company_id) \
                .values_list('user_id', flat=True)
        company_employee_ids_dtos = CompanyIdWithEmployeeIdsDTO(
            company_id=company_id,
            employee_ids=list(company_employees))
        return company_employee_ids_dtos

    def get_user_details(self, user_id: str) -> UserDTO:
        from ib_iam.models import UserDetails
        user_object = UserDetails.objects.get(user_id=user_id)
        user_dto = UserDTO(user_id=user_object.user_id,
                           is_admin=user_object.is_admin,
                           cover_page_url=user_object.cover_page_url)
        return user_dto

    def get_basic_user_dtos_for_given_project(self, project_id: str) -> \
            List[BasicUserDetailsDTO]:
        from ib_iam.models import UserTeam
        from ib_iam.models import UserDetails

        from ib_iam.models import ProjectTeam
        team_ids = ProjectTeam.objects.filter(
            project_id=project_id
        ).values_list(
            "team_id", flat=True
        )
        user_ids = UserTeam.objects.filter(
            team_id__in=team_ids
        ).values_list(
            "user_id", flat=True
        )
        user_ids = list(set(user_ids))
        user_details_objects = UserDetails.objects.filter(
            user_id__in=user_ids
        )
        basic_user_details_dtos = [
            BasicUserDetailsDTO(
                user_id=user_details_object.user_id,
                name=user_details_object.name
            )
            for user_details_object in user_details_objects
        ]
        return basic_user_details_dtos

    def get_user_role_dtos_of_a_project(
            self, user_ids: List[str], project_id: str) -> List[UserRoleDTO]:
        from ib_iam.models import UserRole
        user_role_list = UserRole.objects.filter(
            user_id__in=user_ids, project_role__project_id=project_id
        ).values(
            "user_id", "project_role__role_id", "project_role__name"
        )
        user_role_dtos = [
            UserRoleDTO(
                user_id=user_role_dict["user_id"],
                role_id=user_role_dict["project_role__role_id"],
                name=user_role_dict["project_role__name"]
            )
            for user_role_dict in user_role_list
        ]
        return user_role_dtos

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

    def get_user_ids_for_given_project(self, project_id: str) -> List[str]:
        # TODO need to optimize the storage calls
        from ib_iam.models import ProjectTeam
        team_ids = list(
            ProjectTeam.objects.filter(project_id=project_id).values_list(
                'team_id', flat=True))
        from ib_iam.models import UserTeam
        user_ids = list(
            UserTeam.objects.filter(team_id__in=team_ids).values_list('user_id',
                                                                      flat=True))
        return user_ids

    def add_project_specific_details(
            self, user_id_with_role_ids_dtos: List[
                UserIdWithRoleIdsDTO],
            project_id: str
    ):
        from ib_iam.models import UserRole
        UserRole.objects.filter(project_role__project_id=project_id).delete()

        total_user_role_objects_of_a_project = []

        for user_id_with_role_ids_dto in user_id_with_role_ids_dtos:
            user_role_objects = self._get_user_role_objects(
                user_id_with_role_ids_dto)
            total_user_role_objects_of_a_project.extend(user_role_objects)

        UserRole.objects.bulk_create(total_user_role_objects_of_a_project)
        return

    @staticmethod
    def _get_user_role_objects(
            user_id_with_role_ids_dto: UserIdWithRoleIdsDTO):
        role_ids = user_id_with_role_ids_dto.role_ids
        user_id = user_id_with_role_ids_dto.user_id
        from ib_iam.models import UserRole
        user_role_objects = [
            UserRole(
                user_id=user_id,
                project_role_id=role_id
            )
            for role_id in role_ids
        ]
        return user_role_objects

    def is_valid_project_id(self, project_id: str) -> bool:
        from ib_iam.models import Project
        project_objects = Project.objects.filter(project_id=project_id)
        return project_objects.exists()

    def validate_users_for_project(
            self, user_ids: List[str], project_id: str
    ) -> Optional[InvalidUserIdsForProject]:
        from ib_iam.models import ProjectTeam
        team_ids = ProjectTeam.objects.filter(
            project_id=project_id
        ).values_list(
            "team_id", flat=True)

        from ib_iam.models import UserTeam
        user_ids_in_project = UserTeam.objects.filter(
            team_id__in=team_ids
        ).values_list(
            "user_id", flat=True
        )
        invalid_user_ids = [
            user_id
            for user_id in user_ids if user_id not in user_ids_in_project
        ]
        if invalid_user_ids:
            raise InvalidUserIdsForProject(user_ids=invalid_user_ids)
        return

    def validate_role_ids_for_project(
            self, role_ids: List[str], project_id: str
    ) -> Optional[InvalidRoleIdsForProject]:
        role_ids_in_project = ProjectRole.objects.filter(
            project_id=project_id
        ).values_list(
            "role_id", flat=True
        )

        invalid_role_ids = [
            role_id
            for role_id in role_ids if role_id not in role_ids_in_project
        ]

        if invalid_role_ids:
            raise InvalidRoleIdsForProject(role_ids=invalid_role_ids)
        return

    def validate_project_id(
            self, project_id: str
    ) -> Optional[InvalidProjectId]:
        from ib_iam.models import Project
        project_objects = Project.objects.filter(project_id=project_id)
        is_project_not_exists = not project_objects.exists()
        if is_project_not_exists:
            raise InvalidProjectId
        return
