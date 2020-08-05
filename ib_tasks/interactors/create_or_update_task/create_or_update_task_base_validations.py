from typing import List, Optional, Union

from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.fields_custom_exceptions import InvalidFieldIds, \
    DuplicateFieldIdsToGoF
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsGoFWritablePermission, UserNeedsFieldWritablePermission
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidGoFsOfTaskTemplate, InvalidFieldsOfGoF
from ib_tasks.interactors.storage_interfaces. \
    create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import CreateTaskDTO, UpdateTaskDTO, \
    GoFFieldsDTO, FieldValuesDTO


class CreateOrUpdateTaskBaseValidationsInteractor:

    def __init__(
            self, task_storage: TaskStorageInterface,
            gof_storage: GoFStorageInterface,
            create_task_storage: CreateOrUpdateTaskStorageInterface,
            storage: StorageInterface, field_storage: FieldsStorageInterface
    ):
        self.gof_storage = gof_storage
        self.field_storage = field_storage
        self.task_storage = task_storage
        self.create_task_storage = create_task_storage
        self.storage = storage

    def perform_base_validations_for_create_or_update_task(
            self, task_dto: Union[CreateTaskDTO, UpdateTaskDTO],
            task_template_id: str
    ):
        is_valid_action_id = self.storage.validate_action(task_dto.action_id)
        if not is_valid_action_id:
            raise InvalidActionException(task_dto.action_id)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        field_values_dtos = self._get_field_values_dtos(
            task_dto.gof_fields_dtos
        )
        field_ids = [
            field_values_dto.field_id
            for field_values_dto in field_values_dtos
        ]
        self._validate_for_invalid_gof_ids(gof_ids)
        self._validate_for_invalid_field_ids(field_ids)
        self._validate_for_given_gofs_are_related_to_given_task_template(
            task_template_id, gof_ids)
        self._validate_for_given_fields_are_related_to_given_gofs(
            task_dto.gof_fields_dtos, gof_ids)
        self._validate_user_permission_on_given_fields_and_gofs(
            gof_ids, field_ids, task_dto.created_by_id
        )
        from ib_tasks.interactors.create_or_update_task. \
            validate_field_responses import ValidateFieldResponsesInteractor
        interactor = ValidateFieldResponsesInteractor(self.task_storage)
        field_values_dtos = \
            self._get_field_values_dtos(task_dto.gof_fields_dtos)
        interactor.validate_field_responses(field_values_dtos)

    def _validate_user_permission_on_given_fields_and_gofs(
            self, gof_ids: List[str], field_ids: List[str], user_id: str
    ) -> Union[None, UserNeedsGoFWritablePermission,
               UserNeedsFieldWritablePermission]:
        gof_write_permission_roles_dtos = \
            self.storage.get_write_permission_roles_for_given_gof_ids(gof_ids)
        field_write_permission_roles_dtos = \
            self.storage.get_write_permission_roles_for_given_field_ids(
                field_ids)
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        user_roles = roles_service_adapter.roles_service.get_user_role_ids(
            user_id)
        for gof_roles_dto in gof_write_permission_roles_dtos:
            required_roles = \
                gof_roles_dto.write_permission_roles
            missed_user_roles = list(set(required_roles) - set(user_roles))
            if missed_user_roles:
                raise UserNeedsGoFWritablePermission(
                    user_id, gof_roles_dto.gof_id,
                    missed_user_roles
                )
        for field_roles_dto in field_write_permission_roles_dtos:
            required_roles = \
                field_roles_dto.write_permission_roles
            missed_user_roles = list(set(required_roles) - set(user_roles))
            if missed_user_roles:
                raise UserNeedsFieldWritablePermission(
                    user_id, field_roles_dto.field_id,
                    missed_user_roles
                )
        return

    def _validate_for_given_fields_are_related_to_given_gofs(
            self, gof_fields_dtos: List[GoFFieldsDTO], gof_ids: List[str]
    ) -> Union[None, InvalidFieldsOfGoF, DuplicateFieldIdsToGoF]:
        from collections import defaultdict
        field_id_with_gof_id_dtos = \
            self.field_storage.get_field_ids_related_to_given_gof_ids(gof_ids)
        gof_fields_dict = defaultdict(list)
        for field_id_with_gof_id_dto in field_id_with_gof_id_dtos:
            gof_fields_dict[field_id_with_gof_id_dto.gof_id] \
                .append(field_id_with_gof_id_dto.field_id)
        for gof_fields_dto in gof_fields_dtos:
            given_gof_field_ids = [
                field_value_dto.field_id
                for field_value_dto in gof_fields_dto.field_values_dtos
            ]
            valid_gof_field_ids = gof_fields_dict[gof_fields_dto.gof_id]
            self._validate_for_invalid_fields_to_given_gof(
                gof_fields_dto.gof_id, given_gof_field_ids, valid_gof_field_ids
            )
        return

    def _validate_for_invalid_fields_to_given_gof(
            self, gof_id: str, given_gof_field_ids: List[str],
            valid_gof_field_ids: List[str]
    ) -> Union[None, InvalidFieldsOfGoF, DuplicateFieldIdsToGoF]:
        duplicate_field_ids = self._get_duplicates_in_given_list(
            given_gof_field_ids)
        if duplicate_field_ids:
            raise DuplicateFieldIdsToGoF(gof_id, duplicate_field_ids)
        invalid_gof_field_ids = list(
            set(given_gof_field_ids) - set(valid_gof_field_ids)
        )
        if invalid_gof_field_ids:
            raise InvalidFieldsOfGoF(gof_id, invalid_gof_field_ids)
        return

    def _validate_for_given_gofs_are_related_to_given_task_template(
            self, task_template_id: str, gof_ids: List[str]
    ) -> Optional[InvalidGoFsOfTaskTemplate]:
        valid_task_template_gof_ids = self.create_task_storage. \
            get_all_gof_ids_related_to_a_task_template(task_template_id)
        invalid_task_template_gof_ids = list(
            set(gof_ids) - set(valid_task_template_gof_ids))
        if invalid_task_template_gof_ids:
            raise InvalidGoFsOfTaskTemplate(
                invalid_task_template_gof_ids, task_template_id)
        return

    @staticmethod
    def _get_field_values_dtos(
            gof_fields_dtos: List[GoFFieldsDTO]
    ) -> List[FieldValuesDTO]:
        field_values_dtos = []
        for gof_fields_dto in gof_fields_dtos:
            field_values_dtos += [
                field_value_dto
                for field_value_dto in gof_fields_dto.field_values_dtos
            ]
        return field_values_dtos

    def _validate_for_invalid_gof_ids(
            self, gof_ids: List[str]
    ) -> Optional[InvalidGoFIds]:
        valid_gof_ids = self.gof_storage.get_existing_gof_ids(gof_ids)
        invalid_gof_ids = list(set(gof_ids) - set(valid_gof_ids))
        if invalid_gof_ids:
            raise InvalidGoFIds(gof_ids)
        return

    def _validate_for_invalid_field_ids(
            self, field_ids: List[str]
    ) -> Optional[InvalidFieldIds]:
        valid_field_ids = self.task_storage.get_existing_field_ids(field_ids)
        invalid_field_ids = list(set(field_ids) - set(valid_field_ids))
        if invalid_field_ids:
            raise InvalidFieldIds(invalid_field_ids)
        return

    @staticmethod
    def _get_duplicates_in_given_list(values: List) -> List:
        duplicate_values = list(
            set(
                [
                    value
                    for value in values if values.count(value) > 1
                ]
            )
        )
        return duplicate_values
