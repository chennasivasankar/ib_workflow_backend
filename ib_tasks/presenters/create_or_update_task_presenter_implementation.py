from ib_tasks.exceptions.field_values_custom_exceptions import \
    EmptyValueForPlainTextField, InvalidGoFIDsInGoFSelectorField, \
    InvalidUrlForFile, InvalidUrlForImage, InvalidImageFormat, NotAnImageUrl, \
    CouldNotReadImage, InvalidTimeFormat, InvalidDateFormat, \
    IncorrectMultiSelectLabelsSelected, IncorrectMultiSelectOptionsSelected, \
    IncorrectCheckBoxOptionsSelected, IncorrectRadioGroupChoice, \
    IncorrectGoFIDInGoFSelectorField, InvalidValueForDropdownField, \
    InvalidFloatValue, InvalidNumberValue, NotAStrongPassword, InvalidURLValue, \
    InvalidEmailFieldValue, InvalidPhoneNumberValue, InvalidFileFormat, \
    EmptyValueForRequiredField
from ib_tasks.exceptions.fields_custom_exceptions import \
    DuplicationOfFieldIdsExist, InvalidFieldIds
from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateIds
from ib_tasks.interactors.presenter_interfaces.create_or_update_task_presenter \
    import CreateOrUpdateTaskPresenterInterface
from django.http import response
import json


class CreateOrUpdateTaskPresenterImplementation(
    CreateOrUpdateTaskPresenterInterface
):
    def raise_exception_for_could_not_read_image(self, err: CouldNotReadImage):
        pass

    def raise_exception_for_empty_value_in_required_field(self,
                                                          err: EmptyValueForRequiredField):
        pass

    def raise_exception_for_not_acceptable_file_format(self,
                                                       err: InvalidFileFormat):
        pass

    def raise_exception_for_invalid_phone_number_value(self,
                                                       err: InvalidPhoneNumberValue):
        pass

    def raise_exception_for_invalid_email_address(self,
                                                  err: InvalidEmailFieldValue):
        pass

    def raise_exception_for_invalid_url_address(self, err: InvalidURLValue):
        pass

    def raise_exception_for_weak_password(self, err: NotAStrongPassword):
        pass

    def raise_exception_for_invalid_number_value(self,
                                                 err: InvalidNumberValue):
        pass

    def raise_exception_for_invalid_float_value(self, err: InvalidFloatValue):
        pass

    def raise_exception_for_invalid_dropdown_value(self,
                                                   err: InvalidValueForDropdownField):
        pass

    def raise_exceptions_for_invalid_gof_id_selected_in_gof_selector(self,
                                                                     err: IncorrectGoFIDInGoFSelectorField):
        pass

    def raise_exception_for_invalid_choice_in_radio_group_field(self,
                                                                err: IncorrectRadioGroupChoice):
        pass

    def raise_exception_for_invalid_checkbox_group_options_selected(self,
                                                                    err: IncorrectCheckBoxOptionsSelected):
        pass

    def raise_exception_for_invalid_multi_select_options_selected(self,
                                                                  err: IncorrectMultiSelectOptionsSelected):
        pass

    def raise_exception_for_invalid_multi_select_labels_selected(self,
                                                                 err: IncorrectMultiSelectLabelsSelected):
        pass

    def raise_exception_for_invalid_date_format(self, err: InvalidDateFormat):
        pass

    def raise_exception_for_invalid_time_format(self, err: InvalidTimeFormat):
        pass

    def raise_exception_for_not_an_image_url(self, err: NotAnImageUrl):
        pass

    def raise_exception_for_not_acceptable_image_format(self,
                                                        err: InvalidImageFormat):
        pass

    def raise_exception_for_invalid_image_url(self, err: InvalidUrlForImage):
        pass

    def raise_exception_for_invalid_folder_url(self, err: InvalidUrlForFile):
        pass

    def raise_exception_for_gof_ids_in_gof_selector_field_value(self,
                                                                err: InvalidGoFIDsInGoFSelectorField):
        pass

    def raise_exception_for_duplicate_field_ids(self, err: DuplicationOfFieldIdsExist):
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_FIELD_IDS
        response_message = DUPLICATE_FIELD_IDS[0].format(
            str(err.field_ids)
        )
        data = json.dumps(
            {
                "response": response_message,
                "http_status_code": 400,
                "res_status": DUPLICATE_FIELD_IDS[1]
            }
        )
        response_object = response.HttpResponse(data)
        return response_object

    def raise_exception_for_invalid_task_template_id(
            self, err: InvalidTaskTemplateIds
    ):
        from ib_tasks.constants.exception_messages import \
            INVALID_TASK_TEMPLATE_IDS
        response_message = INVALID_TASK_TEMPLATE_IDS[0].format(
            str(err.invalid_task_template_ids)
        )
        data = json.dumps(
            {
                "response": response_message,
                "http_status_code": 400,
                "res_status": INVALID_TASK_TEMPLATE_IDS[1]
            }
        )
        response_object = response.HttpResponse(data)
        return response_object

    def raise_exception_for_invalid_gof_ids(self, err: InvalidGoFIds):
        from ib_tasks.constants.exception_messages import \
            INVALID_GOF_IDS
        response_message = INVALID_GOF_IDS[0].format(str(err.gof_ids))
        data = json.dumps(
            {
                "response": response_message,
                "http_status_code": 400,
                "res_status": INVALID_GOF_IDS[1]
            }
        )
        response_object = response.HttpResponse(data)
        return response_object

    def raise_exception_for_invalid_field_ids(self, err: InvalidFieldIds):
        from ib_tasks.constants.exception_messages import \
            INVALID_FIELD_IDS
        response_message = INVALID_FIELD_IDS[0].format(str(err.field_ids))
        data = json.dumps(
            {
                "response": response_message,
                "http_status_code": 400,
                "res_status": INVALID_FIELD_IDS[1]
            }
        )
        response_object = response.HttpResponse(data)
        return response_object

    def get_response_for_create_or_update_task(self):
        pass

    def raise_exception_for_empty_value_in_plain_text_field(
            self, err: EmptyValueForPlainTextField
    ):
        from ib_tasks.constants.exception_messages import \
            EMPTY_VALUE_FOR_PLAIN_TEXT_FIELD
        response_message = EMPTY_VALUE_FOR_PLAIN_TEXT_FIELD[0].format(
            str(err.field_id)
        )
        data = json.dumps(
            {
                "response": response_message,
                "http_status_code": 400,
                "res_status": EMPTY_VALUE_FOR_PLAIN_TEXT_FIELD[1]
            }
        )
        response_object = response.HttpResponse(data)
        return response_object
