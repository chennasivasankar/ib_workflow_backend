from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidFileFormat, InvalidUrlForFile, InvalidImageFormat, \
    InvalidUrlForImage, InvalidTimeFormat, IncorrectMultiSelectLabelsSelected, \
    IncorrectMultiSelectOptionsSelected, IncorrectCheckBoxOptionsSelected, \
    IncorrectRadioGroupChoice, IncorrectNameInGoFSelectorField, \
    InvalidValueForDropdownField, InvalidFloatValue, InvalidNumberValue, \
    NotAStrongPassword, InvalidURLValue, InvalidEmailFieldValue, \
    InvalidPhoneNumberValue, EmptyValueForRequiredField, InvalidDateFormat
from ib_tasks.exceptions.fields_custom_exceptions import DuplicateFieldIdsToGoF
from ib_tasks.exceptions.gofs_custom_exceptions import \
    InvalidStagePermittedGoFs
from ib_tasks.exceptions.permission_custom_exceptions import \
    UserNeedsFieldWritablePermission, UserNeedsGoFWritablePermission
from ib_tasks.exceptions.task_custom_exceptions import InvalidFieldsOfGoF, \
    InvalidGoFsOfTaskTemplate


class GoFsFieldsValidationPresenterMixin:

    def raise_invalid_gof_ids_exception(self, err):
        from ib_tasks.constants.exception_messages import \
            INVALID_GOF_IDS
        response_message = INVALID_GOF_IDS[0].format(str(err.gof_ids))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_GOF_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_field_ids_exception(self, err):
        from ib_tasks.constants.exception_messages import \
            INVALID_FIELD_IDS
        response_message = INVALID_FIELD_IDS[0].format(str(err.field_ids))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FIELD_IDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_gofs_given_to_a_task_template_exception(
            self, err: InvalidGoFsOfTaskTemplate
    ):
        from ib_tasks.constants.exception_messages import \
            INVALID_GOFS_OF_TASK_TEMPLATE
        response_message = INVALID_GOFS_OF_TASK_TEMPLATE[0].format(
            str(err.gof_ids), err.task_template_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_GOFS_OF_TASK_TEMPLATE[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_duplicate_field_ids_to_a_gof_exception(
            self, err: DuplicateFieldIdsToGoF):
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF
        response_message = DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF[0].format(
            err.gof_id, str(err.field_ids))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_fields_given_to_a_gof_exception(
            self, err: InvalidFieldsOfGoF):
        from ib_tasks.constants.exception_messages import \
            INVALID_FIELDS_OF_GOF
        response_message = INVALID_FIELDS_OF_GOF[0].format(
            str(err.field_ids), err.gof_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_FIELDS_OF_GOF[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_stage_permitted_gofs_exception(
            self, err: InvalidStagePermittedGoFs):
        from ib_tasks.constants.exception_messages import \
            INVALID_STAGE_PERMITTED_GOFS
        response_message = INVALID_STAGE_PERMITTED_GOFS[0].format(
            str(err.gof_ids), err.stage_id)
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INVALID_STAGE_PERMITTED_GOFS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_user_needs_gof_writable_permission_exception(
            self, err: UserNeedsGoFWritablePermission):
        from ib_tasks.constants.exception_messages import \
            USER_NEEDS_GOF_WRITABLE_PERMISSION
        response_message = USER_NEEDS_GOF_WRITABLE_PERMISSION[0].format(
            err.gof_id, str(err.required_roles))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": USER_NEEDS_GOF_WRITABLE_PERMISSION[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_user_needs_field_writable_permission_exception(
            self, err: UserNeedsFieldWritablePermission):
        from ib_tasks.constants.exception_messages import \
            USER_NEEDS_FILED_WRITABLE_PERMISSION
        response_message = USER_NEEDS_FILED_WRITABLE_PERMISSION[0].format(
            err.field_id, str(err.required_roles))
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": USER_NEEDS_FILED_WRITABLE_PERMISSION[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_empty_value_in_required_field_exception(
            self, err: EmptyValueForRequiredField):
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

    def raise_invalid_phone_number_value_exception(
            self, err: InvalidPhoneNumberValue):
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

    def raise_invalid_email_address_exception(
            self, err: InvalidEmailFieldValue):
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

    def raise_invalid_url_address_exception(self, err: InvalidURLValue):
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

    def raise_weak_password_exception(self, err: NotAStrongPassword):
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

    def raise_invalid_number_value_exception(self, err: InvalidNumberValue):
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

    def raise_invalid_float_value_exception(self, err: InvalidFloatValue):
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

    def raise_invalid_dropdown_value_exception(
            self, err: InvalidValueForDropdownField):
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

    def raise_invalid_name_in_gof_selector_exception(
            self, err: IncorrectNameInGoFSelectorField):
        from ib_tasks.constants.exception_messages import \
            INCORRECT_NAME_IN_GOF_SELECTOR_FIELD
        response_message = INCORRECT_NAME_IN_GOF_SELECTOR_FIELD[0].format(
            err.field_value, err.field_id, err.valid_gof_selector_names
        )
        data = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": INCORRECT_NAME_IN_GOF_SELECTOR_FIELD[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_choice_in_radio_group_field_exception(
            self, err: IncorrectRadioGroupChoice):
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

    def raise_invalid_checkbox_group_options_exception(
            self, err: IncorrectCheckBoxOptionsSelected):
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

    def raise_invalid_multi_select_options_selected_exception(
            self, err: IncorrectMultiSelectOptionsSelected):
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

    def raise_invalid_multi_select_labels_selected_exception(
            self, err: IncorrectMultiSelectLabelsSelected):
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

    def raise_invalid_date_format_exception(self, err: InvalidDateFormat):
        from ib_tasks.constants.exception_messages import \
            INVALID_DATE_FORMAT
        message = INVALID_DATE_FORMAT[0].format(err.field_value, err.field_id,
                                                err.expected_format)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": INVALID_DATE_FORMAT[1]
        }
        return self.prepare_400_bad_request_response(data)

    def raise_invalid_time_format_exception(self, err: InvalidTimeFormat):
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

    def raise_invalid_image_url_exception(self, err: InvalidUrlForImage):
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

    def raise_not_acceptable_image_format_exception(
            self, err: InvalidImageFormat):
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

    def raise_invalid_file_url_exception(self, err: InvalidUrlForFile):
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

    def raise_not_acceptable_file_format_exception(self,
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
