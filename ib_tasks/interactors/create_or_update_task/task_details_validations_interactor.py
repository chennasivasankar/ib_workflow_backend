from dataclasses import dataclass
from typing import Optional, List, Union

from ib_tasks.constants.enum import ActionTypes
from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.custom_exceptions import InvalidProjectId
from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields
from ib_tasks.exceptions.task_custom_exceptions import (
    InvalidTaskTemplateOfProject
)
from ib_tasks.interactors.create_or_update_task \
    .gofs_details_validations_interactor import \
    GoFsDetailsValidationsInteractor
from ib_tasks.interactors.mixins.task_operations_utilities_mixin import \
    TaskOperationsUtilitiesMixin
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces \
    .create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import CreateTaskDTO, GoFFieldsDTO


@dataclass
class TaskDetailsValidationsStorages:
    task_template_storage: TaskTemplateStorageInterface
    storage: StorageInterface
    action_storage: ActionStorageInterface
    task_storage: TaskStorageInterface
    gof_storage: GoFStorageInterface
    create_task_storage: CreateOrUpdateTaskStorageInterface
    field_storage: FieldsStorageInterface


class TaskDetailsValidationsInteractor(TaskOperationsUtilitiesMixin):

    def __init__(self, storages_dto: TaskDetailsValidationsStorages):
        self.task_template_storage = storages_dto.task_template_storage
        self.storage = storages_dto.storage
        self.action_storage = storages_dto.action_storage
        self.task_storage = storages_dto.task_storage
        self.gof_storage = storages_dto.gof_storage
        self.create_task_storage = storages_dto.create_task_storage
        self.field_storage = storages_dto.field_storage

    def perform_task_details_validations(
            self, task_dto: CreateTaskDTO, stage_id: int):
        action_id = task_dto.basic_task_details_dto.action_id
        action_type = self._validate_action_id_and_get_action_type(action_id)
        task_template_id = task_dto.basic_task_details_dto.task_template_id

        self._validate_task_basic_details(task_dto, action_type)
        self._validate_gofs_details(task_dto, action_type, stage_id)
        action_type_is_not_no_validations = \
            action_type != ActionTypes.NO_VALIDATIONS.value
        if action_type_is_not_no_validations:
            self._validate_all_user_permitted_fields_are_filled_or_not(
                user_id=task_dto.basic_task_details_dto.created_by_id,
                project_id=task_dto.basic_task_details_dto.project_id,
                gof_fields_dtos=task_dto.gof_fields_dtos,
                stage_id=stage_id, task_template_id=task_template_id
            )

    def _validate_action_id_and_get_action_type(
            self, action_id: int
    ) -> Union[ActionTypes, InvalidActionException]:
        self._validate_action_id(action_id)
        action_type = \
            self.action_storage.get_action_type_for_given_action_id(action_id)
        return action_type

    def _validate_task_basic_details(
            self, task_dto: CreateTaskDTO, action_type: ActionTypes):
        project_id = task_dto.basic_task_details_dto.project_id
        task_template_id = task_dto.basic_task_details_dto.task_template_id

        self._validate_project_id(project_id)
        self._validate_task_template_project_id(project_id, task_template_id)
        self.validate_task_dates_and_priority(
            task_dto.basic_task_details_dto.start_datetime,
            task_dto.basic_task_details_dto.due_datetime,
            task_dto.basic_task_details_dto.priority, action_type)

    def _validate_gofs_details(
            self, task_dto: CreateTaskDTO, action_type: ActionTypes,
            stage_id: int
    ):
        gofs_details_validation_interactor = GoFsDetailsValidationsInteractor(
            self.task_storage, self.gof_storage,
            self.create_task_storage, self.storage,
            self.field_storage, self.task_template_storage)
        gofs_details_validation_interactor.perform_gofs_details_validations(
            gof_fields_dtos=task_dto.gof_fields_dtos,
            user_id=task_dto.basic_task_details_dto.created_by_id,
            task_template_id=task_dto.basic_task_details_dto.task_template_id,
            project_id=task_dto.basic_task_details_dto.project_id,
            action_type=action_type, stage_id=stage_id)

    @staticmethod
    def _validate_project_id(project_id: str) -> Optional[InvalidProjectId]:
        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        valid_project_ids = \
            service_adapter.auth_service.validate_project_ids([project_id])
        project_id_is_not_valid = project_id not in valid_project_ids
        if project_id_is_not_valid:
            raise InvalidProjectId(project_id)
        return

    def _validate_task_template_project_id(
            self, project_id: str, task_template_id: str
    ) -> Optional[InvalidTaskTemplateOfProject]:
        project_task_templates = \
            self.task_template_storage.get_project_templates(project_id)
        invalid_template_of_project = \
            task_template_id not in project_task_templates
        if invalid_template_of_project:
            raise InvalidTaskTemplateOfProject(project_id, task_template_id)
        return

    def _validate_action_id(
            self, action_id: int) -> Optional[InvalidActionException]:
        is_valid_action_id = self.storage.validate_action(action_id)
        action_id_is_invalid = not is_valid_action_id
        if action_id_is_invalid:
            raise InvalidActionException(action_id)
        return None

    def _validate_all_user_permitted_fields_are_filled_or_not(
            self, user_id: str, project_id: str,
            gof_fields_dtos: List[GoFFieldsDTO], stage_id: int,
            task_template_id: str
    ):
        user_roles = self._get_user_roles_of_project(user_id, project_id)
        permitted_gof_ids = self._get_user_writable_gof_ids_based_on_stage(
            stage_id, user_roles, task_template_id)
        self._validate_permitted_fields_filled_or_not(
            user_roles, permitted_gof_ids, gof_fields_dtos)

    @staticmethod
    def _get_user_roles_of_project(
            user_id: str, project_id: str) -> List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        user_roles = roles_service_adapter.roles_service \
            .get_user_role_ids_based_on_project(user_id, project_id)
        return user_roles

    def _get_user_writable_gof_ids_based_on_stage(
            self, stage_id: int, user_roles: List[str],
            task_template_id: str
    ) -> List[str]:
        stage_permitted_gof_ids = \
            self.task_template_storage.get_template_stage_permitted_gof_ids(
                task_template_id, stage_id)
        gof_id_with_display_name_dtos = \
            self.gof_storage.get_user_write_permitted_gof_ids_in_given_gof_ids(
                user_roles, stage_permitted_gof_ids)
        user_permitted_gof_ids = [
            dto.gof_id for dto in gof_id_with_display_name_dtos]
        return user_permitted_gof_ids

    def _validate_permitted_fields_filled_or_not(
            self, user_roles: List[str], permitted_gof_ids: List[str],
            gof_fields_dtos: List[GoFFieldsDTO]):
        field_id_with_display_name_dtos = \
            self.field_storage.get_user_writable_fields_for_given_gof_ids(
                user_roles, permitted_gof_ids)
        filled_field_ids = []
        for gof_fields_dto in gof_fields_dtos:
            filled_field_ids += [
                field_value_dto.field_id
                for field_value_dto in gof_fields_dto.field_values_dtos
            ]
        self._validate_all_user_permitted_field_ids_are_filled_or_not(
            field_id_with_display_name_dtos, filled_field_ids)

    @staticmethod
    def _validate_all_user_permitted_field_ids_are_filled_or_not(
            permitted_fields, filled_field_ids
    ) -> Optional[UserDidNotFillRequiredFields]:
        permitted_field_ids = [
            permitted_field.field_id for permitted_field in permitted_fields]
        unfilled_field_ids = list(sorted(
            set(permitted_field_ids) - set(filled_field_ids)))
        if unfilled_field_ids:
            unfilled_field_dtos = [
                permitted_field
                for permitted_field in permitted_fields
                if permitted_field.field_id in unfilled_field_ids
            ]
            raise UserDidNotFillRequiredFields(unfilled_field_dtos)
        return
