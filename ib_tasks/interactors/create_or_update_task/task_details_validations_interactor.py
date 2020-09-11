from typing import Optional, List

from ib_tasks.constants.enum import ActionTypes, Priority
from ib_tasks.exceptions.action_custom_exceptions import InvalidActionException
from ib_tasks.exceptions.custom_exceptions import InvalidProjectId
from ib_tasks.exceptions.datetime_custom_exceptions import (
    StartDateTimeIsRequired, DueDateTimeIsRequired, DueDateTimeHasExpired,
    DueDateTimeWithoutStartDateTimeIsNotValid, StartDateIsAheadOfDueDate
)
from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields
from ib_tasks.exceptions.task_custom_exceptions import (
    InvalidTaskTemplateDBId, InvalidTaskTemplateOfProject, PriorityIsRequired
)
from ib_tasks.interactors.create_or_update_task.create_task_interactor import \
    TaskDetailsValidationsStorages
from ib_tasks.interactors.create_or_update_task \
    .gofs_details_validations_interactor import \
    GoFsDetailsValidationsInteractor
from ib_tasks.interactors.task_dtos import CreateTaskDTO, GoFFieldsDTO


class TaskDetailsValidationsInteractor:

    def __init__(self, storages_dto: TaskDetailsValidationsStorages):
        self.task_template_storage = storages_dto.task_template_storage
        self.storage = storages_dto.storage
        self.action_storage = storages_dto.action_storage
        self.task_storage = storages_dto.task_storage
        self.gof_storage = storages_dto.gof_storage
        self.create_task_storage = storages_dto.create_task_storage
        self.field_storage = storages_dto.field_storage

    def perform_task_details_validations(self, task_dto: CreateTaskDTO):
        self._validate_project_id(task_dto.project_id)
        self._validate_task_template_id(task_dto.task_template_id)
        self._validate_task_template_project_id(
            task_dto.project_id, task_dto.task_template_id)
        self._validate_action_id(task_dto.action_id)
        action_type = self.action_storage.get_action_type_for_given_action_id(
            action_id=task_dto.action_id)
        self._validate_task_details(task_dto, action_type)
        gofs_details_validation_interactor = GoFsDetailsValidationsInteractor(
            self.task_storage, self.gof_storage,
            self.create_task_storage, self.storage,
            self.field_storage, self.task_template_storage
        )
        gofs_details_validation_interactor.perform_gof_details_validations(
            gof_fields_dtos=task_dto.gof_fields_dtos,
            user_id=task_dto.created_by_id,
            task_template_id=task_dto.task_template_id,
            project_id=task_dto.project_id, action_type=action_type)
        action_type_is_not_no_validations = \
            action_type != ActionTypes.NO_VALIDATIONS.value
        if action_type_is_not_no_validations:
            self._validate_all_user_template_permitted_fields_are_filled_or_not(
                user_id=task_dto.created_by_id, project_id=task_dto.project_id,
                task_template_id=task_dto.task_template_id,
                gof_fields_dtos=task_dto.gof_fields_dtos
            )

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

    def _validate_task_template_id(
            self, task_template_id: str
    ) -> Optional[InvalidTaskTemplateDBId]:
        task_template_existence = \
            self.task_template_storage.check_is_template_exists(
                template_id=task_template_id)
        if not task_template_existence:
            raise InvalidTaskTemplateDBId(task_template_id)
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

    def _validate_task_details(
            self, task_dto: CreateTaskDTO,
            action_type: Optional[ActionTypes]
    ) -> Optional[Exception]:
        start_datetime = task_dto.start_datetime
        due_datetime = task_dto.due_datetime
        self._validate_due_datetime_without_start_datetime(
            start_datetime, due_datetime)
        action_type_is_no_validations = \
            action_type == ActionTypes.NO_VALIDATIONS.value
        self._validate_priority_in_no_validations_case(
            task_dto.priority, action_type_is_no_validations)
        if action_type_is_no_validations and due_datetime is None:
            return
        start_datetime_is_emtpy = not start_datetime
        due_datetime_is_empty = not due_datetime
        if start_datetime_is_emtpy:
            raise StartDateTimeIsRequired()
        if due_datetime_is_empty:
            raise DueDateTimeIsRequired()
        self._validate_start_date_and_due_date_dependencies(
            start_datetime, due_datetime)
        import datetime
        due_datetime_is_expired = due_datetime <= datetime.datetime.now()
        if due_datetime_is_expired:
            raise DueDateTimeHasExpired(due_datetime)

    @staticmethod
    def _validate_due_datetime_without_start_datetime(
            start_datetime, due_datetime
    ) -> Optional[DueDateTimeWithoutStartDateTimeIsNotValid]:
        due_datetime_given_without_start_date = not start_datetime and \
                                                due_datetime
        if due_datetime_given_without_start_date:
            raise DueDateTimeWithoutStartDateTimeIsNotValid(due_datetime)
        return

    @staticmethod
    def _validate_priority_in_no_validations_case(
            priority: Priority, action_type_is_no_validations: bool
    ) -> Optional[PriorityIsRequired]:
        priority_is_not_given = not priority
        if priority_is_not_given and not action_type_is_no_validations:
            raise PriorityIsRequired()
        return

    @staticmethod
    def _validate_start_date_and_due_date_dependencies(start_date,
                                                       due_date):
        start_date_is_ahead_of_due_date = start_date > due_date
        if start_date_is_ahead_of_due_date:
            raise StartDateIsAheadOfDueDate(start_date, due_date)

    def _validate_all_user_template_permitted_fields_are_filled_or_not(
            self, user_id: str, project_id: str, task_template_id: str,
            gof_fields_dtos: List[GoFFieldsDTO]
    ):
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        user_roles = roles_service_adapter.roles_service \
            .get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id)
        template_gof_ids = self.task_template_storage.get_gof_ids_of_template(
            template_id=task_template_id)
        gof_id_with_display_name_dtos = \
            self.gof_storage.get_user_write_permitted_gof_ids_in_given_gof_ids(
                user_roles, template_gof_ids)
        user_permitted_gof_ids = [
            dto.gof_id for dto in gof_id_with_display_name_dtos]
        field_id_with_display_name_dtos = \
            self.field_storage \
                .get_user_write_permitted_field_ids_for_given_gof_ids(
                user_roles, user_permitted_gof_ids)
        filled_gof_ids = [
            gof_field_dto.gof_id for gof_field_dto in gof_fields_dtos]
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
