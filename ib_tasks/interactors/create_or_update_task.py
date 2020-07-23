from typing import Optional, List, Union

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.exceptions.custom_exceptions import (
    InvalidFieldIds, InvalidTaskTemplateIds,
    InvalidGoFIds, EmptyValueForPlainTextField)
from ib_tasks.exceptions.fields_custom_exceptions import \
    DuplicationOfFieldIdsExist
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
        except DuplicationOfFieldIdsExist as err:
            return presenter.raise_exception_for_duplicate_field_ids(err)
        except InvalidTaskTemplateIds as err:
            return presenter.raise_exception_for_invalid_task_template_id(err)
        except InvalidGoFIds as err:
            return presenter.raise_exception_for_invalid_gof_ids(err)
        except InvalidFieldIds as err:
            return presenter.raise_exception_for_invalid_field_ids(err)
        except EmptyValueForPlainTextField as err:
            return presenter.raise_exception_for_empty_value_in_plain_text_field(err)

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
        self._validate_for_duplicate_field_ids(field_ids)
        self._validate_task_template_id(task_dto.task_template_id)
        self._validate_for_invalid_gof_ids(gof_ids)
        self._validate_for_invalid_field_ids(field_ids)
        self._validate_field_values(field_values_dtos)

    def _validate_field_values(
            self, field_values_dtos: List[FieldValuesDTO]
    ):
        field_ids = [
            field_values_dto.field_id for field_values_dto in field_values_dtos
        ]
        field_types_dtos = self.storage.get_field_types_for_given_field_ids(
            field_ids=field_ids
        )
        for field_type_dto in field_types_dtos:
            field_value = self._get_field_value_for_given_field_id(
                field_id=field_type_dto.field_id,
                field_values_dtos=field_values_dtos
            )
            field_type = field_type_dto.field_type
            field_type_is_text_field = field_type == FieldTypes.PLAIN_TEXT.value
            if field_type_is_text_field:
                self._validate_for_text_field_value(
                    field_value, field_type_dto.field_id
                )

    @staticmethod
    def _validate_for_text_field_value(
            field_value: str, field_id: str
    ) -> Optional[EmptyValueForPlainTextField]:
        field_value_is_empty = not field_value.strip()
        if field_value_is_empty:
            raise EmptyValueForPlainTextField(field_id)
        return

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

    def _validate_for_duplicate_field_ids(
            self, field_ids: List[str]
    ) -> Optional[DuplicationOfFieldIdsExist]:
        duplicate_field_ids = self._get_duplicates_in_given_list(field_ids)
        if duplicate_field_ids:
            raise DuplicationOfFieldIdsExist(duplicate_field_ids)
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

    @staticmethod
    def _get_field_value_for_given_field_id(
            field_id: str, field_values_dtos: List[FieldValuesDTO]
    ) -> Union[None, str, List[str]]:
        for field_values_dto in field_values_dtos:
            field_id_matched = field_values_dto.field_id == field_id
            if field_id_matched:
                return field_values_dto.field_value
        return
