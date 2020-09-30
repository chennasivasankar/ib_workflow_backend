from typing import List, Optional

from ib_iam.adapters.dtos import UserProfileDTO, SearchQueryWithPaginationDTO, \
    UserProfileWithRolesDTO
from ib_iam.app_interfaces.dtos import UserTeamsDTO, ProjectTeamsAndUsersDTO, \
    SearchableDTO, ProjectTeamUserDTO
from ib_iam.interactors.dtos.dtos import UserIdWithRoleIdsDTO, \
    UserIdWithProjectIdAndStatusDTO
from ib_iam.interactors.storage_interfaces.dtos import UserIdAndNameDTO, \
    TeamIdAndNameDTO, ProjectDTO, TeamWithUserIdDTO, \
    MemberIdWithSubordinateMemberIdsDTO, ProjectRolesDTO
from ib_tasks.adapters.dtos import SearchableDetailsDTO


class ServiceInterface:

    @staticmethod
    def get_valid_role_ids(role_ids: List[str]) -> List[str]:
        from ib_iam.storages.roles_storage_implementation import \
            RolesStorageImplementation
        from ib_iam.interactors.roles_interactor import RolesInteractor

        storage = RolesStorageImplementation()
        interactor = RolesInteractor(storage=storage)
        valid_role_ids = interactor.get_valid_role_ids(role_ids=role_ids)

        return valid_role_ids

    @staticmethod
    def get_user_role_ids(user_id: str) -> List[str]:
        from ib_iam.storages.roles_storage_implementation import \
            RolesStorageImplementation
        from ib_iam.interactors.roles_interactor import RolesInteractor

        storage = RolesStorageImplementation()
        interactor = RolesInteractor(storage=storage)
        role_ids = interactor.get_user_role_ids(user_id=user_id)

        return role_ids

    @staticmethod
    def get_users_role_ids(user_ids: List[str]) -> List[UserIdWithRoleIdsDTO]:
        from ib_iam.storages.roles_storage_implementation import \
            RolesStorageImplementation
        from ib_iam.interactors.roles_interactor import RolesInteractor

        storage = RolesStorageImplementation()
        interactor = RolesInteractor(storage=storage)
        user_id_with_role_ids_dtos = interactor.get_role_ids_for_each_user_id(
            user_ids=user_ids
        )

        return user_id_with_role_ids_dtos

    @staticmethod
    def get_user_details_bulk(user_ids: List[str]) -> List[UserProfileDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.interactors.users.get_users_list_interactor import \
            GetListOfUsersInteractor

        storage = UserStorageImplementation()
        interactor = GetListOfUsersInteractor(user_storage=storage)
        user_dtos = interactor.get_user_dtos(user_ids=user_ids)

        return user_dtos

    @staticmethod
    def get_valid_user_ids(user_ids: List[str]) -> List[str]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.interactors.users.get_users_list_interactor import \
            GetListOfUsersInteractor

        storage = UserStorageImplementation()
        interactor = GetListOfUsersInteractor(user_storage=storage)
        valid_user_ids = interactor.get_valid_user_ids(user_ids=user_ids)

        return valid_user_ids

    @staticmethod
    def get_user_dtos_based_on_limit_and_offset(
            limit: int, offset: int, search_query: str
    ) -> List[UserIdAndNameDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.interactors.users.get_users_list_interactor import \
            GetListOfUsersInteractor

        storage = UserStorageImplementation()
        interactor = GetListOfUsersInteractor(user_storage=storage)
        user_details_dtos = interactor.get_user_dtos_based_on_limit_and_offset(
            limit=limit, offset=offset, search_query=search_query
        )

        return user_details_dtos

    @staticmethod
    def get_all_user_dtos_based_on_query(
            search_query: str
    ) -> List[UserIdAndNameDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.interactors.users.get_users_list_interactor import \
            GetListOfUsersInteractor

        storage = UserStorageImplementation()
        interactor = GetListOfUsersInteractor(user_storage=storage)
        user_details_dtos = interactor.get_all_user_dtos_based_on_query(
            search_query=search_query
        )

        return user_details_dtos

    @staticmethod
    def get_user_details_for_given_role_ids(
            role_ids: List[str], project_id: str
    ) -> List[UserProfileDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.interactors.users.get_users_list_interactor import \
            GetListOfUsersInteractor

        user_storage = UserStorageImplementation()
        interactor = GetListOfUsersInteractor(user_storage=user_storage)
        user_details_dtos = interactor.get_user_details_for_given_role_ids(
            role_ids=role_ids, project_id=project_id
        )

        return user_details_dtos

    @staticmethod
    def get_user_details_with_roles_for_given_roles(
            role_ids: List[str], project_id: str
    ) -> List[UserProfileWithRolesDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.interactors.users.get_users_list_interactor import \
            GetListOfUsersInteractor

        user_storage = UserStorageImplementation()
        interactor = GetListOfUsersInteractor(user_storage=user_storage)
        user_details_with_roles_dtos = interactor.get_user_details_with_roles(
            role_ids=role_ids, project_id=project_id)

        return user_details_with_roles_dtos

    @staticmethod
    def get_user_details_for_the_given_role_ids_based_on_query(
            role_ids: List[str], project_id: str,
            search_query_with_pagination_dto: SearchQueryWithPaginationDTO
    ) -> List[UserProfileDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.interactors.users.get_users_list_interactor import \
            GetListOfUsersInteractor

        user_storage = UserStorageImplementation()
        interactor = GetListOfUsersInteractor(user_storage=user_storage)
        user_details_dtos = \
            interactor.get_user_details_for_given_role_ids_based_on_query(
                role_ids=role_ids, project_id=project_id,
                search_query_with_pagination_dto
                =search_query_with_pagination_dto
            )

        return user_details_dtos

    @staticmethod
    def get_search_users(
            offset: int, limit: int, search_query: str
    ) -> List[str]:
        from ib_iam.storages.elastic_storage_implementation \
            import ElasticStorageImplementation
        from ib_iam.interactors.get_search_results_interactor \
            import GetSearchResultsInteractor

        elastic_storage = ElasticStorageImplementation()
        interactor = GetSearchResultsInteractor(
            elastic_storage=elastic_storage
        )

        return interactor.search_users_results(
            offset=offset, limit=limit, search_query=search_query
        )

    @staticmethod
    def get_search_countries(offset: int, limit: int, search_query: str):
        from ib_iam.storages.elastic_storage_implementation \
            import ElasticStorageImplementation
        from ib_iam.interactors.get_search_results_interactor \
            import GetSearchResultsInteractor

        elastic_storage = ElasticStorageImplementation()
        interactor = GetSearchResultsInteractor(
            elastic_storage=elastic_storage
        )

        return interactor.search_countries_results(
            offset=offset, limit=limit, search_query=search_query
        )

    @staticmethod
    def get_search_states(offset: int, limit: int, search_query: str):
        from ib_iam.storages.elastic_storage_implementation \
            import ElasticStorageImplementation
        elastic_storage = ElasticStorageImplementation()
        from ib_iam.interactors.get_search_results_interactor \
            import GetSearchResultsInteractor
        interactor = GetSearchResultsInteractor(
            elastic_storage=elastic_storage)
        return interactor.search_states_results(
            offset=offset, limit=limit, search_query=search_query
        )

    @staticmethod
    def get_search_cities(offset: int, limit: int, search_query: str):
        from ib_iam.storages.elastic_storage_implementation \
            import ElasticStorageImplementation
        elastic_storage = ElasticStorageImplementation()
        from ib_iam.interactors.get_search_results_interactor \
            import GetSearchResultsInteractor
        interactor = GetSearchResultsInteractor(
            elastic_storage=elastic_storage)
        return interactor.search_cities_results(
            offset=offset, limit=limit, search_query=search_query
        )

    @staticmethod
    def get_immediate_superior_user_id(
            team_id: str, user_id: str
    ) -> Optional[str]:
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.interactors.levels \
            .get_team_members_of_level_hierarchy_interactor import \
            GetTeamMembersOfLevelHierarchyInteractor

        team_member_level_storage = TeamMemberLevelStorageImplementation()
        user_storage = UserStorageImplementation()
        interactor = GetTeamMembersOfLevelHierarchyInteractor(
            team_member_level_storage=team_member_level_storage,
            user_storage=user_storage
        )
        immediate_superior_user_id = interactor.get_immediate_superior_user_id(
            team_id=team_id, user_id=user_id
        )

        return immediate_superior_user_id

    @staticmethod
    def get_searchable_details_dtos(
            searchable_dtos: List[SearchableDTO]
    ) -> List[SearchableDetailsDTO]:
        from ib_iam.storages.searchable_storage_implementtion import \
            SearchableStorageImplementation
        from ib_iam.interactors.get_searchable_details_interactor import \
            GetSearchableDetailsInteractor

        storage = SearchableStorageImplementation()
        interactor = GetSearchableDetailsInteractor(storage=storage)
        searchable_details_dtos = interactor.get_searchable_details_dtos(
            searchable_dtos
        )

        return searchable_details_dtos

    @staticmethod
    def get_user_role_ids_based_on_project(
            user_id: str, project_id: str
    ) -> List[str]:
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        from ib_iam.interactors.project_role_interactor import \
            ProjectRoleInteractor

        project_storage = ProjectStorageImplementation()
        interactor = ProjectRoleInteractor(project_storage=project_storage)
        role_ids = interactor.get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id
        )

        return role_ids

    @staticmethod
    def get_user_role_ids_for_given_project_ids(user_id: str, project_ids:
    List[str]) -> List[ProjectRolesDTO]:
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        from ib_iam.interactors.project_role_interactor import \
            ProjectRoleInteractor

        project_storage = ProjectStorageImplementation()
        interactor = ProjectRoleInteractor(project_storage=project_storage)
        project_roles_dtos = \
            interactor.get_user_role_ids_for_given_project_ids(
                user_id=user_id, project_ids=project_ids)
        return project_roles_dtos

    @staticmethod
    def get_valid_project_ids(project_ids: List[str]) -> List[str]:
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.interactors.project_interactor import ProjectInteractor

        project_storage = ProjectStorageImplementation()
        user_storage = UserStorageImplementation()
        team_storage = TeamStorageImplementation()
        interactor = ProjectInteractor(
            project_storage=project_storage, user_storage=user_storage,
            team_storage=team_storage
        )
        project_ids = interactor.get_valid_project_ids(project_ids=project_ids)

        return project_ids

    @staticmethod
    def get_valid_team_ids(team_ids: List[str]) -> List[str]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.interactors.team_interactor import TeamInteractor

        team_storage = TeamStorageImplementation()
        user_storage = UserStorageImplementation()
        interactor = TeamInteractor(
            team_storage=team_storage, user_storage=user_storage
        )
        team_ids = interactor.get_valid_team_ids(team_ids=team_ids)

        return team_ids

    @staticmethod
    def get_team_details_bulk(team_ids: List[str]) -> List[TeamIdAndNameDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.interactors.team_interactor import TeamInteractor

        user_storage = UserStorageImplementation()
        team_storage = TeamStorageImplementation()
        interactor = TeamInteractor(
            user_storage=user_storage, team_storage=team_storage
        )

        return interactor.get_team_id_and_name_dtos(team_ids=team_ids)

    @staticmethod
    def get_project_dtos_bulk(project_ids: List[str]) -> List[ProjectDTO]:
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.interactors.project_interactor import ProjectInteractor

        project_storage = ProjectStorageImplementation()
        user_storage = UserStorageImplementation()
        team_storage = TeamStorageImplementation()
        interactor = ProjectInteractor(
            project_storage=project_storage, user_storage=user_storage,
            team_storage=team_storage
        )

        return interactor.get_project_dtos_bulk(project_ids=project_ids)

    @staticmethod
    def get_user_teams_for_each_project_user(
            user_ids: List[str], project_id: str
    ) -> List[UserTeamsDTO]:
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.interactors.project_interactor import ProjectInteractor

        user_storage = UserStorageImplementation()
        team_storage = TeamStorageImplementation()
        project_storage = ProjectStorageImplementation()
        interactor = ProjectInteractor(
            user_storage=user_storage, team_storage=team_storage,
            project_storage=project_storage
        )

        return interactor.get_user_teams_for_each_project_user(
            user_ids=user_ids, project_id=project_id)

    @staticmethod
    def get_team_details_for_given_project_team_user_details_dto(
            project_team_user_dto: ProjectTeamUserDTO) -> TeamWithUserIdDTO:
        # todo tests has to be written for this after
        #  confirming if it is going to be used or not
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.interactors.project_interactor import ProjectInteractor

        interactor = ProjectInteractor(
            project_storage=ProjectStorageImplementation(),
            user_storage=UserStorageImplementation(),
            team_storage=TeamStorageImplementation()
        )

        return \
            interactor.get_team_details_for_given_project_team_user_details_dto(
                project_team_user_dto=project_team_user_dto)

    @staticmethod
    def get_user_team_dtos_for_given_project_teams_and_users_details_dto(
            project_teams_and_users_dto: ProjectTeamsAndUsersDTO
    ) -> List[TeamWithUserIdDTO]:
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.interactors.project_interactor import ProjectInteractor

        project_storage = ProjectStorageImplementation()
        user_storage = UserStorageImplementation()
        team_storage = TeamStorageImplementation()
        interactor = ProjectInteractor(
            project_storage=project_storage, user_storage=user_storage,
            team_storage=team_storage
        )
        user_id_with_team_id_and_name_dtos = interactor. \
            get_user_team_dtos_for_given_project_teams_and_users_details_dto(
            project_teams_and_users_dto=project_teams_and_users_dto
        )

        return user_id_with_team_id_and_name_dtos

    @staticmethod
    def is_valid_user_id_for_given_project(
            user_id: str, project_id: str
    ) -> bool:
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.interactors.project_interactor import ProjectInteractor

        project_storage = ProjectStorageImplementation()
        user_storage = UserStorageImplementation()
        team_storage = TeamStorageImplementation()
        interactor = ProjectInteractor(
            project_storage=project_storage, user_storage=user_storage,
            team_storage=team_storage
        )

        return interactor.is_valid_user_id_for_given_project(
            user_id=user_id, project_id=project_id
        )

    @staticmethod
    def get_user_status_for_given_projects(
            user_id: str, project_ids: List[str]
    ) -> List[UserIdWithProjectIdAndStatusDTO]:
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.interactors.project_interactor import ProjectInteractor

        project_storage = ProjectStorageImplementation()
        user_storage = UserStorageImplementation()
        team_storage = TeamStorageImplementation()
        interactor = ProjectInteractor(
            project_storage=project_storage, user_storage=user_storage,
            team_storage=team_storage
        )

        return interactor.get_user_status_for_given_projects(
            user_id=user_id, project_ids=project_ids
        )

    @staticmethod
    def get_project_role_ids(project_id: str) -> List[str]:
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.interactors.project_interactor import ProjectInteractor

        user_storage = UserStorageImplementation()
        team_storage = TeamStorageImplementation()
        project_storage = ProjectStorageImplementation()
        interactor = ProjectInteractor(
            project_storage=project_storage, user_storage=user_storage,
            team_storage=team_storage
        )
        project_role_ids = interactor.get_project_role_ids(
            project_id=project_id
        )

        return project_role_ids

    @staticmethod
    def get_user_id_with_subordinate_user_ids_dto(user_id: str,
                                                  project_id: str) -> \
            MemberIdWithSubordinateMemberIdsDTO:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        team_member_level_storage = TeamMemberLevelStorageImplementation()

        from ib_iam.interactors.levels.get_team_member_levels_with_members_interactor import \
            GetTeamMemberLevelsWithMembersInteractor
        interactor = GetTeamMemberLevelsWithMembersInteractor(
            user_storage=user_storage,
            team_member_level_storage=team_member_level_storage
        )
        member_id_with_subordinate_member_ids_dto = \
            interactor.get_user_id_with_subordinate_user_ids_dto(
                user_id=user_id, project_id=project_id
            )
        return member_id_with_subordinate_member_ids_dto

    @staticmethod
    def is_user_in_a_least_level(user_id: str, project_id: str) -> bool:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        team_member_level_storage = TeamMemberLevelStorageImplementation()

        from ib_iam.interactors.levels.get_team_member_levels_with_members_interactor import \
            GetTeamMemberLevelsWithMembersInteractor
        interactor = GetTeamMemberLevelsWithMembersInteractor(
            user_storage=user_storage,
            team_member_level_storage=team_member_level_storage
        )
        is_user_in_a_least_level = \
            interactor.is_user_in_a_least_level(
                user_id=user_id, project_id=project_id
            )
        return is_user_in_a_least_level

    @staticmethod
    def get_projects_task_assignee_config():
        from ib_iam.constants.config import PROJECTS_CONFIG
        return PROJECTS_CONFIG
