from typing import List, Optional

from ib_tasks.constants.enum import ActionTypes
from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields
from ib_tasks.exceptions.task_custom_exceptions import StartDateIsRequired, \
    DueDateIsRequired, PriorityIsRequired
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.presenter_interfaces.validate_task_fields_presenter import \
    ValidateTaskFieldsPresenterInterface
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface import \
    CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.gof_storage_interface import \
    GoFStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface import \
    TaskTemplateStorageInterface


class TaskFieldsFilledValidationInteractor(GetTaskIdForTaskDisplayIdMixin):

    def __init__(
            self, create_task_storage: CreateOrUpdateTaskStorageInterface,
            field_storage: FieldsStorageInterface,
            task_storage: TaskStorageInterface,
            action_storage: ActionStorageInterface,
            task_template_storage: TaskTemplateStorageInterface,
            gof_storage: GoFStorageInterface):
        self.task_storage = task_storage
        self.action_storage = action_storage
        self.create_task_storage = create_task_storage
        self.task_template_storage = task_template_storage
        self.gof_storage = gof_storage
        self.field_storage = field_storage

    def validate_task_filled_fields_wrapper(
            self, task_display_id: str, action_id: int, user_id: str,
            presenter: ValidateTaskFieldsPresenterInterface):
        try:
            task_id = self.get_task_id_for_task_display_id(task_display_id)
            self.validate_task_filled_fields(task_id, action_id, user_id)
        except UserDidNotFillRequiredFields as err:
            return presenter.raise_user_did_not_fill_required_fields(err)
        except StartDateIsRequired:
            return presenter.start_date_is_required()
        except DueDateIsRequired:
            return presenter.due_date_is_required()
        except PriorityIsRequired:
            return presenter.priority_is_required()

    def validate_task_filled_fields(
            self, task_id: int, action_id: int, user_id: str):
        action_type = self.action_storage.get_action_type_for_given_action_id(
            action_id)
        action_type_is_no_validations = \
            action_type == ActionTypes.NO_VALIDATIONS.value
        if action_type_is_no_validations:
            return
        project_id = \
            self.task_storage.get_project_id_for_the_task_id(task_id=task_id)
        self._validation_all_user_template_permitted_fields_are_filled_or_not(
            task_id=task_id, project_id=project_id, action_id=action_id,
            user_id=user_id)
        self._validate_task_base_details(task_id)

    def _validation_all_user_template_permitted_fields_are_filled_or_not(
            self, task_id: int, project_id: str, action_id: int,
            user_id: str):
        action_type = self.action_storage.get_action_type_for_given_action_id(
            action_id)
        action_type_is_not_no_validations = \
            action_type != ActionTypes.NO_VALIDATIONS.value
        if action_type_is_not_no_validations:
            stage_id = self.action_storage.get_stage_id_for_given_action_id(
                action_id)
            self._validate_all_user_template_permitted_fields_are_filled_or_not(
                user_id, task_id, project_id, stage_id)

    def _validate_all_user_template_permitted_fields_are_filled_or_not(
            self, user_id: str, task_id: int, project_id: str,
            stage_id: int
    ):
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        user_roles = roles_service_adapter.roles_service \
            .get_user_role_ids_based_on_project(user_id=user_id,
                                                project_id=project_id)
        task_template_id = \
            self.create_task_storage.get_template_id_for_given_task(task_id)
        template_gof_ids = \
            self.task_template_storage.get_template_stage_permitted_gof_ids(
                stage_id=stage_id, task_template_id=task_template_id)
        gof_id_with_display_name_dtos = \
            self.gof_storage.get_user_write_permitted_gof_ids_in_given_gof_ids(
                user_roles, template_gof_ids)
        user_permitted_gof_ids = [
            dto.gof_id for dto in gof_id_with_display_name_dtos]
        field_id_with_display_name_dtos = \
            self.field_storage.get_user_writable_fields_for_given_gof_ids(
                user_roles, user_permitted_gof_ids)
        filled_gofs_with_task_gof_ids = \
            self.gof_storage.get_filled_task_gofs_with_gof_id(task_id)
        task_gof_ids = [
            dto.task_gof_id for dto in filled_gofs_with_task_gof_ids]
        filled_field_ids = \
            self.gof_storage.get_filled_field_ids_of_given_task_gof_ids(
                task_gof_ids)
        self._validate_all_user_permitted_field_ids_are_filled_or_not(
            field_id_with_display_name_dtos, filled_field_ids)

    @staticmethod
    def _validate_all_user_permitted_field_ids_are_filled_or_not(
            permitted_fields: List[FieldWithGoFDisplayNameDTO],
            filled_field_ids: List[str]
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

    def _validate_task_base_details(self, task_id: int):
        task_dto = self.task_storage.get_task_base_details_dto(task_id)
        is_start_date_empty = not task_dto.start_date
        if is_start_date_empty:
            raise StartDateIsRequired()
        is_due_date_empty = not task_dto.due_date
        if is_due_date_empty:
            raise DueDateIsRequired()
        is_priority_empty = not task_dto.priority
        if is_priority_empty:
            raise PriorityIsRequired()
