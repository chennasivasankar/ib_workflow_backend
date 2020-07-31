from ib_tasks.exceptions.field_values_custom_exceptions import \
    EmptyValueForPlainTextField, InvalidGoFIDsInGoFSelectorField, \
    InvalidUrlForFile, InvalidUrlForImage, InvalidImageFormat, \
    InvalidTimeFormat, InvalidDateFormat, \
    IncorrectMultiSelectLabelsSelected, IncorrectMultiSelectOptionsSelected, \
    IncorrectCheckBoxOptionsSelected, IncorrectRadioGroupChoice, \
    IncorrectGoFIDInGoFSelectorField, InvalidValueForDropdownField, \
    InvalidFloatValue, InvalidNumberValue, NotAStrongPassword, InvalidURLValue, \
    InvalidEmailFieldValue, InvalidPhoneNumberValue, InvalidFileFormat, \
    EmptyValueForRequiredField
from ib_tasks.exceptions.fields_custom_exceptions import \
    DuplicationOfFieldIdsExist, InvalidFieldIds
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateIds, \
    InvalidTaskException
from ib_tasks.interactors.presenter_interfaces.create_or_update_task_presenter \
    import CreateOrUpdateTaskPresenterInterface
from django.http import response
import json
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin


class CreateOrUpdateTaskPresenterImplementation(
    CreateOrUpdateTaskPresenterInterface, HTTPResponseMixin
):
    def raise_exception_for_invalid_task_id(self, err: InvalidTaskException):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_ID
        response_message = INVALID_TASK_ID[0].format(
            err.task_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_TASK_ID[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_empty_value_in_required_field(self,
                                                          err: EmptyValueForRequiredField):
        from ib_tasks.constants.exception_messages import \
            EMPTY_VALUE_FOR_REQUIRED_FIELD
        response_message = EMPTY_VALUE_FOR_REQUIRED_FIELD[0].format(
            err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": EMPTY_VALUE_FOR_REQUIRED_FIELD[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_not_acceptable_file_format(self,
                                                       err: InvalidFileFormat):
        from ib_tasks.constants.exception_messages import \
            INVALID_FILE_FORMAT
        response_message = INVALID_FILE_FORMAT[0].format(
            err.given_format, err.field_id, err.allowed_formats
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FILE_FORMAT[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_phone_number_value(self,
                                                       err: InvalidPhoneNumberValue):
        from ib_tasks.constants.exception_messages import \
            INVALID_PHONE_NUMBER_VALUE
        response_message = INVALID_PHONE_NUMBER_VALUE[0].format(
            err.field_value, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_PHONE_NUMBER_VALUE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_email_address(self,
                                                  err: InvalidEmailFieldValue):
        from ib_tasks.constants.exception_messages import \
            INVALID_EMAIL
        response_message = INVALID_EMAIL[0].format(
            err.field_value, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_EMAIL[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_url_address(self, err: InvalidURLValue):
        from ib_tasks.constants.exception_messages import INVALID_URL
        response_message = INVALID_URL[0].format(
            err.field_value, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_URL[1]
        }
        return self.prepare_400_bad_request_response(response_dict=data)

    def raise_exception_for_weak_password(self, err: NotAStrongPassword):
        from ib_tasks.constants.exception_messages import NOT_A_STRONG_PASSWORD
        response_message = NOT_A_STRONG_PASSWORD[0].format(
            err.field_value, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": NOT_A_STRONG_PASSWORD[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_number_value(self,
                                                 err: InvalidNumberValue):
        from ib_tasks.constants.exception_messages import INVALID_NUMBER_VALUE
        response_message = INVALID_NUMBER_VALUE[0].format(
            err.field_value, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_NUMBER_VALUE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_float_value(self, err: InvalidFloatValue):
        from ib_tasks.constants.exception_messages import INVALID_FLOAT_VALUE
        response_message = INVALID_FLOAT_VALUE[0].format(
            err.field_value, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FLOAT_VALUE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_dropdown_value(self,
                                                   err: InvalidValueForDropdownField):
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_DROPDOWN
        response_message = INVALID_VALUE_FOR_DROPDOWN[0].format(
            err.field_value, err.field_id, err.valid_values
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_VALUE_FOR_DROPDOWN[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exceptions_for_invalid_gof_id_selected_in_gof_selector(self,
                                                                     err: IncorrectGoFIDInGoFSelectorField):
        from ib_tasks.constants.exception_messages import \
            INCORRECT_GOF_ID_IN_GOF_SELECTOR_FIELD
        response_message = INCORRECT_GOF_ID_IN_GOF_SELECTOR_FIELD[0].format(
            err.field_value, err.field_id, err.valid_gof_id_options
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INCORRECT_GOF_ID_IN_GOF_SELECTOR_FIELD[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_choice_in_radio_group_field(self,
                                                                err: IncorrectRadioGroupChoice):
        from ib_tasks.constants.exception_messages import \
            INCORRECT_RADIO_GROUP_CHOICE
        response_message = INCORRECT_RADIO_GROUP_CHOICE[0].format(
            err.field_value, err.field_id, err.valid_radio_group_options
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INCORRECT_RADIO_GROUP_CHOICE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_checkbox_group_options_selected(self,
                                                                    err: IncorrectCheckBoxOptionsSelected):
        from ib_tasks.constants.exception_messages import \
            INCORRECT_CHECK_BOX_OPTIONS_SELECTED
        response_message = INCORRECT_CHECK_BOX_OPTIONS_SELECTED[0].format(
            err.invalid_checkbox_options, err.field_id,
            err.valid_check_box_options
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INCORRECT_CHECK_BOX_OPTIONS_SELECTED[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_multi_select_options_selected(self,
                                                                  err: IncorrectMultiSelectOptionsSelected):
        from ib_tasks.constants.exception_messages import \
            INCORRECT_MULTI_SELECT_OPTIONS_SELECTED
        response_message = INCORRECT_MULTI_SELECT_OPTIONS_SELECTED[0].format(
            err.invalid_multi_select_options, err.field_id,
            err.valid_multi_select_options
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INCORRECT_MULTI_SELECT_OPTIONS_SELECTED[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_multi_select_labels_selected(self,
                                                                 err: IncorrectMultiSelectLabelsSelected):
        from ib_tasks.constants.exception_messages import \
            INCORRECT_MULTI_SELECT_LABELS_SELECTED
        response_message = INCORRECT_MULTI_SELECT_LABELS_SELECTED[0].format(
            err.invalid_multi_select_labels, err.field_id,
            err.valid_multi_select_labels
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INCORRECT_MULTI_SELECT_LABELS_SELECTED[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_date_format(self, err: InvalidDateFormat):
        from ib_tasks.constants.exception_messages import INVALID_DATE_FORMAT
        response_message = INVALID_DATE_FORMAT[0].format(
            err.field_value, err.field_id, err.expected_format
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_DATE_FORMAT[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_time_format(self, err: InvalidTimeFormat):
        from ib_tasks.constants.exception_messages import INVALID_TIME_FORMAT
        response_message = INVALID_TIME_FORMAT[0].format(
            err.field_value, err.field_id, err.expected_format
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_TIME_FORMAT[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_not_acceptable_image_format(self,
                                                        err: InvalidImageFormat):
        from ib_tasks.constants.exception_messages import INVALID_IMAGE_FORMAT
        response_message = INVALID_IMAGE_FORMAT[0].format(
            err.given_format, err.field_id, err.allowed_formats
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_IMAGE_FORMAT[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_image_url(self, err: InvalidUrlForImage):
        from ib_tasks.constants.exception_messages import INVALID_IMAGE_URL
        response_message = INVALID_IMAGE_URL[0].format(
            err.image_url, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_IMAGE_URL[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_file_url(self, err: InvalidUrlForFile):
        from ib_tasks.constants.exception_messages import INVALID_FILE_URL
        response_message = INVALID_FILE_URL[0].format(
            err.file_url, err.field_id
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FILE_URL[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_gof_ids_in_gof_selector_field_value(self,
                                                                err: InvalidGoFIDsInGoFSelectorField):
        from ib_tasks.constants.exception_messages import \
            INVALID_GOF_IDS_IN_GOF_SELECTOR_FIELD
        response_message = INVALID_GOF_IDS_IN_GOF_SELECTOR_FIELD[0].format(
            err.gof_ids
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_GOF_IDS_IN_GOF_SELECTOR_FIELD[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_duplicate_field_ids(self,
                                                err: DuplicationOfFieldIdsExist):
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_FIELD_IDS
        response_message = DUPLICATE_FIELD_IDS[0].format(
            str(err.field_ids)
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": DUPLICATE_FIELD_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_task_template_id(
            self, err: InvalidTaskTemplateIds
    ):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_TEMPLATE_IDS
        response_message = INVALID_TASK_TEMPLATE_IDS[0].format(
            str(err.invalid_task_template_ids)
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_TASK_TEMPLATE_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_gof_ids(self, err: InvalidGoFIds):
        from ib_tasks.constants.exception_messages import \
            INVALID_GOF_IDS
        response_message = INVALID_GOF_IDS[0].format(str(err.gof_ids))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_GOF_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_exception_for_invalid_field_ids(self, err: InvalidFieldIds):
        from ib_tasks.constants.exception_messages import \
            INVALID_FIELD_IDS
        response_message = INVALID_FIELD_IDS[0].format(str(err.field_ids))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FIELD_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def get_response_for_create_or_update_task(self):
        data = {
            "message": "task created or updated successfully"
        }
        return self.prepare_201_created_response(response_dict=data)

    def raise_exception_for_empty_value_in_plain_text_field(
            self, err: EmptyValueForPlainTextField
    ):
        from ib_tasks.constants.exception_messages import \
            EMPTY_VALUE_FOR_PLAIN_TEXT_FIELD
        response_message = EMPTY_VALUE_FOR_PLAIN_TEXT_FIELD[0].format(
            str(err.field_id)
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": EMPTY_VALUE_FOR_PLAIN_TEXT_FIELD[1]
        }
        return self.prepare_400_bad_request_response(data)
