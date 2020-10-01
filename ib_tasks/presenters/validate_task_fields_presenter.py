from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields
from ib_tasks.interactors.presenter_interfaces.validate_task_fields_presenter import \
    ValidateTaskFieldsPresenterInterface


class ValidateTaskFieldsPresenterImplementation(
    ValidateTaskFieldsPresenterInterface, HTTPResponseMixin
):
    def raise_user_did_not_fill_required_fields(
            self, err: UserDidNotFillRequiredFields):
        from ib_tasks.constants.exception_messages import \
            USER_DID_NOT_FILL_REQUIRED_FIELDS
        field_display_names = [
            dto.field_display_name for dto in err.unfilled_field_dtos]
        message = USER_DID_NOT_FILL_REQUIRED_FIELDS[0].format(
            field_display_names)
        data = {
            "response": message,
            "http_status_code": 400,
            "res_status": USER_DID_NOT_FILL_REQUIRED_FIELDS[1]
        }
        return self.prepare_400_bad_request_response(data)

    def start_date_is_required(self):
        from ib_tasks.constants.exception_messages import \
            START_DATE_TIME_IS_REQUIRED
        response_message = START_DATE_TIME_IS_REQUIRED[0]
        response_dict = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": START_DATE_TIME_IS_REQUIRED[1]
        }

        response_object = self.prepare_400_bad_request_response(response_dict)
        return response_object

    def due_date_is_required(self):
        from ib_tasks.constants.exception_messages import \
            DUE_DATE_TIME_IS_REQUIRED
        response_message = DUE_DATE_TIME_IS_REQUIRED[0]
        response_dict = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": DUE_DATE_TIME_IS_REQUIRED[1]
        }

        response_object = self.prepare_400_bad_request_response(response_dict)
        return response_object

    def priority_is_required(self):
        from ib_tasks.constants.exception_messages import PRIORITY_IS_REQUIRED
        response_message = PRIORITY_IS_REQUIRED[0]
        response_dict = {
            "response": response_message,
            "http_status_code": 400,
            "res_status": PRIORITY_IS_REQUIRED[1]
        }

        response_object = self.prepare_400_bad_request_response(response_dict)
        return response_object
