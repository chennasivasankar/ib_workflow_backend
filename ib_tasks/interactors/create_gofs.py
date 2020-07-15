from collections import defaultdict
from typing import List, Optional, Union

from ib_tasks.exceptions.custom_exceptions import (
    GOFIdCantBeEmpty, GOFDisplayNameCantBeEmpty, GOFReadPermissionsCantBeEmpty,
    GOFWritePermissionsCantBeEmpty, GOFFieldIdsCantBeEmpty, DuplicatedFieldIds,
    InvalidReadPermissionRoles, InvalidWritePermissionRoles,
    DifferentDisplayNamesForSameGOF
)
from ib_tasks.interactors.storage_interfaces.dtos import GOFDTO
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface


class CreateGoFsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_gof_wrapper(self):
        pass

    def create_gofs(self, gof_dtos: List[GOFDTO]):

        self._validate_for_empty_mandatory_fields(gof_dtos=gof_dtos)
        self._validate_for_unique_field_ids(gof_dtos=gof_dtos)
        self._validate_read_permission_roles(gof_dtos=gof_dtos)
        self._validate_write_permission_roles(gof_dtos=gof_dtos)
        self._validate_for_different_gof_display_names_with_same_gof_id(
            gof_dtos=gof_dtos
        )
        self.storage.create_gofs(gof_dtos=gof_dtos)

    def _validate_for_empty_mandatory_fields(self, gof_dtos: List[GOFDTO]):
        self._validate_for_invalid_gof_ids(gof_dtos=gof_dtos)
        self._validate_for_invalid_gof_display_names(gof_dtos=gof_dtos)
        self._validate_for_empty_read_permission_roles(gof_dtos=gof_dtos)
        self._validate_for_empty_write_permission_roles(gof_dtos=gof_dtos)
        self._validate_for_empty_field_ids(gof_dtos=gof_dtos)

    def _validate_for_invalid_gof_ids(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFIdCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_gof_id = self._is_empty_field(field=gof_dto.gof_id)
            if invalid_gof_id:
                raise GOFIdCantBeEmpty
            return

    def _validate_for_invalid_gof_display_names(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFDisplayNameCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_display_name = self._is_empty_field(
                field=gof_dto.gof_display_name
            )
            if invalid_display_name:
                raise GOFDisplayNameCantBeEmpty
            return

    def _validate_for_empty_read_permission_roles(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFReadPermissionsCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_read_permission_roles = self._is_empty_field(
                field=gof_dto.read_permission_roles
            )
            if invalid_read_permission_roles:
                raise GOFReadPermissionsCantBeEmpty
            return

    def _validate_for_empty_write_permission_roles(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFWritePermissionsCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_write_permission_roles = self._is_empty_field(
                field=gof_dto.write_permission_roles
            )
            if invalid_write_permission_roles:
                raise GOFWritePermissionsCantBeEmpty
            return

    def _validate_for_empty_field_ids(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFFieldIdsCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_field_ids = self._is_empty_field(field=gof_dto.field_ids)
            if invalid_field_ids:
                raise GOFFieldIdsCantBeEmpty
            return

    @staticmethod
    def _is_empty_field(field: Union[None, str, List]) -> bool:
        return field is None or not field

    def _validate_for_unique_field_ids(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[DuplicatedFieldIds]:
        for gof_dto in gof_dtos:
            field_ids_are_duplicated = self._are_field_ids_duplicated(
                field_ids=gof_dto.field_ids
            )
            if field_ids_are_duplicated:
                raise DuplicatedFieldIds
            return

    @staticmethod
    def _are_field_ids_duplicated(field_ids: List[str]) -> bool:
        return len(field_ids) != len(set(field_ids))

    def _validate_read_permission_roles(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[InvalidReadPermissionRoles]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        valid_read_permission_roles = \
            roles_service_adapter.roles_service.get_all_valid_read_permission_roles()
        for gof_dto in gof_dtos:
            self._validate_read_permission_roles_of_a_gof(
                read_permission_roles=gof_dto.read_permission_roles,
                valid_read_permission_roles=valid_read_permission_roles
            )
        return

    @staticmethod
    def _validate_read_permission_roles_of_a_gof(
            read_permission_roles: List[str],
            valid_read_permission_roles: List[str]
    ) -> Optional[InvalidReadPermissionRoles]:
        invalid_read_permission_roles = \
                not set(read_permission_roles).issubset(set(valid_read_permission_roles))
        if invalid_read_permission_roles:
            raise InvalidReadPermissionRoles
        return

    def _validate_write_permission_roles(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[InvalidWritePermissionRoles]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        valid_write_permission_roles = \
            roles_service_adapter.roles_service.get_all_valid_write_permission_roles()
        for gof_dto in gof_dtos:
            self._validate_write_permission_roles_of_a_gof(
                write_permission_roles=gof_dto.write_permission_roles,
                valid_write_permission_roles=valid_write_permission_roles
            )
        return

    @staticmethod
    def _validate_write_permission_roles_of_a_gof(
            write_permission_roles: List[str],
            valid_write_permission_roles: List[str]
    ) -> Optional[InvalidWritePermissionRoles]:
        invalid_write_permission_roles = \
                not set(write_permission_roles).issubset(set(valid_write_permission_roles))
        if invalid_write_permission_roles:
            raise InvalidWritePermissionRoles
        return

    @staticmethod
    def _validate_for_different_gof_display_names_with_same_gof_id(
            gof_dtos: List[GOFDTO]
    ) -> Optional[DifferentDisplayNamesForSameGOF]:
        gof_display_names = defaultdict(str)
        for gof_dto in gof_dtos:
            new_gof_id = not gof_display_names[gof_dto.gof_id]
            if new_gof_id:
                gof_display_names[gof_dto.gof_id] = gof_dto.gof_display_name
            else:
                different_display_name_for_same_gof_id = \
                    gof_display_names[gof_dto.gof_id] != gof_dto.gof_display_name
                if different_display_name_for_same_gof_id:
                    raise DifferentDisplayNamesForSameGOF
        return
