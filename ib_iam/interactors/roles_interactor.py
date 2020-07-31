from typing import List

from ib_iam.exceptions.custom_exceptions import DuplicateRoleIds, \
    RoleIdFormatIsInvalid, \
    RoleNameIsEmpty, RoleDescriptionIsEmpty
from ib_iam.interactors.DTOs.common_dtos import UserIdWithRoleIdsDTO
from ib_iam.interactors.presenter_interfaces.add_roles_presenter_interface \
    import AddRolesPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import RoleDTO
from ib_iam.interactors.storage_interfaces.roles_storage_interface \
    import RolesStorageInterface


class RolesInteractor:

    def __init__(self, storage: RolesStorageInterface):
        self.storage = storage

    def add_roles_wrapper(self, roles: List[dict],
                          presenter: AddRolesPresenterInterface):
        response = None
        try:
            self.add_roles(roles=roles)
        except DuplicateRoleIds:
            response = presenter.raise_duplicate_role_ids_exception()
        except RoleIdFormatIsInvalid:
            response = presenter.raise_role_id_format_is_invalid_exception()
        except RoleNameIsEmpty:
            response = presenter.raise_role_name_should_not_be_empty_exception()
        except RoleDescriptionIsEmpty:
            response = presenter.raise_role_description_should_not_be_empty_exception()
        return response

    def add_roles(self, roles: List[dict]):
        role_dtos = []
        role_ids = [role['role_id'] for role in roles]
        self._validate_role_ids(role_ids=role_ids)
        for role in roles:
            self._validate_role_details(role=role)
            role_dto = RoleDTO(
                role_id=role['role_id'],
                name=role['role_name'],
                description=role['description']
            )
            role_dtos.append(role_dto)
        self.storage.create_roles(role_dtos)

    def _validate_role_details(self, role: dict):
        self._validate_role_id_format(role_id=role['role_id'])
        self._validate_role_name(role_name=role['role_name'])
        self._validate_role_description(
            role_description=role['description'])

    @staticmethod
    def _is_invalid_string(value):
        if value == '' or not isinstance(value, str):
            return True
        return False

    def _validate_role_name(self, role_name):
        is_invalid_string = self._is_invalid_string(value=role_name)
        if is_invalid_string:
            raise RoleNameIsEmpty()

    def _validate_role_description(self, role_description: str):
        is_invalid_string = self._is_invalid_string(value=role_description)
        if is_invalid_string:
            raise RoleDescriptionIsEmpty()

    @staticmethod
    def _validate_role_id_format(role_id: str):
        import re
        valid_format_pattern = '^([A-Z]+[A-Z0-9_]*)*[A-Z0-9]$'
        if not re.match(valid_format_pattern, role_id):
            raise RoleIdFormatIsInvalid()

    @staticmethod
    def _validate_role_ids(role_ids: List[int]):
        unique_role_ids = list(set(role_ids))
        if len(unique_role_ids) != len(role_ids):
            raise DuplicateRoleIds()

    def get_valid_role_ids(self, role_ids: List[str]):
        role_ids = list(set(role_ids))
        valid_role_ids = self.storage.get_valid_role_ids(role_ids=role_ids)
        return valid_role_ids

    def get_user_role_ids(self, user_id: str) -> List[str]:
        self.storage.validate_user_id(user_id=user_id)
        role_ids = self.storage.get_user_role_ids(user_id=user_id)
        return role_ids

    def get_role_ids_for_each_user_id(self, user_ids: List[str]) \
            -> List[UserIdWithRoleIdsDTO]:
        self.storage.validate_user_ids(user_ids=user_ids)
        user_id_with_role_ids_dtos \
            = self.storage.get_user_id_with_role_ids_dtos(user_ids=user_ids)
        return user_id_with_role_ids_dtos
