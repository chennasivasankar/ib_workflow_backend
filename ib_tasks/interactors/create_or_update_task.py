from typing import Optional, List

from ib_tasks.exceptions.custom_exceptions import TaskTemplateIdCantBeEmpty, \
    InvalidGoFIds, InvalidFieldIds, InvalidTaskTemplateIds, DuplicateGoFIds
from ib_tasks.interactors.dtos import TaskDTO, GoFFieldsDTO, FieldValuesDTO
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
        except DuplicateGoFIds as err:
            return presenter.raise_exception_for_duplicate_gof_ids(err)
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
        self._validate_for_duplicate_gof_ids(gof_ids)
        # self._validate_for_duplicate_field_ids(field_ids)
        self._validate_task_template_id(task_dto.task_template_id)
        self._validate_for_invalid_gof_ids(gof_ids)
        self._validate_for_invalid_field_ids(field_ids)
        # TODO: VALIDATE FOR PLAIN_TEXT FIELD TYPE VALUE
        # TODO: GET FIELD VALUES DTOS FROM THE BELOW PRIVATE METHOD
        # TODO: NEXT FIELD TYPE VALIDATION

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
            self, gof_ids: List[str]
    ) -> Optional[InvalidGoFIds]:
        valid_gof_ids = self.storage.get_existing_gof_ids(gof_ids)
        invalid_gof_ids = list(set(gof_ids) - set(valid_gof_ids))
        if invalid_gof_ids:
            raise InvalidGoFIds(gof_ids)
        return

    def _validate_for_invalid_field_ids(
            self, field_ids: List[str]
    ) -> Optional[InvalidFieldIds]:
        valid_field_ids = self.storage.get_existing_field_ids(field_ids)
        invalid_field_ids = list(set(field_ids) - set(valid_field_ids))
        if invalid_field_ids:
            raise InvalidFieldIds(invalid_field_ids)
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

    def _validate_for_duplicate_gof_ids(
            self, gof_ids: List[str]
    ) -> Optional[DuplicateGoFIds]:
        duplicate_gof_ids = self._get_duplicates_in_given_list(gof_ids)
        if duplicate_gof_ids:
            raise DuplicateGoFIds(duplicate_gof_ids)
        return

    @staticmethod
    def _get_duplicates_in_given_list(values: List):
        duplicate_values = list(
            set(
                [
                    value
                    for value in values if values.count(value) > 1
                ]
            )
        )
        return duplicate_values

