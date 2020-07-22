from typing import List, Optional
import collections

from ib_tasks.interactors.storage_interfaces.dtos import FieldRolesDTO
from ib_tasks.exceptions.fields_custom_exceptions import (
    EmptyValueForPermissions,
    InvalidFieldRolesException,
    DuplicationOfPermissionRoles
)
from ib_tasks.adapters.roles_service_adapter \
    import get_roles_service_adapter


class FieldsRolesValidationsInteractor:

    def fields_roles_validations(
            self, field_roles_dtos: List[FieldRolesDTO]
    ):
        self._check_read_permission_roles_empty(field_roles_dtos)
        self._check_write_permission_roles_empty(field_roles_dtos)
        self._check_for_duplication_of_read_permissions(field_roles_dtos)
        self._check_for_duplication_of_write_permissions(field_roles_dtos)
        role_ids = self._get_all_role_ids(field_roles_dtos)
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        valid_role_ids = \
            roles_service.get_valid_role_ids_in_given_role_ids(role_ids)
        self._validate_read_permission_roles(field_roles_dtos, valid_role_ids)
        self._validate_write_permission_roles(field_roles_dtos, valid_role_ids)

    @staticmethod
    def _get_all_role_ids(field_roles_dtos: List[FieldRolesDTO]):
        role_ids = []
        for field_roles_dto in field_roles_dtos:
            read_permission_roles = field_roles_dto.read_permission_roles
            write_permission_roles = field_roles_dto.write_permission_roles
            role_ids = role_ids + read_permission_roles + write_permission_roles

    @staticmethod
    def _check_read_permission_roles_empty(
            field_roles_dtos: List[FieldRolesDTO]
    ) -> Optional[EmptyValueForPermissions]:

        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_READ_PERMISSIONS
        field_ids = []
        for field_roles_dto in field_roles_dtos:
            is_read_permissions_empty = \
                not field_roles_dto.read_permission_roles
            if is_read_permissions_empty:
                field_ids.append(field_roles_dto.field_id)

        if field_ids:
            raise EmptyValueForPermissions(
                EMPTY_VALUE_FOR_READ_PERMISSIONS.format(field_ids)
            )
        return

    @staticmethod
    def _check_write_permission_roles_empty(
            field_roles_dtos: List[FieldRolesDTO]
    ) -> Optional[EmptyValueForPermissions]:

        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_WRITE_PERMISSIONS
        field_ids = []
        for field_roles_dto in field_roles_dtos:
            is_write_permissions_empty = \
                not field_roles_dto.write_permission_roles
            if is_write_permissions_empty:
                field_ids.append(field_roles_dto.field_id)

        if field_ids:
            raise EmptyValueForPermissions(
                EMPTY_VALUE_FOR_WRITE_PERMISSIONS.format(field_ids)
            )
        return

    def _check_for_duplication_of_read_permissions(
            self, field_roles_dtos: List[FieldRolesDTO]
    ) -> Optional[DuplicationOfPermissionRoles]:

        from ib_tasks.constants.exception_messages \
            import DUPLICATED_VALUES_FOR_READ_PERMISSIONS

        duplication_of_read_permission_roles = []
        for field_roles_dto in field_roles_dtos:
            read_permissions_roles = field_roles_dto.read_permission_roles
            duplication_of_roles = \
                self._get_duplication_of_roles(read_permissions_roles)
            if duplication_of_roles:
                duplication_of_roles_dict = {
                    "field_id": field_roles_dto.field_id,
                    "duplication_values_for_read_permissions": duplication_of_roles
                }
                duplication_of_read_permission_roles.append(
                    duplication_of_roles_dict
                )

        if duplication_of_read_permission_roles:
            raise DuplicationOfPermissionRoles(
                DUPLICATED_VALUES_FOR_READ_PERMISSIONS.format(
                    duplication_of_read_permission_roles
                )
            )
        return

    def _check_for_duplication_of_write_permissions(
            self, field_roles_dtos: List[FieldRolesDTO]
    ) -> Optional[DuplicationOfPermissionRoles]:

        from ib_tasks.constants.exception_messages \
            import DUPLICATED_VALUES_FOR_WRITE_PERMISSIONS

        duplication_of_write_permission_roles = []
        for field_roles_dto in field_roles_dtos:
            write_permissions_roles = field_roles_dto.write_permission_roles
            duplication_of_roles = self._get_duplication_of_roles(
                write_permissions_roles
            )
            if duplication_of_roles:
                duplication_of_roles_dict = {
                    "field_id": field_roles_dto.field_id,
                    "duplication_values_for_write_permissions": duplication_of_roles
                }
                duplication_of_write_permission_roles.\
                    append(duplication_of_roles_dict)

        if duplication_of_write_permission_roles:
            raise DuplicationOfPermissionRoles(
                DUPLICATED_VALUES_FOR_WRITE_PERMISSIONS.format(
                    duplication_of_write_permission_roles
                )
            )
        return

    def _get_duplication_of_roles(self, permissions_roles: List[str]):
        duplication_of_roles = [
            role
            for role, count in collections.Counter(permissions_roles).items()
            if count > 1
        ]
        return duplication_of_roles

    def _validate_read_permission_roles(
            self, field_roles_dtos: List[FieldRolesDTO],
            valid_role_ids: List[str]
    ):
        fields_invalid_roles_for_read_permission = []
        for field_roles_dto in field_roles_dtos:
            read_permission_roles = field_roles_dto.read_permission_roles
            invalid_roles_dict = self._validate_roles(
                valid_role_ids, read_permission_roles, field_roles_dto
            )
            if invalid_roles_dict:
                invalid_roles_dict["permissions"] = "read_permissions"
                fields_invalid_roles_for_read_permission.append(
                    invalid_roles_dict
                )
        if fields_invalid_roles_for_read_permission:
            raise InvalidFieldRolesException(
                fields_invalid_roles_for_read_permission
            )
        return

    def _validate_write_permission_roles(
            self, field_roles_dtos: List[FieldRolesDTO],
            valid_role_ids: List[str]
    ):

        fields_invalid_roles_for_write_permission = []
        for field_roles_dto in field_roles_dtos:
            write_permission_roles = field_roles_dto.write_permission_roles
            invalid_roles_dict = self._validate_roles(
                valid_role_ids, write_permission_roles, field_roles_dto
            )
            if invalid_roles_dict:
                invalid_roles_dict["permissions"] = "write_permissions"
                fields_invalid_roles_for_write_permission. \
                    append(invalid_roles_dict)
        if fields_invalid_roles_for_write_permission:
            raise InvalidFieldRolesException(
                fields_invalid_roles_for_write_permission
            )
        return

    def _validate_roles(
            self, valid_role_ids: List[str],
            permission_roles: List[str], field_roles_dto: FieldRolesDTO
    ):
        field_id = field_roles_dto.field_id
        invalid_roles = []
        field_with_invalid_roles = {}
        for role in permission_roles:
            if role not in valid_role_ids:
                invalid_roles.append(role)
        if invalid_roles:
            field_with_invalid_roles["field_id"] = field_id
            field_with_invalid_roles['invalid_roles'] = invalid_roles

        return field_with_invalid_roles
