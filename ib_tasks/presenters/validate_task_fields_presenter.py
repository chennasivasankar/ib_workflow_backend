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
