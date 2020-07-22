from typing import List, Optional, Union

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.exceptions.columns_custom_exceptions import MaxColumnsMustBeAPositiveInteger
from ib_tasks.exceptions.roles_custom_exceptions import InvalidReadPermissionRoles, InvalidWritePermissionRoles
from ib_tasks.exceptions.gofs_custom_exceptions import GOFIdCantBeEmpty, GOFDisplayNameCantBeEmpty, \
    GOFReadPermissionsCantBeEmpty, GOFWritePermissionsCantBeEmpty
from ib_tasks.interactors.storage_interfaces.gof_dtos import GoFDTO, GoFRolesDTO, GoFRoleDTO, CompleteGoFDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface


class CreateOrUpdateGoFsInteractor:

    def __init__(self, storage: TaskStorageInterface):
        self.storage = storage

    def create_or_update_gofs_wrapper(self):
        pass

    def create_or_update_gofs(
            self, complete_gof_details_dtos: List[CompleteGoFDetailsDTO]
    ):
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        gof_dtos = self._get_gof_dtos_for_given_complete_gof_details_dtos(
            complete_gof_details_dtos=complete_gof_details_dtos
        )
        gof_roles_dtos = \
            self._get_gof_roles_dtos_for_given_complete_gof_details_dtos(
                complete_gof_details_dtos=complete_gof_details_dtos
            )
        self._validate_for_empty_mandatory_fields(
            gof_dtos=gof_dtos, gof_roles_dtos=gof_roles_dtos
        )
        gof_role_dtos = self._get_role_dtos(gof_roles_dtos)
        role_ids = [gof_role_dto.role for gof_role_dto in gof_role_dtos]

        service_adapter = get_roles_service_adapter()
        roles_service = service_adapter.roles_service
        valid_roles = roles_service.get_valid_role_ids_in_given_role_ids(
            role_ids=role_ids
        )
        self._validate_read_permission_roles(
            gof_roles_dtos=gof_roles_dtos, valid_roles=valid_roles
        )
        self._validate_write_permission_roles(
            gof_roles_dtos=gof_roles_dtos, valid_roles=valid_roles
        )

        gofs_for_updation, gofs_for_creation = self._filter_gof_details_dtos(
            gof_dtos, complete_gof_details_dtos
        )
        gof_roles_dtos = \
            self._get_gof_roles_dtos_for_given_complete_gof_details_dtos(
                complete_gof_details_dtos=complete_gof_details_dtos
            )
        gof_role_dtos = self._get_role_dtos(gof_roles_dtos=gof_roles_dtos)
        if gofs_for_updation:
            self._update_gofs(gofs_for_updation)

        if gofs_for_creation:
            self._create_gofs(gofs_for_creation)

        self.storage.create_gof_roles(gof_role_dtos)
        return

    def _filter_gof_details_dtos(
            self, gof_dtos: List[GoFDTO],
            complete_gof_details_dtos: List[CompleteGoFDetailsDTO]
    ) -> (List[CompleteGoFDetailsDTO], List[CompleteGoFDetailsDTO]):
        gof_ids = [
            gof_dto.gof_id for gof_dto in gof_dtos
        ]
        existing_gof_ids_in_given_gof_ids = \
            self.storage.get_existing_gof_ids_in_given_gof_ids(gof_ids=gof_ids)
        gofs_for_updation = []
        if existing_gof_ids_in_given_gof_ids:
            gofs_for_updation = \
                self._get_complete_gof_details_dtos_of_given_gof_ids(
                    gof_ids=existing_gof_ids_in_given_gof_ids,
                    complete_gof_details_dtos=complete_gof_details_dtos
                )
        new_gof_ids_in_given_gof_ids = list(
            set(gof_ids) - set(existing_gof_ids_in_given_gof_ids)
        )
        gofs_for_creation = \
            self._get_complete_gof_details_dtos_of_given_gof_ids(
                gof_ids=new_gof_ids_in_given_gof_ids,
                complete_gof_details_dtos=complete_gof_details_dtos
            )
        return gofs_for_updation, gofs_for_creation

    def _update_gofs(
            self, complete_gof_details_dtos: List[CompleteGoFDetailsDTO]
    ):
        gof_dtos = \
            self._get_gof_dtos_for_given_complete_gof_details_dtos(
                complete_gof_details_dtos=complete_gof_details_dtos
            )
        self.storage.update_gofs(gof_dtos=gof_dtos)
        gof_ids = [gof_dto.gof_id for gof_dto in gof_dtos]
        self.storage.delete_gof_roles(gof_ids=gof_ids)

    def _create_gofs(
            self, complete_gof_details_dtos: List[CompleteGoFDetailsDTO]
    ):
        gof_dtos = \
            self._get_gof_dtos_for_given_complete_gof_details_dtos(
                complete_gof_details_dtos=complete_gof_details_dtos
            )
        self.storage.create_gofs(gof_dtos=gof_dtos)

    @staticmethod
    def _get_gof_dtos_for_given_complete_gof_details_dtos(
            complete_gof_details_dtos: List[CompleteGoFDetailsDTO]
    ):
        gof_dtos = [
            complete_gof_details_dto.gof_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        return gof_dtos

    @staticmethod
    def _get_gof_roles_dtos_for_given_complete_gof_details_dtos(
            complete_gof_details_dtos: List[CompleteGoFDetailsDTO]
    ):
        gof_roles_dtos = [
            complete_gof_details_dto.gof_roles_dto
            for complete_gof_details_dto in complete_gof_details_dtos
        ]
        return gof_roles_dtos

    def _get_complete_gof_details_dtos_of_given_gof_ids(
            self, gof_ids: List[str],
            complete_gof_details_dtos: List[CompleteGoFDetailsDTO]
    ) -> List[CompleteGoFDetailsDTO]:
        gof_details_dtos = [
            self._get_complete_gof_details_dto_for_a_gof_id(
                gof_id=gof_id,
                complete_gof_details_dtos=complete_gof_details_dtos
            )
            for gof_id in gof_ids
        ]
        return gof_details_dtos

    @staticmethod
    def _get_complete_gof_details_dto_for_a_gof_id(
            gof_id: str, complete_gof_details_dtos: List[CompleteGoFDetailsDTO]
    ) -> Optional[CompleteGoFDetailsDTO]:
        for complete_gof_details_dto in complete_gof_details_dtos:
            gof_id_is_matched = \
                complete_gof_details_dto.gof_dto.gof_id == gof_id
            if gof_id_is_matched:
                return complete_gof_details_dto
        return

    @staticmethod
    def _get_role_dtos(gof_roles_dtos: List[GoFRolesDTO]) -> List[GoFRoleDTO]:
        from ib_tasks.constants.enum import PermissionTypes
        gof_role_dtos = []
        for gof_roles_dto in gof_roles_dtos:
            gof_role_dtos += [
                GoFRoleDTO(
                    gof_id=gof_roles_dto.gof_id,
                    role=read_permission_role,
                    permission_type=PermissionTypes.READ.value
                )
                for read_permission_role in gof_roles_dto.read_permission_roles
            ]
        for gof_roles_dto in gof_roles_dtos:
            gof_role_dtos += [
                GoFRoleDTO(
                    gof_id=gof_roles_dto.gof_id,
                    role=write_permission_role,
                    permission_type=PermissionTypes.WRITE.value
                )
                for write_permission_role in (
                    gof_roles_dto.write_permission_roles
                )
            ]
        return gof_role_dtos

    def _validate_for_empty_mandatory_fields(
            self, gof_dtos: List[GoFDTO], gof_roles_dtos: List[GoFRolesDTO]
    ):
        self._validate_for_empty_gof_ids(
            gof_dtos=gof_dtos, gof_roles_dtos=gof_roles_dtos
        )
        self._validate_for_empty_gof_display_names(gof_dtos=gof_dtos)
        self._validate_for_invalid_max_columns(gof_dtos=gof_dtos)
        self._validate_for_empty_read_permission_roles(
            gof_roles_dtos=gof_roles_dtos
        )
        self._validate_for_empty_write_permission_roles(
            gof_roles_dtos=gof_roles_dtos
        )

    def _validate_for_invalid_max_columns(
            self, gof_dtos: List[GoFDTO]
    ) -> Optional[MaxColumnsMustBeAPositiveInteger]:
        for gof_dto in gof_dtos:
            self._validate_max_column_value(gof_dto.max_columns)
        return

    @staticmethod
    def _validate_max_column_value(
            max_columns: int
    ) -> Union[None, MaxColumnsMustBeAPositiveInteger]:
        from ib_tasks.constants.exception_messages import (
            MAX_COLUMNS_VALUE_MUST_BE_POSITIVE_INTEGER_MESSAGE
        )
        max_columns_is_not_a_positive_integer = max_columns < 1
        if max_columns_is_not_a_positive_integer:
            error_message = "{}: {}".format(
                MAX_COLUMNS_VALUE_MUST_BE_POSITIVE_INTEGER_MESSAGE, max_columns
            )
            raise MaxColumnsMustBeAPositiveInteger(error_message)
        return

    def _validate_for_empty_gof_ids(
            self, gof_dtos: List[GoFDTO], gof_roles_dtos: List[GoFRolesDTO]
    ) -> Optional[GOFIdCantBeEmpty]:
        from ib_tasks.constants.exception_messages import EMPTY_GOF_ID_MESSAGE
        for gof_dto in gof_dtos:
            gof_id_is_empty = self._is_empty_field(field=gof_dto.gof_id)
            if gof_id_is_empty:
                raise GOFIdCantBeEmpty(EMPTY_GOF_ID_MESSAGE)
        for gof_roles_dto in gof_roles_dtos:
            gof_id_is_empty = self._is_empty_field(field=gof_roles_dto.gof_id)
            if gof_id_is_empty:
                raise GOFIdCantBeEmpty(EMPTY_GOF_ID_MESSAGE)
        return

    def _validate_for_empty_gof_display_names(
            self, gof_dtos: List[GoFDTO]
    ) -> Optional[GOFDisplayNameCantBeEmpty]:
        from ib_tasks.constants.exception_messages import \
            EMPTY_GOF_NAME_MESSAGE
        for gof_dto in gof_dtos:
            invalid_display_name = self._is_empty_field(
                field=gof_dto.gof_display_name
            )
            if invalid_display_name:
                raise GOFDisplayNameCantBeEmpty(EMPTY_GOF_NAME_MESSAGE)
        return

    def _validate_for_empty_read_permission_roles(
            self, gof_roles_dtos: List[GoFRolesDTO]
    ) -> Optional[GOFReadPermissionsCantBeEmpty]:
        from ib_tasks.constants.exception_messages import \
            EMPTY_GOF_READ_PERMISSIONS_MESSAGE
        for gof_roles_dto in gof_roles_dtos:
            read_permission_roles_are_emtpy = self._is_empty_field(
                field=gof_roles_dto.read_permission_roles
            )
            if read_permission_roles_are_emtpy:
                raise GOFReadPermissionsCantBeEmpty(
                    EMPTY_GOF_READ_PERMISSIONS_MESSAGE
                )
        return

    def _validate_for_empty_write_permission_roles(
            self, gof_roles_dtos: List[GoFRolesDTO]
    ) -> Optional[GOFWritePermissionsCantBeEmpty]:
        from ib_tasks.constants.exception_messages import \
            EMPTY_WRITE_PERMISSIONS_MESSAGE
        for gof_roles_dto in gof_roles_dtos:
            write_permission_roles_are_empty = self._is_empty_field(
                field=gof_roles_dto.write_permission_roles
            )
            if write_permission_roles_are_empty:
                raise GOFWritePermissionsCantBeEmpty(
                    EMPTY_WRITE_PERMISSIONS_MESSAGE
                )
        return

    @staticmethod
    def _is_empty_field(field: Union[None, str, List]) -> bool:
        if isinstance(field, str):
            return not field or not field.strip()
        return not field

    def _validate_read_permission_roles(
            self, gof_roles_dtos: List[GoFRolesDTO], valid_roles: List[str]
    ) -> Optional[InvalidReadPermissionRoles]:
        for gof_roles_dto in gof_roles_dtos:
            self._validate_read_permission_roles_of_a_gof(
                read_permission_roles=gof_roles_dto.read_permission_roles,
                valid_roles=valid_roles
            )
        return

    @staticmethod
    def _validate_read_permission_roles_of_a_gof(
            read_permission_roles: List[str],
            valid_roles: List[str]
    ) -> Optional[InvalidReadPermissionRoles]:
        invalid_read_permission_roles = \
            not set(read_permission_roles).issubset(set(valid_roles))
        if invalid_read_permission_roles:
            invalid_roles = list(
                set(read_permission_roles) - set(valid_roles)
            )
            from ib_tasks.constants.exception_messages import \
                INVALID_READ_PERMISSION_ROLES
            INVALID_READ_PERMISSION_ROLES += str(invalid_roles)
            raise InvalidReadPermissionRoles(INVALID_READ_PERMISSION_ROLES)
        return

    def _validate_write_permission_roles(
            self, gof_roles_dtos: List[GoFRolesDTO], valid_roles: List[str]
    ) -> Optional[InvalidWritePermissionRoles]:
        for gof_roles_dto in gof_roles_dtos:
            self._validate_write_permission_roles_of_a_gof(
                write_permission_roles=gof_roles_dto.write_permission_roles,
                valid_roles=valid_roles
            )
        return

    @staticmethod
    def _validate_write_permission_roles_of_a_gof(
            write_permission_roles: List[str],
            valid_roles: List[str]
    ) -> Optional[InvalidWritePermissionRoles]:
        invalid_write_permission_roles = \
            not set(write_permission_roles).issubset(set(valid_roles))
        if invalid_write_permission_roles:
            invalid_roles = list(
                set(write_permission_roles) - set(valid_roles)
            )
            from ib_tasks.constants.exception_messages import \
                INVALID_WRITE_PERMISSION_ROLES
            INVALID_WRITE_PERMISSION_ROLES += str(invalid_roles)
            raise InvalidWritePermissionRoles(INVALID_WRITE_PERMISSION_ROLES)
        return
