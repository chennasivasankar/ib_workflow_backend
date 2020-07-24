from typing import List

from ib_iam.app_interfaces.dtos import UserDTO
from ib_iam.storages.storage_implementation import StorageImplementation


class ServiceInterface:

    @staticmethod
    def get_valid_role_ids(role_ids: List[str]):
        from ib_iam.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage)

        valid_role_ids = interactor.get_valid_role_ids(role_ids=role_ids)
        return valid_role_ids

    @staticmethod
    def get_user_role_ids(self, user_id: str):
        pass

    @staticmethod
    def get_user_dtos_based_on_limit_and_offset(limit: int, offset: int, search_query: str) \
            -> List[UserDTO]:
        storage = StorageImplementation()

        user_dtos = storage.get_user_dtos_based_on_limit_and_offset(limit=limit,
                                                                    offset=offset,
                                                                    search_query=
                                                         search_query)
        return user_dtos

    @staticmethod
    def get_all_user_dtos_based_on_query(search_query: str) -> \
            List[UserDTO]:
        storage = StorageImplementation()

        user_dtos = storage.get_all_user_dtos_based_on_query(
            search_query=
            search_query)
        return user_dtos
