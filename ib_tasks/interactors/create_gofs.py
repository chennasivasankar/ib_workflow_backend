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


class CreateGOF:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_gof_wrapper(self):
        pass

    def create_gofs(self, gof_dtos: List[GOFDTO]):

        # TODO: check if any mandatory fields are empty if so, raise exception
        self._validate_for_empty_mandatory_fields(gof_dtos=gof_dtos)

        # TODO: validate for unique field ids for a gof
        self._validate_for_unique_field_ids(gof_dtos=gof_dtos)

        # TODO: roles in read permission should be valid
        self._validate_read_permission_roles(gof_dtos=gof_dtos)

        # TODO: roles in write permission should be valid
        self._validate_write_permission_roles(gof_dtos=gof_dtos)

        # TODO: same gof ids should not have multiple display names
        self._validate_for_different_gof_display_names_with_same_gof_id(
            gof_dtos=gof_dtos
        )

        # TODO: store gofs in database
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

    def _validate_for_invalid_gof_display_names(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFDisplayNameCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_display_name = self._is_empty_field(
                field=gof_dto.gof_display_name
            )
            if invalid_display_name:
                raise GOFDisplayNameCantBeEmpty

    def _validate_for_empty_read_permission_roles(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFReadPermissionsCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_read_permission_roles = self._is_empty_field(
                field=gof_dto.read_permission_roles
            )
            if invalid_read_permission_roles:
                raise GOFReadPermissionsCantBeEmpty

    def _validate_for_empty_write_permission_roles(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFWritePermissionsCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_write_permission_roles = self._is_empty_field(
                field=gof_dto.write_permission_roles
            )
            if invalid_write_permission_roles:
                raise GOFWritePermissionsCantBeEmpty

    def _validate_for_empty_field_ids(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFFieldIdsCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_field_ids = self._is_empty_field(field=gof_dto.field_ids)
            if invalid_field_ids:
                raise GOFFieldIdsCantBeEmpty

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

    @staticmethod
    def _are_field_ids_duplicated(field_ids: List[str]) -> bool:
        return len(field_ids) != len(set(field_ids))

    def _validate_read_permission_roles(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[InvalidReadPermissionRoles]:
        valid_read_permission_roles = \
            self.storage.get_valid_read_permission_roles()
        for gof_dto in gof_dtos:
            self._validate_read_permission_roles_of_a_gof(
                read_permission_roles=gof_dto.read_permission_roles,
                valid_read_permission_roles=valid_read_permission_roles
            )

    @staticmethod
    def _validate_read_permission_roles_of_a_gof(
            read_permission_roles: List[str],
            valid_read_permission_roles: List[str]
    ) -> Optional[InvalidReadPermissionRoles]:
        read_permission_roles_is_string = isinstance(
            read_permission_roles, str
        )
        if read_permission_roles_is_string:
            invalid_read_permission_roles = \
                read_permission_roles not in valid_read_permission_roles
        read_permission_roles_is_list = isinstance(
            read_permission_roles, list
        )
        if read_permission_roles_is_list:
            invalid_read_permission_roles = \
                set(read_permission_roles) != set(valid_read_permission_roles)
        if invalid_read_permission_roles:
            raise InvalidReadPermissionRoles

    def _validate_write_permission_roles(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[InvalidWritePermissionRoles]:
        valid_write_permission_roles = \
            self.storage.get_valid_write_permission_roles()
        for gof_dto in gof_dtos:
            self._validate_write_permission_roles_of_a_gof(
                write_permission_roles=gof_dto.write_permission_roles,
                valid_write_permission_roles=valid_write_permission_roles
            )

    @staticmethod
    def _validate_write_permission_roles_of_a_gof(
            write_permission_roles: List[str],
            valid_write_permission_roles: List[str]
    ) -> Optional[InvalidWritePermissionRoles]:
        write_permission_roles_is_string = isinstance(
            write_permission_roles, str
        )
        if write_permission_roles_is_string:
            invalid_write_permission_roles = \
                write_permission_roles not in valid_write_permission_roles
        write_permission_roles_is_list = isinstance(
            write_permission_roles, list
        )
        if write_permission_roles_is_list:
            invalid_write_permission_roles = \
                set(write_permission_roles) != set(valid_write_permission_roles)
        if invalid_write_permission_roles:
            raise InvalidWritePermissionRoles

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
