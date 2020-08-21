from typing import List, Optional

from ib_iam.adapters.dtos import UserProfileDTO, SearchQueryWithPaginationDTO
from ib_iam.interactors.dtos.dtos import UserIdWithRoleIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import UserIdAndNameDTO


class ServiceInterface:
    @staticmethod
    def get_valid_role_ids(role_ids: List[str]) -> List[str]:
        from ib_iam.storages.roles_storage_implementation import \
            RolesStorageImplementation
        storage = RolesStorageImplementation()

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage)

        valid_role_ids = interactor.get_valid_role_ids(role_ids=role_ids)
        return valid_role_ids

    @staticmethod
    def get_user_role_ids(user_id: str) -> List[str]:
        from ib_iam.storages.roles_storage_implementation import \
            RolesStorageImplementation
        storage = RolesStorageImplementation()

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage)

        role_ids = interactor.get_user_role_ids(user_id=user_id)
        return role_ids

    @staticmethod
    def get_users_role_ids(user_ids: List[str]) -> List[UserIdWithRoleIdsDTO]:
        from ib_iam.storages.roles_storage_implementation import \
            RolesStorageImplementation
        storage = RolesStorageImplementation()

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage)

        user_id_with_role_ids_dtos = interactor.get_role_ids_for_each_user_id(
            user_ids=user_ids)
        return user_id_with_role_ids_dtos

    @staticmethod
    def get_user_details_bulk(user_ids: List[str]) -> List[UserProfileDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        storage = UserStorageImplementation()

        from ib_iam.interactors.get_users_list_interactor import \
            GetListOfUsersInteractor
        interactor = GetListOfUsersInteractor(user_storage=storage)

        user_dtos = interactor.get_user_dtos(user_ids=user_ids)
        return user_dtos

    @staticmethod
    def get_valid_user_ids(user_ids: List[str]) -> List[str]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        storage = UserStorageImplementation()

        from ib_iam.interactors.get_users_list_interactor import \
            GetListOfUsersInteractor
        interactor = GetListOfUsersInteractor(user_storage=storage)

        valid_user_ids = interactor.get_valid_user_ids(user_ids=user_ids)
        return valid_user_ids

    @staticmethod
    def get_user_dtos_based_on_limit_and_offset(
            limit: int, offset: int, search_query: str
    ) -> List[UserIdAndNameDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        storage = UserStorageImplementation()

        from ib_iam.interactors.get_users_list_interactor import \
            GetListOfUsersInteractor
        interactor = GetListOfUsersInteractor(user_storage=storage)

        user_details_dtos = interactor.get_user_dtos_based_on_limit_and_offset(
            limit=limit, offset=offset, search_query=search_query)
        return user_details_dtos

    @staticmethod
    def get_all_user_dtos_based_on_query(search_query: str) -> \
            List[UserIdAndNameDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        storage = UserStorageImplementation()

        from ib_iam.interactors.get_users_list_interactor import \
            GetListOfUsersInteractor
        interactor = GetListOfUsersInteractor(user_storage=storage)

        user_details_dtos = interactor.get_all_user_dtos_based_on_query(
            search_query=search_query)
        return user_details_dtos

    @staticmethod
    def get_user_details_for_given_role_ids(
            role_ids: List[str]) -> List[UserProfileDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()

        from ib_iam.interactors.get_users_list_interactor import \
            GetListOfUsersInteractor
        interactor = GetListOfUsersInteractor(user_storage=user_storage)

        user_details_dtos = interactor.get_user_details_for_given_role_ids(
            role_ids=role_ids)
        return user_details_dtos

    @staticmethod
    def get_user_details_for_the_given_role_ids_based_on_query(
            role_ids: List[str],
            search_query_with_pagination_dto:
            SearchQueryWithPaginationDTO
    ) -> List[UserProfileDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()

        from ib_iam.interactors.get_users_list_interactor import \
            GetListOfUsersInteractor
        interactor = GetListOfUsersInteractor(user_storage=user_storage)

        user_details_dtos = \
            interactor.get_user_details_for_given_role_ids_based_on_query(
                role_ids=role_ids,
                search_query_with_pagination_dto=
                search_query_with_pagination_dto)
        return user_details_dtos

    @staticmethod
    def get_search_users(offset: int, limit: int, search_query: str):
        from ib_iam.storages.elastic_storage_implementation \
            import ElasticStorageImplementation
        elastic_storage = ElasticStorageImplementation()
        from ib_iam.interactors.get_search_results_interactor \
            import GetSearchResultsInteractor
        interactor = GetSearchResultsInteractor(
            elastic_storage=elastic_storage)

        return interactor.search_users_results(
            offset=offset, limit=limit, search_query=search_query
        )

    @staticmethod
    def get_search_countries(offset: int, limit: int, search_query: str):
        from ib_iam.storages.elastic_storage_implementation \
            import ElasticStorageImplementation
        elastic_storage = ElasticStorageImplementation()
        from ib_iam.interactors.get_search_results_interactor \
            import GetSearchResultsInteractor
        interactor = GetSearchResultsInteractor(
            elastic_storage=elastic_storage)
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
    def get_immediate_superior_user_id(team_id: str, user_id: str) -> \
            Optional[str]:
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        team_member_level_storage = TeamMemberLevelStorageImplementation()
        from ib_iam.interactors.get_team_members_of_level_hierarchy_interactor import \
            GetTeamMembersOfLevelHierarchyInteractor
        interactor = GetTeamMembersOfLevelHierarchyInteractor(
            team_member_level_storage=team_member_level_storage
        )
        immediate_superion_user_id = interactor.get_immediate_superior_user_id(
            team_id=team_id, user_id=user_id
        )
        return immediate_superion_user_id
