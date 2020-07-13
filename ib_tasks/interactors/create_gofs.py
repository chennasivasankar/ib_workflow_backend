from typing import List, Optional, Union

from ib_tasks.exceptions.custom_exceptions import GOFIdCantBeEmpty, GOFDisplayNameCantBeEmpty, \
    GOFReadPermissionsCantBeEmpty, GOFWritePermissionsCantBeEmpty, GOFFieldIdsCantBeEmpty, DuplicatedFieldIds
from ib_tasks.interactors.storage_interfaces.dtos import GOFDTO
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface

class CreateGOF:

    def __init__(self, storage: StorageInterface):
        self.storage=storage

    def create_gof_wraper(self):
        pass

    def create_gofs(self, gof_dtos: List[GOFDTO]):

        #TODO: check if any mandatory fields are empty if so, raise exception
        self._validate_for_empty_mandatory_fields(gof_dtos=gof_dtos)

        #TODO: validate for unique field ids for a gof
        self._validate_for_unique_field_ids(gof_dtos=gof_dtos)

        #TODO: roles in read permission should be valid

        #TODO: roles in write permission should be valid

        #TODO: same gof ids should not have multiple display names

        #TODO: store gofs in database
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
            invalid_gof_id = self._is_invalid_field(field=gof_dto.gof_id)
            if invalid_gof_id:
                raise GOFIdCantBeEmpty

    def _validate_for_invalid_gof_display_names(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFDisplayNameCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_display_name = self._is_invalid_field(
                field=gof_dto.gof_display_name
            )
            if invalid_display_name:
                raise GOFDisplayNameCantBeEmpty

    def _validate_for_empty_read_permission_roles(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFReadPermissionsCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_read_permission_roles = self._is_invalid_field(
                field=gof_dto.read_permission_roles
            )
            if invalid_read_permission_roles:
                raise GOFReadPermissionsCantBeEmpty

    def _validate_for_empty_write_permission_roles(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFWritePermissionsCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_write_permission_roles = self._is_invalid_field(
                field=gof_dto.write_permission_roles
            )
            if invalid_write_permission_roles:
                raise GOFWritePermissionsCantBeEmpty

    def _validate_for_empty_field_ids(
            self, gof_dtos: List[GOFDTO]
    ) -> Optional[GOFFieldIdsCantBeEmpty]:
        for gof_dto in gof_dtos:
            invalid_field_ids = self._is_invalid_field(field=gof_dto.field_ids)
            if invalid_field_ids:
                raise GOFFieldIdsCantBeEmpty

    @staticmethod
    def _is_invalid_field(field: Union[None, str, List]) -> bool:
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