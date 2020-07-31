from typing import List

from ib_iam.interactors.storage_interfaces.dtos import UserIdAndNameDTO


class ServiceInterface:

    @staticmethod
    def get_valid_role_ids(role_ids: List[str]):
        from ib_iam.storages.add_roles_storage_implementation import \
            AddRolesStorageImplementation
        storage = AddRolesStorageImplementation()

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage)

        valid_role_ids = interactor.get_valid_role_ids(role_ids=role_ids)
        return valid_role_ids

    @staticmethod
    def get_user_role_ids(self, user_id: str):
        pass

    @staticmethod
    def get_user_dtos_based_on_limit_and_offset(
            limit: int, offset: int, search_query: str
    ) -> List[UserIdAndNameDTO]:
        from ib_iam.storages.get_users_list_storage_implementation import \
            GetUsersListStorageImplementation
        storage = GetUsersListStorageImplementation()

        from ib_iam.interactors.get_users_list_interactor import \
            GetUsersDetailsInteractor
        interactor = GetUsersDetailsInteractor(storage=storage)

        user_details_dtos = interactor.get_user_dtos_based_on_limit_and_offset(
            limit=limit, offset=offset, search_query=search_query
        )
        return user_details_dtos

    @staticmethod
    def get_all_user_dtos_based_on_query(search_query: str) -> \
            List[UserIdAndNameDTO]:
        from ib_iam.storages.get_users_list_storage_implementation import \
            GetUsersListStorageImplementation
        storage = GetUsersListStorageImplementation()

        from ib_iam.interactors.get_users_list_interactor import \
            GetUsersDetailsInteractor
        interactor = GetUsersDetailsInteractor(storage=storage)

        user_details_dtos = interactor.get_all_user_dtos_based_on_query(
            search_query=search_query
        )
        return user_details_dtos
