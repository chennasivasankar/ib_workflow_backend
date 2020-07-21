from typing import Optional, List

from ib_tasks.exceptions.custom_exceptions import TaskTemplateIdCantBeEmpty, \
    InvalidGoFIds, InvalidFieldIds, InvalidTaskTemplateIds
from ib_tasks.interactors.dtos import TaskDTO, GoFFieldsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.presenter_interfaces.create_or_update_task_presenter \
    import CreateOrUpdateTaskPresenterInterface


class CreateOrUpdateTaskInteractor:

    def __init__(self, storage: TaskStorageInterface):
        self.storage = storage

    def create_or_update_task_wrapper(
            self, presenter: CreateOrUpdateTaskPresenterInterface,
            task_dto: TaskDTO
    ):

        try:
            return self._prepare_response_for_create_or_update_task(
                presenter=presenter, task_dto=task_dto
            )
        except InvalidTaskTemplateIds as err:
            return presenter.raise_exception_for_invalid_task_template_id(err)
        except InvalidGoFIds as err:
            return presenter.raise_exception_for_invalid_gof_ids(err)
        except InvalidFieldIds as err:
            return presenter.raise_exception_for_invalid_field_ids(err)

    def _prepare_response_for_create_or_update_task(
            self, presenter: CreateOrUpdateTaskPresenterInterface,
            task_dto: TaskDTO
    ):
        self.create_or_update_task(task_dto)
        response = presenter.get_response_for_create_or_update_task()
        return response

    def create_or_update_task(self, task_dto: TaskDTO):
        self._validate_task_template_id(task_dto.task_template_id)
        self._validate_for_invalid_gof_ids(task_dto.gof_fields_dtos)
        self._validate_for_invalid_field_ids(task_dto.gof_fields_dtos)

    def _validate_task_template_id(
            self, task_template_id: str
    ) -> Optional[InvalidTaskTemplateIds]:
        task_template_existence = \
            self.storage.check_is_template_exists(template_id=task_template_id)
        if not task_template_existence:
            raise InvalidTaskTemplateIds(
                invalid_task_template_ids=[task_template_id]
            )
        return

    def _validate_for_invalid_gof_ids(
            self, gof_fields_dtos: List[GoFFieldsDTO]
    ) -> Optional[InvalidGoFIds]:
        gof_ids = [gof_fields_dto.gof_id for gof_fields_dto in gof_fields_dtos]
        valid_gof_ids = self.storage.get_existing_gof_ids(gof_ids)
        invalid_gof_ids = list(set(gof_ids) - set(valid_gof_ids))
        if invalid_gof_ids:
            raise InvalidGoFIds(gof_ids)
        return

    def _validate_for_invalid_field_ids(
            self, gof_fields_dtos: List[GoFFieldsDTO]
    ) -> Optional[InvalidFieldIds]:

        field_ids = []
        for gof_fields_dto in gof_fields_dtos:
            field_ids += [
                field_value_dto.field_id
                for field_value_dto in gof_fields_dto.field_values_dtos
            ]
        field_ids = list(set(field_ids))
        valid_field_ids = self.storage.get_existing_field_ids(field_ids)
        invalid_field_ids = list(set(field_ids) - set(valid_field_ids))
        if invalid_field_ids:
            from ib_tasks.constants.exception_messages import \
                INVALID_FIELD_IDS_MESSAGE
            INVALID_FIELD_IDS_MESSAGE += str(invalid_field_ids)
            raise InvalidFieldIds(INVALID_FIELD_IDS_MESSAGE)
        return
