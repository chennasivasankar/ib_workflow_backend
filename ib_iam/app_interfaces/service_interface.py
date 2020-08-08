from typing import List

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.DTOs.common_dtos import UserIdWithRoleIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import UserIdAndNameDTO


class ServiceInterface:

    @staticmethod
    def get_valid_role_ids(role_ids: List[str]):
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
            user_ids=user_ids
        )
        return user_id_with_role_ids_dtos

    @staticmethod
    def get_user_details_bulk(user_ids: List[str]) -> List[UserProfileDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        storage = UserStorageImplementation()

        from ib_iam.interactors.get_users_list_interactor import \
            GetUsersDetailsInteractor
        interactor = GetUsersDetailsInteractor(storage=storage)

        user_dtos = interactor.get_user_dtos(user_ids=user_ids)
        return user_dtos

    @staticmethod
    def get_valid_user_ids(user_ids: List[str]) -> List[str]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        storage = UserStorageImplementation()

        from ib_iam.interactors.get_users_list_interactor import \
            GetUsersDetailsInteractor
        interactor = GetUsersDetailsInteractor(storage=storage)

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
            GetUsersDetailsInteractor
        interactor = GetUsersDetailsInteractor(storage=storage)

        user_details_dtos = interactor.get_user_dtos_based_on_limit_and_offset(
            limit=limit, offset=offset, search_query=search_query
        )
        return user_details_dtos

    @staticmethod
    def get_all_user_dtos_based_on_query(search_query: str) -> \
            List[UserIdAndNameDTO]:
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        storage = UserStorageImplementation()

        from ib_iam.interactors.get_users_list_interactor import \
            GetUsersDetailsInteractor
        interactor = GetUsersDetailsInteractor(storage=storage)

        user_details_dtos = interactor.get_all_user_dtos_based_on_query(
            search_query=search_query
        )
        return user_details_dtos

    def get_permitted_user_details(self, role_ids: List[str]):
        pass

