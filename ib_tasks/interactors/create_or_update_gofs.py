from collections import defaultdict
from typing import List, Optional, Union

from ib_tasks.exceptions.custom_exceptions import (
    GOFIdCantBeEmpty, GOFDisplayNameCantBeEmpty, GOFReadPermissionsCantBeEmpty,
    GOFWritePermissionsCantBeEmpty, InvalidReadPermissionRoles,
    InvalidWritePermissionRoles, InvalidTaskTemplateIds,
    InvalidOrderValues, TaskTemplateIdCantBeEmpty, ConflictingGoFOrder
)
from ib_tasks.interactors.storage_interfaces.dtos import (
    CompleteGoFDetailsDTO, GoFRolesDTO, GoFDTO, GoFRoleDTO, GoFRoleWithIdDTO
)
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
        self._validate_for_invalid_order_value(gof_dtos=gof_dtos)
        self._validate_read_permission_roles(gof_roles_dtos=gof_roles_dtos)
        self._validate_write_permission_roles(gof_roles_dtos=gof_roles_dtos)
        self._validate_for_invalid_task_template_id(gof_dtos=gof_dtos)

        complete_gof_details_dtos_for_updation, \
        complete_gof_details_dtos_for_creation = self._filter_gof_details_dtos(
            gof_dtos, complete_gof_details_dtos
        )
        if complete_gof_details_dtos_for_updation:
            self._update_gofs(complete_gof_details_dtos_for_updation)

        if complete_gof_details_dtos_for_creation:
            self._create_gofs(complete_gof_details_dtos_for_creation)
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
        complete_gof_details_dtos_for_updation = []
        if existing_gof_ids_in_given_gof_ids:
            complete_gof_details_dtos_for_updation = \
                self._get_complete_gof_details_dtos_of_given_gof_ids(
                    gof_ids=existing_gof_ids_in_given_gof_ids,
                    complete_gof_details_dtos=complete_gof_details_dtos
                )
        new_gof_ids_in_given_gof_ids = list(
            set(gof_ids) - set(existing_gof_ids_in_given_gof_ids)
        )
        complete_gof_details_dtos_for_creation = \
            self._get_complete_gof_details_dtos_of_given_gof_ids(
                gof_ids=new_gof_ids_in_given_gof_ids,
                complete_gof_details_dtos=complete_gof_details_dtos
            )
        return complete_gof_details_dtos_for_updation, \
               complete_gof_details_dtos_for_creation

    def _update_gofs(
            self, complete_gof_details_dtos: List[CompleteGoFDetailsDTO]
    ):
        gof_dtos = \
            self._get_gof_dtos_for_given_complete_gof_details_dtos(
                complete_gof_details_dtos=complete_gof_details_dtos
            )
        self._validate_for_order_value_in_updating_gofs(gof_dtos)
        gof_roles_dtos = \
            self._get_gof_roles_dtos_for_given_complete_gof_details_dtos(
                complete_gof_details_dtos=complete_gof_details_dtos
            )
        gof_role_dtos = self._get_role_dtos(gof_roles_dtos=gof_roles_dtos)
        existing_roles, new_roles = self._filter_gof_role_dtos(
            gof_role_dtos=gof_role_dtos
        )
        self.storage.update_gofs(gof_dtos=gof_dtos)
        if existing_roles:
            self.storage.update_gof_roles(gof_role_with_id_dtos=existing_roles)
        if new_roles:
            self.storage.create_gof_roles(gof_role_dtos=new_roles)

    def _validate_for_order_value_in_updating_gofs(
            self, gof_dtos: List[GoFDTO]
    ) -> Optional[ConflictingGoFOrder]:
        gof_ids = [gof_dto.gof_id for gof_dto in gof_dtos]
        existing_gof_dtos = \
            self.storage.get_gof_dtos_for_given_gof_ids(gof_ids)
        template_gofs = defaultdict(list)
        for gof_dto in existing_gof_dtos:
            template_gofs[gof_dto.task_template_id].append(gof_dto)
        invalid_order_gof_ids = []
        for gof_dto in gof_dtos:
            for template_gof in template_gofs[gof_dto.task_template_id]:
                conflicting_order_value = (
                        template_gof.gof_id != gof_dto.gof_id and
                        template_gof.order == gof_dto.order
                )
                if conflicting_order_value:
                    invalid_order_gof_ids.append(gof_dto.gof_id)
                    break
        if invalid_order_gof_ids:
            raise ConflictingGoFOrder(invalid_order_gof_ids)
        return

    def _create_gofs(
            self, complete_gof_details_dtos: List[CompleteGoFDetailsDTO]
    ):
        gof_dtos = \
            self._get_gof_dtos_for_given_complete_gof_details_dtos(
                complete_gof_details_dtos=complete_gof_details_dtos
            )
        gof_roles_dtos = \
            self._get_gof_roles_dtos_for_given_complete_gof_details_dtos(
                complete_gof_details_dtos=complete_gof_details_dtos
            )
        gof_role_dtos = self._get_role_dtos(gof_roles_dtos=gof_roles_dtos)
        self.storage.create_gofs(gof_dtos=gof_dtos)
        self.storage.create_gof_roles(gof_role_dtos=gof_role_dtos)

    def _filter_gof_role_dtos(
            self, gof_role_dtos: List[GoFRoleDTO]
    ) -> (List[GoFRoleWithIdDTO], List[GoFRoleDTO]):
        gof_ids = [gof_role_dto.gof_id for gof_role_dto in gof_role_dtos]
        existing_gof_roles = self.storage.get_roles_for_given_gof_ids(
            gof_ids=gof_ids
        )
        for existing_gof_role in existing_gof_roles:
            for gof_role_dto in gof_role_dtos:
                role_is_matched = (
                        existing_gof_role.gof_id == gof_role_dto.gof_id and
                        existing_gof_role.role == gof_role_dto.role
                )
                if role_is_matched:
                    existing_gof_role.permission_type = \
                        gof_role_dto.permission_type
                    gof_role_dtos.remove(gof_role_dto)
                    break
        return existing_gof_roles, gof_role_dtos

    def _validate_for_invalid_order_value(
            self, gof_dtos: List[GoFDTO]
    ) -> Optional[InvalidOrderValues]:
        invalid_order_values = [
            gof_dto.order
            for gof_dto in gof_dtos
            if self._invalid_order_value(order=gof_dto.order)
        ]
        if invalid_order_values:
            raise InvalidOrderValues(invalid_order_values=invalid_order_values)
        return

    @staticmethod
    def _invalid_order_value(order: int) -> bool:
        return order < -1

    def _validate_for_invalid_task_template_id(
            self, gof_dtos: List[GoFDTO]
    ) -> Optional[InvalidTaskTemplateIds]:
        template_ids = [gof_dto.task_template_id for gof_dto in gof_dtos]
        valid_template_ids = \
            self.storage.get_valid_template_ids_in_given_template_ids(
                template_ids=template_ids
            )
        invalid_template_ids = list(
            set(template_ids) - set(valid_template_ids))
        if invalid_template_ids:
            raise InvalidTaskTemplateIds(
                invalid_task_template_ids=invalid_template_ids
            )
        return

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
                    permission_type=PermissionTypes.READ
                )
                for read_permission_role in gof_roles_dto.read_permission_roles
            ]
        for gof_roles_dto in gof_roles_dtos:
            gof_role_dtos += [
                GoFRoleDTO(
                    gof_id=gof_roles_dto.gof_id,
                    role=write_permission_role,
                    permission_type=PermissionTypes.WRITE
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
        self._validate_for_empty_task_template_ids(gof_dtos=gof_dtos)
        self._validate_for_empty_read_permission_roles(
            gof_roles_dtos=gof_roles_dtos
        )
        self._validate_for_empty_write_permission_roles(
            gof_roles_dtos=gof_roles_dtos
        )

    def _validate_for_empty_task_template_ids(
            self, gof_dtos: List[GoFDTO]
    ) -> Optional[TaskTemplateIdCantBeEmpty]:
        from ib_tasks.constants.exception_messages import \
            empty_task_template_id_message
        for gof_dto in gof_dtos:
            task_template_id_is_empty = self._is_empty_field(
                gof_dto.task_template_id
            )
            if task_template_id_is_empty:
                raise TaskTemplateIdCantBeEmpty(empty_task_template_id_message)
        return

    def _validate_for_empty_gof_ids(
            self, gof_dtos: List[GoFDTO], gof_roles_dtos: List[GoFRolesDTO]
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

    @staticmethod
    def _is_empty_field(field: Union[None, str, List]) -> bool:
        if isinstance(field, str):
            return not field or not field.strip()
        return not field

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
