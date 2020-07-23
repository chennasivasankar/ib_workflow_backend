from typing import Optional, List, Union

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidPhoneNumberValue, EmptyValueForPlainTextField, \
    InvalidEmailFieldValue, InvalidURLValue, NotAStrongPassword, \
    InvalidNumberValue, InvalidFloatValue, \
    InvalidValueForDropdownField, InvalidGoFIDsInGoFSelectorField
from ib_tasks.exceptions.fields_custom_exceptions import \
    DuplicationOfFieldIdsExist, InvalidFieldIds
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateIds
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.presenter_interfaces.create_or_update_task_presenter \
    import CreateOrUpdateTaskPresenterInterface
from ib_tasks.interactors.task_dtos import TaskDTO, FieldValuesDTO, \
    GoFFieldsDTO


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
        except InvalidGoFIDsInGoFSelectorField as err:
            return presenter.raise_exception_for_gof_ids_in_gof_selector_field_value(err)
        except EmptyValueForPlainTextField as err:
            return presenter.raise_exception_for_empty_value_in_plain_text_field(
                err)
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
        field_details_dtos = self.storage.get_field_details_for_given_field_ids(
            field_ids=field_ids
        )
        gof_ids_in_gof_selector = []
        for field_values_dto in field_values_dtos:
            field_type = self._get_field_type_for_given_field_id(
                field_values_dto.field_id, field_details_dtos
            )
            field_type_is_gof_selector = field_type == FieldTypes.GOF_SELECTOR.value
            if field_type_is_gof_selector:
                gof_ids_in_gof_selector.append(field_values_dto.field_value)
        valid_gof_ids = self.storage.get_valid_gof_ids_in_given_gof_ids(
            gof_ids_in_gof_selector
        )
        invalid_gof_ids = list(set(gof_ids_in_gof_selector) - set(valid_gof_ids))
        if invalid_gof_ids:
            raise InvalidGoFIDsInGoFSelectorField(invalid_gof_ids)

        for field_details_dto in field_details_dtos:
            field_value = self._get_field_value_for_given_field_id(
                field_id=field_details_dto.field_id,
                field_values_dtos=field_values_dtos
            )
            field_value = field_value.strip()
            field_type = field_details_dto.field_type
            field_id = field_details_dto.field_id
            field_type_is_text_field = field_type == FieldTypes.PLAIN_TEXT.value
            if field_type_is_text_field:
                self._validate_for_text_field_value(field_value, field_id)
            field_type_is_phone_number = field_type == FieldTypes.PHONE_NUMBER.value
            if field_type_is_phone_number:
                self._validate_phone_number_value(field_value, field_id)
            field_type_is_email = field_type == FieldTypes.EMAIL.value
            if field_type_is_email:
                self._validate_for_email_field_value(field_value, field_id)
            field_type_is_url = field_type == FieldTypes.URL.value
            if field_type_is_url:
                self._validate_for_url_field_value(field_value, field_id)
            field_type_is_password = field_type == FieldTypes.PASSWORD.value
            if field_type_is_password:
                self._validate_for_strong_password(field_value, field_id)
            field_type_is_number = field_type == FieldTypes.NUMBER.value
            if field_type_is_number:
                self._validate_for_number_value(field_value, field_id)
            field_type_is_float = field_type == FieldTypes.FLOAT.value
            if field_type_is_float:
                self._validate_for_float_value(field_value, field_id)
            field_type_is_dropdown = field_type == FieldTypes.DROPDOWN.value
            if field_type_is_dropdown:
                valid_dropdown_values = field_details_dto.field_values
                self._validate_for_dropdown_field_value(
                    field_value, field_id, valid_dropdown_values
                )
            field_type_is_gof_selector = field_type == FieldTypes.GOF_SELECTOR.value
            if field_type_is_gof_selector:
                #  TODO: check valid gof_id option in valid list of gof ids
                # in given json stringified list
                pass

    @staticmethod
    def _validate_for_dropdown_field_value(
            field_value: str, field_id: str, valid_dropdown_values: List[str]
    ) -> Optional[InvalidValueForDropdownField]:
        invalid_dropdown_value = field_value not in valid_dropdown_values
        if invalid_dropdown_value:
            raise InvalidValueForDropdownField(
                field_id, field_value, valid_dropdown_values
            )
        return

    @staticmethod
    def _validate_for_float_value(
            field_value: str, field_id: str
    ) -> Optional[InvalidFloatValue]:
        invalid_float_value = not field_value.replace('.', '', 1).isdigit()
        if invalid_float_value:
            raise InvalidFloatValue(field_id, field_value)
        return

    @staticmethod
    def _validate_for_number_value(
            field_value: str, field_id: str
    ) -> Optional[InvalidNumberValue]:
        invalid_number_value = not field_value.isdigit()
        if invalid_number_value:
            raise InvalidNumberValue(field_id, field_value)
        return

    @staticmethod
    def _validate_for_strong_password(
            field_value: str, field_id: str
    ) -> Optional[NotAStrongPassword]:
        import re
        from ib_tasks.constants.config import STRONG_PASSWORD_REGEX
        password_is_not_strong_enough = not re.search(
            STRONG_PASSWORD_REGEX, field_value
        )
        if password_is_not_strong_enough:
            raise NotAStrongPassword(field_id, field_value)
        return

    @staticmethod
    def _validate_for_url_field_value(
            field_value: str, field_id: str
    ) -> Optional[InvalidURLValue]:
        from ib_tasks.constants.config import VALID_URL_REGEX_PATTERN
        url_is_invalid = not VALID_URL_REGEX_PATTERN.search(field_value)
        if url_is_invalid:
            raise InvalidURLValue(field_id, field_value)
        return

    @staticmethod
    def _validate_for_email_field_value(
            field_value: str, field_id: str
    ) -> Optional[InvalidEmailFieldValue]:
        import re
        from ib_tasks.constants.config import VALID_EMAIL_REGEX
        email_address_is_invalid = not re.search(VALID_EMAIL_REGEX,
                                                 field_value)
        if email_address_is_invalid:
            raise InvalidEmailFieldValue(field_id, field_value)
        return

    @staticmethod
    def _validate_phone_number_value(
            field_value: str, field_id: str
    ) -> Optional[InvalidPhoneNumberValue]:
        phone_number_has_non_digit_chars = field_value.isdigit()
        if phone_number_has_non_digit_chars:
            raise InvalidPhoneNumberValue(field_id, field_value)
        phone_number_does_not_contain_10_digits = len(field_value) != 10
        if phone_number_does_not_contain_10_digits:
            raise InvalidPhoneNumberValue(field_id, field_value)
        return

    @staticmethod
    def _validate_for_text_field_value(
            field_value: str, field_id: str
    ) -> Optional[EmptyValueForPlainTextField]:
        field_value_is_empty = not field_value
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

    @staticmethod
    def _get_field_type_for_given_field_id(
            field_id: str, field_details_dtos: List[FieldDetailsDTO]
    ) -> Union[None, str, List[str]]:
        for field_details_dto in field_details_dtos:
            field_id_matched = field_details_dto.field_id == field_id
            if field_id_matched:
                return field_details_dto.field_type
        return
