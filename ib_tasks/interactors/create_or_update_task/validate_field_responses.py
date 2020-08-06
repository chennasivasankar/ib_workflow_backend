from typing import List, Optional

from ib_tasks.exceptions.field_values_custom_exceptions import \
    EmptyValueForRequiredField
from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import NumberFieldValidationInteractor, FloatFieldValidationInteractor, \
    DropDownFieldValidationInteractor, GoFSelectorFieldValidationInteractor, \
    RadioGroupFieldValidationInteractor, \
    CheckBoxGroupFieldValidationInteractor, \
    MultiSelectFieldValidationInteractor, DateFieldValidationInteractor, \
    TimeFieldValidationInteractor, ImageUploaderFieldValidationInteractor, \
    FileUploaderFieldValidationInteractor, \
    PhoneNumberFieldValidationInteractor, URLFieldValidationInteractor, \
    EmailFieldValidationInteractor, PasswordFieldValidationInteractor, \
    MultiSelectLabelFieldValidationInteractor
from ib_tasks.interactors.create_or_update_task.field_response_validations. \
    base_field_validation import BaseFieldValidation
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import FieldValuesDTO


class ValidateFieldResponsesInteractor:

    def __init__(
            self, field_storage: FieldsStorageInterface
    ):
        self.field_storage = field_storage

    def validate_field_responses(
            self, field_values_dtos: List[FieldValuesDTO]
    ) -> Optional[Exception]:
        field_ids = [
            field_values_dto.field_id
            for field_values_dto in field_values_dtos
        ]
        field_details_dtos = self.field_storage. \
            get_field_details_for_given_field_ids(field_ids=field_ids)
        for field_details_dto in field_details_dtos:
            field_response = self._get_field_response_for_given_field_id(
                field_id=field_details_dto.field_id,
                field_values_dtos=field_values_dtos
            )
            field_validation_required = \
                field_response or field_details_dto.required
            if field_validation_required:
                self._validate_field_response(
                    field_response, field_details_dto)
        return

    @staticmethod
    def _get_field_response_for_given_field_id(
            field_id: str, field_values_dtos: List[FieldValuesDTO]
    ) -> Optional[str]:
        for field_values_dto in field_values_dtos:
            field_id_matched = field_values_dto.field_id == field_id
            if field_id_matched:
                return field_values_dto.field_response
        return

    def _validate_field_response(
            self, field_response: str,
            field_details_dto: FieldCompleteDetailsDTO
    ) -> Optional[Exception]:
        field_response = field_response.strip()
        field_id = field_details_dto.field_id
        field_is_required_but_not_given = (
                not field_response and field_details_dto.required)
        if field_is_required_but_not_given:
            raise EmptyValueForRequiredField(field_id)
        field_validation_interactor = \
            self._get_field_validation_interactor_based_on_field_details(
                field_id, field_response, field_details_dto
            )
        if field_validation_interactor is not None:
            field_validation_interactor.validate_field_response()
        return

    @staticmethod
    def _get_field_validation_interactor_based_on_field_details(
            field_id, field_response, field_details_dto
    ) -> Optional[BaseFieldValidation]:
        from ib_tasks.constants.enum import FieldTypes
        import json
        field_type = field_details_dto.field_type
        if field_type == FieldTypes.PHONE_NUMBER.value:
            return PhoneNumberFieldValidationInteractor(field_id,
                                                        field_response)
        if field_type == FieldTypes.URL.value:
            return URLFieldValidationInteractor(field_id, field_response)
        if field_type == FieldTypes.EMAIL.value:
            return EmailFieldValidationInteractor(field_id, field_response)
        if field_type == FieldTypes.NUMBER.value:
            return NumberFieldValidationInteractor(field_id, field_response)
        if field_type == FieldTypes.PASSWORD.value:
            return PasswordFieldValidationInteractor(field_id, field_response)
        if field_type == FieldTypes.FLOAT.value:
            return FloatFieldValidationInteractor(field_id, field_response)
        if field_type == FieldTypes.DROPDOWN.value:
            valid_dropdown_values = json.loads(field_details_dto.field_values)
            return DropDownFieldValidationInteractor(
                field_id, field_response, valid_dropdown_values)
        if field_type == FieldTypes.GOF_SELECTOR.value:
            field_values_dicts = json.loads(field_details_dto.field_values)
            valid_gof_selector_names = [
                field_values_dict['name']
                for field_values_dict in field_values_dicts
            ]
            return GoFSelectorFieldValidationInteractor(
                field_id, field_response, valid_gof_selector_names)
        if field_type == FieldTypes.RADIO_GROUP.value:
            valid_radio_group_options = json.loads(
                field_details_dto.field_values)
            return RadioGroupFieldValidationInteractor(
                field_id, field_response, valid_radio_group_options
            )
        if field_type == FieldTypes.CHECKBOX_GROUP.value:
            valid_check_box_options = json.loads(
                field_details_dto.field_values)
            return CheckBoxGroupFieldValidationInteractor(
                field_id, field_response, valid_check_box_options
            )
        if field_type == FieldTypes.MULTI_SELECT_FIELD.value:
            valid_multi_select_options = json.loads(
                field_details_dto.field_values)
            return MultiSelectFieldValidationInteractor(
                field_id, field_response, valid_multi_select_options
            )
        if field_type == FieldTypes.MULTI_SELECT_LABELS.value:
            valid_multi_select_labels = json.loads(
                field_details_dto.field_values
            )
            return MultiSelectLabelFieldValidationInteractor(
                field_id, field_response, valid_multi_select_labels)
        if field_type == FieldTypes.DATE.value:
            return DateFieldValidationInteractor(field_id, field_response)
        if field_type == FieldTypes.TIME.value:
            return TimeFieldValidationInteractor(field_id, field_response)
        if field_type == FieldTypes.IMAGE_UPLOADER.value:
            allowed_formats = json.loads(field_details_dto.allowed_formats)
            return ImageUploaderFieldValidationInteractor(
                field_id, field_response, allowed_formats
            )
        if field_type == FieldTypes.FILE_UPLOADER.value:
            allowed_formats = json.loads(field_details_dto.allowed_formats)
            return FileUploaderFieldValidationInteractor(
                field_id, field_response, allowed_formats
            )
        return
