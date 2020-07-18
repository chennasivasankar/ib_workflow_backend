from typing import List, Optional
from ib_tasks.interactors.storage_interfaces.dtos import FieldRolesDTO
from ib_tasks.exceptions.custom_exceptions import (
    EmptyValueForPermissions,
    InvalidRolesException
)

class FieldsRolesValidationsInteractor:

    def fields_roles_validations(self, field_roles_dtos: List[FieldRolesDTO]):
        self._check_permissions_to_roles_contains_empty_values(field_roles_dtos)
        self._validate_read_permission_roles(field_roles_dtos)
        self._validate_write_permission_roles(field_roles_dtos)


    def _check_permissions_to_roles_contains_empty_values(
            self, field_roles_dtos: List[FieldRolesDTO]
    ) -> Optional[EmptyValueForPermissions]:

        from ib_tasks.constants.exception_messages \
            import EMPTY_VALUE_FOR_PERMISSIONS
        for field_roles_dto in field_roles_dtos:
            is_read_permissions_empty = \
                not field_roles_dto.read_permission_roles
            is_write_permissions_empty = \
                not field_roles_dto.write_permission_roles
            if is_read_permissions_empty or is_write_permissions_empty:
                raise EmptyValueForPermissions(EMPTY_VALUE_FOR_PERMISSIONS)
        return


    def _validate_read_permission_roles(
            self, field_roles_dtos: List[FieldRolesDTO]
    ):
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        valid_read_permission_roles = \
            roles_service.get_all_valid_read_permission_roles()
        self._check_invalid_roles_for_read_permissions_in_field_dtos(
            field_roles_dtos, valid_read_permission_roles
        )

    def _check_invalid_roles_for_read_permissions_in_field_dtos(
            self, field_roles_dtos: List[FieldRolesDTO],
            available_read_permission_roles: List[str]
    ) -> Optional[InvalidRolesException]:

        fields_invalid_roles_for_read_permission = []
        for field_roles_dto in field_roles_dtos:
            read_permission_roles = field_roles_dto.read_permission_roles
            invalid_roles_dict = self._validate_roles(
                available_read_permission_roles,
                read_permission_roles, field_roles_dto
            )
            if invalid_roles_dict:
                invalid_roles_dict["permissions"] = "read_permissions"
                fields_invalid_roles_for_read_permission.append(
                    invalid_roles_dict
                )
        if fields_invalid_roles_for_read_permission:
            raise InvalidRolesException(
                fields_invalid_roles_for_read_permission
            )
        return


    def _validate_write_permission_roles(
            self, field_roles_dtos: List[FieldRolesDTO]
    ):
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        valid_write_permission_roles = \
            roles_service.get_all_valid_write_permission_roles()
        self._check_invalid_roles_for_write_permissions_in_field_dtos(
            field_roles_dtos, valid_write_permission_roles
        )



    def _check_invalid_roles_for_write_permissions_in_field_dtos(
            self, field_roles_dtos: List[FieldRolesDTO],
            available_write_permission_roles: List[str]
    ) -> Optional[InvalidRolesException]:
        fields_invalid_roles_for_write_permission = []
        for field_roles_dto in field_roles_dtos:
            write_permission_roles = field_roles_dto.write_permission_roles
            invalid_roles_dict = self._validate_roles(
                available_write_permission_roles,
                write_permission_roles, field_roles_dto
            )
            if invalid_roles_dict:
                invalid_roles_dict["permissions"] = "write_permissions"
                fields_invalid_roles_for_write_permission. \
                    append(invalid_roles_dict)
        if fields_invalid_roles_for_write_permission:
            raise InvalidRolesException(
                fields_invalid_roles_for_write_permission
            )
        return

    def _validate_roles(
            self, available_roles: List[str],
            permission_roles: List[str], field_roles_dto: FieldRolesDTO
    ):
        field_id = field_roles_dto.field_id
        invalid_roles = []
        field_with_invalid_roles = {}
        for role in permission_roles:
            if role not in available_roles:
                invalid_roles.append(role)
        if invalid_roles:
            field_with_invalid_roles["field_id"] = field_id
            field_with_invalid_roles['invalid_roles'] = invalid_roles

        return field_with_invalid_roles