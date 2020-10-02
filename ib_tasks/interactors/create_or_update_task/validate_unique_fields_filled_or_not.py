from typing import List, Optional

from ib_tasks.exceptions.fields_custom_exceptions import \
    FieldsFilledAlreadyBySomeone
from ib_tasks.interactors.mixins.get_gofs_feilds_display_names_mixin import \
    GetGoFsFieldsDisplayNameMixin
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldWithGoFDisplayNameDTO, FieldDetailsWithFilledResponse
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import FieldValuesDTO


class ValidateUniqueFieldsFilledInteractor(GetGoFsFieldsDisplayNameMixin):

    def __init__(
            self, field_storage: FieldsStorageInterface,
            task_storage: TaskStorageInterface):
        self.field_storage = field_storage
        self.task_storage = task_storage

    def validate_unique_fields_filled_in_task_creation(
            self, field_values_dtos: List[FieldValuesDTO], project_id: str,
            task_template_id: str):
        field_ids = [dto.field_id for dto in field_values_dtos]
        unique_fields = self._get_unique_field_ids_in_given_field_ids(
            field_ids)
        self._validate_unique_fields_are_not_filled_again_in_task_creation(
            field_values_dtos, project_id, task_template_id, unique_fields)

    def validate_unique_fields_filled_in_task_updation(
            self, field_values_dtos: List[FieldValuesDTO], task_id: int):
        field_ids = [dto.field_id for dto in field_values_dtos]
        unique_fields = self._get_unique_field_ids_in_given_field_ids(
            field_ids)
        self._validate_unique_fields_are_not_filled_again_in_task_updation(
            field_values_dtos, task_id, unique_fields)

    def _get_unique_field_ids_in_given_field_ids(
            self, given_field_ids: List[str]):
        unique_field_ids = \
            self.field_storage.get_unique_field_ids_in_given_field_ids(
                given_field_ids)
        return unique_field_ids

    def _validate_unique_fields_are_not_filled_again_in_task_creation(
            self, given_fields: List[FieldValuesDTO], project_id: str,
            task_template_id: str, unique_field_ids: List[str]):
        if unique_field_ids:
            already_filled_unique_fields_details = \
                self._get_already_filled_unique_field_details_in_task_creation(
                    project_id, task_template_id, unique_field_ids)
            self._validate_that_unique_fields_are_not_filled_in_another_task(
                given_fields, already_filled_unique_fields_details)
        return

    def _validate_unique_fields_are_not_filled_again_in_task_updation(
            self, given_fields: List[FieldValuesDTO], task_id: int,
            unique_field_ids: List[str]):
        if unique_field_ids:
            already_filled_unique_fields_details = \
                self._get_already_filled_unique_field_details_in_task_updation(
                    task_id, unique_field_ids)
            self._validate_that_unique_fields_are_not_filled_in_another_task(
                given_fields, already_filled_unique_fields_details)
        return

    def _get_already_filled_unique_field_details_in_task_creation(
            self, project_id: str,
            task_template_id: str, unique_field_ids: List[str]
    ) -> List[FieldDetailsWithFilledResponse]:
        already_filled_unique_fields_details = \
            self.task_storage.get_filled_fields_for_given_project_template(
                project_id, task_template_id, unique_field_ids)
        return already_filled_unique_fields_details

    def _get_already_filled_unique_field_details_in_task_updation(
            self, task_id: int, unique_field_ids: List[str]
    ) -> List[FieldDetailsWithFilledResponse]:
        already_filled_unique_fields_details = \
            self.task_storage.get_filled_fields_if_filled_in_another_task_than_given_task(
                task_id, unique_field_ids)
        return already_filled_unique_fields_details

    def _validate_that_unique_fields_are_not_filled_in_another_task(
            self, given_fields: List[FieldValuesDTO],
            already_filled_fields_details: List[FieldDetailsWithFilledResponse]
    ) -> Optional[FieldsFilledAlreadyBySomeone]:
        given_filled_unique_field_ids = \
            self._get_given_unique_field_ids_with_same_response(
                given_fields, already_filled_fields_details)
        if given_filled_unique_field_ids:
            unique_field_display_names = self.get_field_display_names(
                given_filled_unique_field_ids, already_filled_fields_details)
            raise FieldsFilledAlreadyBySomeone(unique_field_display_names)
        return

    @staticmethod
    def _get_given_unique_field_ids_with_same_response(
            given_fields: List[FieldValuesDTO],
            already_filled_fields_details: List[FieldDetailsWithFilledResponse]
    ) -> List[str]:
        given_unique_field_ids = []
        for given_field in given_fields:
            for field in already_filled_fields_details:
                same_field_response_for_unique_field = (
                    field.field_id == given_field.field_id and
                    field.field_response == given_field.field_response)
                if same_field_response_for_unique_field:
                    given_unique_field_ids.append(given_field.field_id)
        return given_unique_field_ids
