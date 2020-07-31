from typing import List

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.DTOs.common_dtos import UserIdWithRoleIdsDTO


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
    def get_user_role_ids(user_id: str) -> List[str]:
        from ib_iam.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage)

        role_ids = interactor.get_user_role_ids(user_id=user_id)
        return role_ids

    @staticmethod
    def get_users_role_ids(user_ids: List[str]) -> List[UserIdWithRoleIdsDTO]:
        from ib_iam.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage)

        user_id_with_role_ids_dtos = interactor.get_role_ids_for_each_user_id(
            user_ids=user_ids
        )
        return user_id_with_role_ids_dtos

    @staticmethod
    def get_user_details_bulk(user_ids: List[str]) -> List[UserProfileDTO]:
        from ib_iam.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        from ib_iam.interactors.get_users_details_inteactor import \
            GetUsersDetailsInteractor
        interactor = GetUsersDetailsInteractor(storage=storage)

        user_dtos = interactor.get_user_dtos(user_ids=user_ids)
        return user_dtos

    @staticmethod
    def get_valid_user_ids(user_ids: List[str]) -> List[str]:
        from ib_iam.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        from ib_iam.interactors.get_users_details_inteactor import \
            GetUsersDetailsInteractor
        interactor = GetUsersDetailsInteractor(storage=storage)

        valid_user_ids = interactor.get_valid_user_ids(user_ids=user_ids)
        return valid_user_ids
