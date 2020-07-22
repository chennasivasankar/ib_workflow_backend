from typing import List, Optional
import collections

from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.dtos \
    import FieldDTO, FieldRolesDTO, FieldRoleDTO
from ib_tasks.constants.enum import FieldTypes, PermissionTypes
from ib_tasks.exceptions.custom_exceptions import (
    InvalidFieldIdException,
    DuplicationOfFieldIdsExist,
    FieldsDuplicationOfDropDownValues,
    EmptyValueForPermissions,
    InvalidValueForFieldDisplayName,
    InvalidValueForFieldType,
    InvalidGOFIds
)
from ib_tasks.interactors.create_update_delete_stage_actions import InvalidRolesException


class CreateFieldsInteractor:
    def __init__(self, storage: TaskStorageInterface):
        self.storage = storage

    def create_fields(
            self, field_dtos: List[FieldDTO],
            field_roles_dtos: List[FieldRolesDTO]
    ):
        self._validate_gof_ids(field_dtos)
        self._validate_field_id(field_dtos)
        self._check_for_duplication_of_filed_ids(field_dtos)
        self._validate_field_display_name(field_dtos)
        self._validate_field_type(field_dtos)
        self._check_for_duplication_of_drop_down_values_for_field_dtos(
            field_dtos
        )
        self._check_permissions_to_roles_contains_empty_values(field_roles_dtos)
        self._validate_read_permission_roles(field_roles_dtos)
        self._validate_write_permission_roles(field_roles_dtos)
        new_field_dtos, existing_field_dtos = self._get_field_dtos(field_dtos)
        new_field_roles_dtos, existing_field_roles_dtos = self._get_field_roles_dto(
            new_field_dtos, existing_field_dtos, field_roles_dtos
        )
        if new_field_dtos:
            self.storage.create_fields(new_field_dtos)
            new_field_role_dtos = self._get_field_role_dtos(new_field_roles_dtos)
            self.storage.create_fields_roles(new_field_role_dtos)
        if existing_field_dtos:
            self.storage.update_fields(existing_field_dtos)
            existing_field_role_dtos = self._get_field_role_dtos(existing_field_roles_dtos)
            self.storage.update_fields_roles(existing_field_role_dtos)


    def _get_field_role_dtos(
            self, field_roles_dtos: List[FieldRolesDTO]
    ) -> List[FieldRoleDTO]:
        new_field_role_dtos = []
        for field_roles_dto in field_roles_dtos:
            read_permission_field_role_dtos = \
                self._get_read_permission_field_role_dtos(field_roles_dto)
            write_permission_field_role_dtos = \
                self._get_write_permission_field_role_dtos(field_roles_dto)
            new_field_role_dtos = read_permission_field_role_dtos + write_permission_field_role_dtos
        return new_field_role_dtos


    def _get_read_permission_field_role_dtos(
            self, field_roles_dto: FieldRolesDTO
    ) -> List[FieldRoleDTO]:
        read_permission_field_role_dtos = []
        field_id = field_roles_dto.field_id
        read_permission_roles = field_roles_dto.read_permission_roles
        for role in read_permission_roles:
            field_role_dto = FieldRoleDTO(
                field_id=field_id, role=role,
                permission_type=PermissionTypes.READ.value
            )
            read_permission_field_role_dtos.append(field_role_dto)
        return read_permission_field_role_dtos

    def _get_write_permission_field_role_dtos(
            self, field_roles_dto: FieldRolesDTO
    ) -> List[FieldRoleDTO]:
        write_permission_field_role_dtos = []
        field_id = field_roles_dto.field_id
        write_permission_roles = field_roles_dto.read_permission_roles
        for role in write_permission_roles:
            field_role_dto = FieldRoleDTO(
                field_id=field_id, role=role,
                permission_type=PermissionTypes.WRITE.value
            )
            write_permission_field_role_dtos.append(field_role_dto)
        return write_permission_field_role_dtos


    def _get_field_roles_dto(
            self, new_field_dtos: List[FieldDTO],
            existing_field_dtos: List[FieldDTO],
            field_roles_dtos: List[FieldRolesDTO]
    ):
        new_field_ids = [field_dto.field_id for field_dto in new_field_dtos]
        existing_field_ids = [
            field_dto.field_id
            for field_dto in existing_field_dtos
        ]
        new_field_roles_dtos = [
            field_roles_dto
            for field_roles_dto in field_roles_dtos
            if field_roles_dto.field_id in new_field_ids
        ]
        existing_field_roles_dtos = [
            field_roles_dto
            for field_roles_dto in field_roles_dtos
            if field_roles_dto.field_id in existing_field_ids
        ]
        return new_field_roles_dtos, existing_field_roles_dtos


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

    def _validate_gof_ids(
            self, field_dtos: List[FieldDTO]
    ) -> Optional[InvalidGOFIds]:
        gof_ids = [field_dto.gof_id for field_dto in field_dtos]
        existing_gof_ids = self.storage.get_existing_gof_ids(gof_ids)
        for gof_id in gof_ids:
            if gof_id not in existing_gof_ids:
                raise InvalidGOFIds("Invalid GOF Ids")
        return

    def _get_field_dtos(self, field_dtos: List[FieldDTO]):
        updated_field_dtos = self._update_field_dtos_by_field_value(field_dtos)
        field_ids = [field_dto.field_id for field_dto in updated_field_dtos]
        existing_field_ids = self.storage.get_existing_field_ids(field_ids)
        new_field_ids = [
            field_id
            for field_id in field_ids
            if field_id not in existing_field_ids
        ]
        new_field_dtos = [
            field_dto
            for field_dto in updated_field_dtos
            if field_dto.field_id in new_field_ids
        ]
        existing_field_dtos = [
            field_dto
            for field_dto in updated_field_dtos
            if field_dto.field_id in existing_field_ids
        ]
        return new_field_dtos, existing_field_dtos

    @staticmethod
    def _update_field_dtos_by_field_value(field_dtos: List[FieldDTO]):
        for field_dto in field_dtos:
            field_values = field_dto.field_values
            if field_values and type(field_values) == list:
                import json
                field_dto.field_values = json.dumps(field_dto.field_values)
        return field_dtos

    @staticmethod
    def _validate_field_type(
            field_dtos: List[FieldDTO]
    ) -> Optional[InvalidValueForFieldType]:
        from ib_tasks.constants.constants import FIELD_TYPES_LIST
        for field_dto in field_dtos:
            field_type = field_dto.field_type
            if field_type not in FIELD_TYPES_LIST:
                raise InvalidValueForFieldType(
                    "Field_Type should be one of these {}".format(FIELD_TYPES_LIST)
                )
        return

    @staticmethod
    def _validate_field_display_name(
            field_dtos: List[FieldDTO]
    ) -> Optional[InvalidValueForFieldDisplayName]:
        for field_dto in field_dtos:
            field_display_name = field_dto.field_display_name.strip()
            is_field_display_name_empty = not field_display_name
            if is_field_display_name_empty:
                raise InvalidValueForFieldDisplayName(
                    "Field display name shouldn't be empty"
                )
        return

    @staticmethod
    def _validate_field_id(
            field_dtos: List[FieldDTO]
    ) -> Optional[InvalidFieldIdException]:

        for field_dto in field_dtos:
            field_id = field_dto.field_id.strip()
            is_field_id_empty = not field_id
            if is_field_id_empty:
                raise InvalidFieldIdException("Field Id shouldn't be empty")
        return

    @staticmethod
    def _check_for_duplication_of_filed_ids(
            field_dtos
    ) -> Optional[DuplicationOfFieldIdsExist]:
        field_ids = []
        for field_dto in field_dtos:
            field_id = field_dto.field_id
            field_ids.append(field_id)

        duplication_of_field_ids = [
            field_id
            for field_id, count in collections.Counter(field_ids).items()
            if count > 1
        ]
        if duplication_of_field_ids:
            raise DuplicationOfFieldIdsExist(duplication_of_field_ids)
        return

    def _check_for_duplication_of_drop_down_values_for_field_dtos(
            self, field_dtos: List[FieldDTO]
    ) -> Optional[FieldsDuplicationOfDropDownValues]:
        fields_with_dropdown_duplicate_values = []

        for field_dto in field_dtos:
            if field_dto.field_type == FieldTypes.DROPDOWN.value:
                field_with_dropdown_duplicate_values_dict = \
                    self._check_for_duplication_of_dropdown_values(field_dto)
                if field_with_dropdown_duplicate_values_dict:
                    fields_with_dropdown_duplicate_values.append(
                        field_with_dropdown_duplicate_values_dict
                    )

        if fields_with_dropdown_duplicate_values:
            raise FieldsDuplicationOfDropDownValues(
                fields_with_dropdown_duplicate_values
            )
        return

    def _check_for_duplication_of_dropdown_values(self, field_dto: FieldDTO):
        field_id = field_dto.field_id
        dropdown_values = field_dto.field_values
        field_with_dropdown_duplicate_values = {}

        duplications_of_dropdown_values = [
            value
            for value, count in collections.Counter(dropdown_values).items()
            if count > 1
        ]
        if duplications_of_dropdown_values:
            field_with_dropdown_duplicate_values["field_id"] = field_id
            field_with_dropdown_duplicate_values["field_type"] = \
                FieldTypes.DROPDOWN.value
            field_with_dropdown_duplicate_values["duplicate_values"] = \
                duplications_of_dropdown_values

        return field_with_dropdown_duplicate_values

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

    def _check_permissions_to_roles_contains_empty_values(
            self, field_roles_dtos: List[FieldRolesDTO]
    ) -> Optional[EmptyValueForPermissions]:
        for field_roles_dto in field_roles_dtos:
            is_read_permissions_empty = \
                not field_roles_dto.read_permission_roles
            is_write_permissions_empty = \
                not field_roles_dto.write_permission_roles
            if is_read_permissions_empty or is_write_permissions_empty:
                raise EmptyValueForPermissions(
                    "Permissions to roles shouldn't be empty"
                )
        return