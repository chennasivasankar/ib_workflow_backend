from typing import List, Optional, Union

from ib_tasks.exceptions.custom_exceptions import (
    GOFIdCantBeEmpty, GOFDisplayNameCantBeEmpty, GOFReadPermissionsCantBeEmpty,
    GOFWritePermissionsCantBeEmpty, GOFFieldIdsCantBeEmpty, DuplicatedFieldIds,
    InvalidReadPermissionRoles, InvalidWritePermissionRoles
)
from ib_tasks.interactors.storage_interfaces.dtos import CompleteGoFDetailsDTO, \
    GoFRolesDTO, GoFFieldsDTO, GoFDTO
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface


class CreateGoFsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_gof_wrapper(self):
        pass

    def create_gofs(
            self, complete_gof_details_dtos: List[CompleteGoFDetailsDTO]
    ):
        gof_dtos = [
            complete_gof_details_dto.gof_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        gof_roles_dtos = [
            complete_gof_details_dto.gof_roles_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        gof_fields_dtos = [
            complete_gof_details_dto.gof_fields_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        self._validate_for_empty_mandatory_fields(
            gof_dtos=gof_dtos, gof_roles_dtos=gof_roles_dtos,
            gof_fields_dtos=gof_fields_dtos
        )
        self._validate_for_unique_field_ids(gof_fields_dtos=gof_fields_dtos)
        self._validate_read_permission_roles(gof_roles_dtos=gof_roles_dtos)
        self._validate_write_permission_roles(gof_roles_dtos=gof_roles_dtos)
        self.storage.create_gofs(gof_dtos=gof_dtos)
        self.storage.create_gof_roles(gof_roles_dtos=gof_roles_dtos)
        self.storage.create_gof_fields(gof_fields_dtos=gof_fields_dtos)

    def _validate_for_empty_mandatory_fields(
            self, gof_dtos: List[GoFDTO], gof_roles_dtos: List[GoFRolesDTO],
            gof_fields_dtos: List[GoFFieldsDTO]
    ):
        self._validate_for_empty_gof_ids(
            gof_dtos=gof_dtos, gof_roles_dtos=gof_roles_dtos,
            gof_fields_dtos=gof_fields_dtos
        )
        self._validate_for_empty_gof_display_names(gof_dtos=gof_dtos)
        self._validate_for_empty_read_permission_roles(
            gof_roles_dtos=gof_roles_dtos
        )
        self._validate_for_empty_write_permission_roles(
            gof_roles_dtos=gof_roles_dtos
        )
        self._validate_for_empty_field_ids(gof_fields_dtos=gof_fields_dtos)

    def _validate_for_empty_gof_ids(
            self, gof_dtos: List[GoFDTO], gof_roles_dtos: List[GoFRolesDTO],
            gof_fields_dtos: List[GoFFieldsDTO]
    ) -> Optional[GOFIdCantBeEmpty]:
        from ib_tasks.constants.exception_messages import empty_gof_id_message
        for gof_dto in gof_dtos:
            gof_id_is_empty = self._is_empty_field(field=gof_dto.gof_id)
            if gof_id_is_empty:
                raise GOFIdCantBeEmpty(empty_gof_id_message)
        for gof_roles_dto in gof_roles_dtos:
            gof_id_is_empty = self._is_empty_field(field=gof_roles_dto.gof_id)
            if gof_id_is_empty:
                raise GOFIdCantBeEmpty(empty_gof_id_message)
        for gof_fields_dto in gof_fields_dtos:
            gof_id_is_empty = self._is_empty_field(field=gof_fields_dto.gof_id)
            if gof_id_is_empty:
                raise GOFIdCantBeEmpty(empty_gof_id_message)
        return

    def _validate_for_empty_gof_display_names(
            self, gof_dtos: List[GoFDTO]
    ) -> Optional[GOFDisplayNameCantBeEmpty]:
        from ib_tasks.constants.exception_messages import \
            empty_gof_name_message
        for gof_dto in gof_dtos:
            invalid_display_name = self._is_empty_field(
                field=gof_dto.gof_display_name
            )
            if invalid_display_name:
                raise GOFDisplayNameCantBeEmpty(empty_gof_name_message)
        return

    def _validate_for_empty_read_permission_roles(
            self, gof_roles_dtos: List[GoFRolesDTO]
    ) -> Optional[GOFReadPermissionsCantBeEmpty]:
        from ib_tasks.constants.exception_messages import \
            empty_read_permissions_message
        for gof_roles_dto in gof_roles_dtos:
            read_permission_roles_are_emtpy = self._is_empty_field(
                field=gof_roles_dto.read_permission_roles
            )
            if read_permission_roles_are_emtpy:
                raise GOFReadPermissionsCantBeEmpty(
                    empty_read_permissions_message
                )
        return

    def _validate_for_empty_write_permission_roles(
            self, gof_roles_dtos: List[GoFRolesDTO]
    ) -> Optional[GOFWritePermissionsCantBeEmpty]:
        from ib_tasks.constants.exception_messages import \
            empty_write_permissions_message
        for gof_roles_dto in gof_roles_dtos:
            write_permission_roles_are_empty = self._is_empty_field(
                field=gof_roles_dto.write_permission_roles
            )
            if write_permission_roles_are_empty:
                raise GOFWritePermissionsCantBeEmpty(
                    empty_write_permissions_message
                )
        return

    def _validate_for_empty_field_ids(
            self, gof_fields_dtos: List[GoFFieldsDTO]
    ) -> Optional[GOFFieldIdsCantBeEmpty]:
        from ib_tasks.constants.exception_messages import \
            empty_field_ids_message
        for gof_fields_dto in gof_fields_dtos:
            field_ids_are_empty = self._is_empty_field(
                field=gof_fields_dto.field_ids
            )
            if field_ids_are_empty:
                raise GOFFieldIdsCantBeEmpty(empty_field_ids_message)
        return

    @staticmethod
    def _is_empty_field(field: Union[None, str, List]) -> bool:
        if isinstance(field, str):
            return not field or not field.strip()
        return not field

    def _validate_for_unique_field_ids(
            self, gof_fields_dtos: List[GoFFieldsDTO]
    ) -> Optional[DuplicatedFieldIds]:
        from ib_tasks.constants.exception_messages import \
            duplicated_field_ids_message
        for gof_fields_dto in gof_fields_dtos:
            field_ids_are_duplicated = self._are_field_ids_duplicated(
                field_ids=gof_fields_dto.field_ids
            )
            if field_ids_are_duplicated:
                raise DuplicatedFieldIds(duplicated_field_ids_message)
        return

    @staticmethod
    def _are_field_ids_duplicated(field_ids: List[str]) -> bool:
        return len(field_ids) != len(set(field_ids))

    def _validate_read_permission_roles(
            self, gof_roles_dtos: List[GoFRolesDTO]
    ) -> Optional[InvalidReadPermissionRoles]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        valid_read_permission_roles = \
            roles_service.get_all_valid_read_permission_roles()
        for gof_roles_dto in gof_roles_dtos:
            self._validate_read_permission_roles_of_a_gof(
                read_permission_roles=gof_roles_dto.read_permission_roles,
                valid_read_permission_roles=valid_read_permission_roles
            )
        return

    @staticmethod
    def _validate_read_permission_roles_of_a_gof(
            read_permission_roles: List[str],
            valid_read_permission_roles: List[str]
    ) -> Optional[InvalidReadPermissionRoles]:
        from ib_tasks.constants.exception_messages import \
            invalid_read_permission_roles_message
        invalid_read_permission_roles = \
            not set(read_permission_roles).issubset(
                set(valid_read_permission_roles)
            )
        if invalid_read_permission_roles:
            raise InvalidReadPermissionRoles(
                invalid_read_permission_roles_message
            )
        return

    def _validate_write_permission_roles(
            self, gof_roles_dtos: List[GoFRolesDTO]
    ) -> Optional[InvalidWritePermissionRoles]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        valid_write_permission_roles = \
            roles_service.get_all_valid_write_permission_roles()
        for gof_roles_dto in gof_roles_dtos:
            self._validate_write_permission_roles_of_a_gof(
                write_permission_roles=gof_roles_dto.write_permission_roles,
                valid_write_permission_roles=valid_write_permission_roles
            )
        return

    @staticmethod
    def _validate_write_permission_roles_of_a_gof(
            write_permission_roles: List[str],
            valid_write_permission_roles: List[str]
    ) -> Optional[InvalidWritePermissionRoles]:
        from ib_tasks.constants.exception_messages import \
            invalid_write_permission_roles_message
        invalid_write_permission_roles = \
            not set(write_permission_roles).issubset(
                set(valid_write_permission_roles)
            )
        if invalid_write_permission_roles:
            raise InvalidWritePermissionRoles(
                invalid_write_permission_roles_message
            )
        return
