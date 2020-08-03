from typing import List, Optional, Union

from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.fields_custom_exceptions import InvalidFieldIds
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidGoFsOfTaskTemplate
from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import CreateTaskDTO, UpdateTaskDTO, \
    GoFFieldsDTO, FieldValuesDTO


class CreateOrUpdateBaseValidationsInteractor:

    def __init__(
            self, task_storage: TaskStorageInterface,
            create_task_storage: CreateOrUpdateTaskStorageInterface,
            storage: StorageInterface
    ):
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
        self._validate_for_task_template_gofs(task_template_id, gof_ids)
        self._validate_gof_fields(task_dto)
        self._validate_same_gof_order(task_dto)
        self._validate_user_permission_on_given_fields_and_gofs(task_dto)

    def _validate_for_task_template_gofs(
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
        valid_gof_ids = self.task_storage.get_existing_gof_ids(gof_ids)
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
