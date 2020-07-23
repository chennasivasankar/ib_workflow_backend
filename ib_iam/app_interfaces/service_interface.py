from typing import List


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
    def get_user_role_ids(user_id: str):
        from ib_iam.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage)

        role_ids = interactor.get_user_role_ids(user_id=user_id)
        return role_ids

    @staticmethod
    def get_users_role_ids(user_ids: str):
        pass