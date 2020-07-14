from typing import List

from ib_iam.interactors.storage_interfaces.dtos import RoleDto
from ib_iam.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_iam.interactors.presenter_interfaces.presenter_interface \
    import PresenterInterface


class RoleIdIsEmptyException(Exception):
    pass


class RoleNameIsEmptyException(Exception):
    pass


class RoleDescriptionIsEmptyException(Exception):
    pass


def check_is_value_valid(value: str):
    if value == '':
        return False
    return True


class RoleIdFormatIsInvalid(Exception):
    pass


class InvalidRoleIdException(Exception):
    pass


class DuplicateRoleIdsException(Exception):
    pass


class AddRolesInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_roles_wrapper(self, roles: List,
                          presenter: PresenterInterface):
        try:
            self.add_roles(roles=roles)
        except RoleIdFormatIsInvalid:
            return presenter.raise_role_id_format_is_invalid()
        except DuplicateRoleIdsException:
            return presenter.raise_duplicate_role_ids_exception()
        except InvalidRoleIdException:
            return presenter.raise_invalid_role_id_execption()
        except RoleIdIsEmptyException:
            return presenter.raise_role_id_should_not_be_empty()
        except RoleNameIsEmptyException:
            return presenter.raise_role_name_should_not_be_empty()
        except RoleDescriptionIsEmptyException:
            return presenter.raise_role_description_should_not_be_empty()

    def add_roles(self, roles: List):
        roles_dto_list = []
        role_ids = [role['role_id'] for role in roles]
        self.check_for_duplicate_role_ids(role_ids)
        for role in roles:
            self.check_role_id_is_string(role_id=role['role_id'])
            self.check_role_id_format(role_id=role['role_id'])
            # self.check_is_role_id_valid(role_id=role['role_id'])
            self.check_is_role_name_valid(role_name=role['role_name'])
            self.check_is_role_description_valid(
                role_description=role['role_description'])
            role_dto = RoleDto(
                role_id=role['role_id'],
                role_name=role['role_name'],
                role_description=role['role_description']
            )
            roles_dto_list.append(role_dto)
        self.storage.create_roles_from_list_of_role_dtos(roles_dto_list)

    @staticmethod
    def check_is_role_id_valid(role_id: str):
        is_valid = check_is_value_valid(value=role_id)
        is_not_valid = not is_valid
        if is_not_valid:
            raise RoleIdIsEmptyException()

    def check_is_role_name_valid(self, role_name: str):
        is_valid = check_is_value_valid(value=role_name)
        is_not_valid = not is_valid
        if is_not_valid:
            raise RoleNameIsEmptyException()

    def check_is_role_description_valid(self, role_description: str):
        is_valid = check_is_value_valid(value=role_description)
        is_not_valid = not is_valid
        if is_not_valid:
            raise RoleDescriptionIsEmptyException()

    def check_role_id_format(self, role_id: str):
        import re
        # valid_format_pattern = '^[A-Z]+\_[A-Z0-9]+[0-9]*$'
        valid_format_pattern = '^([A-Z]+|[A-Z0-9_]*)*[A-Z0-9]$'
        is_valid_format = bool(re.match(valid_format_pattern, role_id))
        print(role_id)
        is_invalid_format = not is_valid_format
        print(is_invalid_format)
        if is_invalid_format:
            raise RoleIdFormatIsInvalid()

    def check_role_id_is_string(self, role_id):
        is_string = isinstance(role_id, str)
        if not is_string:
            raise InvalidRoleIdException()

    def check_for_duplicate_role_ids(self, role_ids: List[int]):
        unique_role_ids = list(set(role_ids))

        if unique_role_ids != role_ids:
            raise DuplicateRoleIdsException()
