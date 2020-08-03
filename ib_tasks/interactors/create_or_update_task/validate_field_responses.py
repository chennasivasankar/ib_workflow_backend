from typing import List, Optional

from ib_tasks.interactors.create_or_update_task.field_response_validations.\
    base_field_validation import BaseFieldValidation
from ib_tasks.exceptions.field_values_custom_exceptions import \
    EmptyValueForRequiredField, InvalidPhoneNumberValue, \
    InvalidEmailFieldValue, InvalidURLValue, NotAStrongPassword, \
    InvalidNumberValue, InvalidFloatValue, InvalidValueForDropdownField, \
    IncorrectRadioGroupChoice, IncorrectCheckBoxOptionsSelected, \
    IncorrectMultiSelectOptionsSelected, IncorrectMultiSelectLabelsSelected, \
    InvalidDateFormat, InvalidTimeFormat, InvalidUrlForImage, \
    InvalidImageFormat, InvalidUrlForFile, InvalidFileFormat, \
    IncorrectNameInGoFSelectorField
from ib_tasks.interactors.create_or_update_task.field_response_validations \
    import NumberFieldValidationInteractor, FloatFieldValidationInteractor, \
    DropDownFieldValidationInteractor, GoFSelectorFieldValidationInteractor, \
    RadioGroupFieldValidationInteractor, \
    CheckBoxGroupFieldValidationInteractor, \
    MultiSelectFieldValidationInteractor, DateFieldValidationInteractor, \
    TimeFieldValidationInteractor, ImageUploaderFieldValidationInteractor, \
    FileUploaderFieldValidationInteractor
from ib_tasks.interactors.presenter_interfaces. \
    create_or_update_task_presenter import CreateOrUpdateTaskPresenterInterface
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import FieldValuesDTO


class ValidateFieldResponsesInteractor:

    def __init__(
            self, field_values_dtos: List[FieldValuesDTO],
            task_storage: TaskStorageInterface
    ):
        self.field_values_dtos = field_values_dtos
        self.task_storage = task_storage

    def validate_field_responses_wrapper(
            self, presenter: CreateOrUpdateTaskPresenterInterface
    ):
        try:
            self.validate_field_responses()
        except EmptyValueForRequiredField as err:
            return presenter. \
                raise_exception_for_empty_value_in_required_field(err)
        except InvalidPhoneNumberValue as err:
            return presenter.raise_exception_for_invalid_phone_number_value(
                err)
        except InvalidEmailFieldValue as err:
            return presenter.raise_exception_for_invalid_email_address(err)
        except InvalidURLValue as err:
            return presenter.raise_exception_for_invalid_url_address(err)
        except NotAStrongPassword as err:
            return presenter.raise_exception_for_weak_password(err)
        except InvalidNumberValue as err:
            return presenter.raise_exception_for_invalid_number_value(err)
        except InvalidFloatValue as err:
            return presenter.raise_exception_for_invalid_float_value(err)
        except InvalidValueForDropdownField as err:
            return presenter.raise_exception_for_invalid_dropdown_value(err)
        except IncorrectNameInGoFSelectorField as err:
            return presenter. \
                raise_exception_for_invalid_name_in_gof_selector_field_value(
                    err
                )
        except IncorrectRadioGroupChoice as err:
            return presenter. \
                raise_exception_for_invalid_choice_in_radio_group_field(err)
        except IncorrectCheckBoxOptionsSelected as err:
            return presenter. \
                raise_exception_for_invalid_checkbox_group_options_selected(
                    err
                )
        except IncorrectMultiSelectOptionsSelected as err:
            return presenter. \
                raise_exception_for_invalid_multi_select_options_selected(err)
        except IncorrectMultiSelectLabelsSelected as err:
            return presenter. \
                raise_exception_for_invalid_multi_select_labels_selected(err)
        except InvalidDateFormat as err:
            return presenter.raise_exception_for_invalid_date_format(err)
        except InvalidTimeFormat as err:
            return presenter.raise_exception_for_invalid_time_format(err)
        except InvalidUrlForImage as err:
            return presenter.raise_exception_for_invalid_image_url(err)
        except InvalidImageFormat as err:
            return presenter.raise_exception_for_not_acceptable_image_format(
                err)
        except InvalidUrlForFile as err:
            return presenter.raise_exception_for_invalid_file_url(err)
        except InvalidFileFormat as err:
            return presenter.raise_exception_for_not_acceptable_file_format(
                err
            )

    def validate_field_responses(self) -> Optional[Exception]:
        field_ids = [
            field_values_dto.field_id
            for field_values_dto in self.field_values_dtos
        ]
        field_details_dtos = self.task_storage. \
            get_field_details_for_given_field_ids(field_ids=field_ids)
        for field_details_dto in field_details_dtos:
            field_response = self._get_field_response_for_given_field_id(
                field_id=field_details_dto.field_id,
                field_values_dtos=self.field_values_dtos
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
        field_validation_interactor.validate_field_response()
        return

    @staticmethod
    def _get_field_validation_interactor_based_on_field_details(
            field_id, field_response, field_details_dto
    ) -> Optional[BaseFieldValidation]:
        from ib_tasks.constants.enum import FieldTypes
        import json
        field_type = field_details_dto.field_type
        if field_type == FieldTypes.NUMBER.value:
            return NumberFieldValidationInteractor(field_id, field_response)
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
