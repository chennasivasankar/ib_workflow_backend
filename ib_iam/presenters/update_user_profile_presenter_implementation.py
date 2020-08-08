from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces \
    .update_user_profile_presenter_interface import \
    UpdateUserProfilePresenterInterface


class UpdateUserProfilePresenterImplementation(
    UpdateUserProfilePresenterInterface, HTTPResponseMixin):

    def get_success_response_for_update_user_profile(self):
        empty_dict = {}
        return self.prepare_200_success_response(response_dict=empty_dict)

    def get_response_for_empty_name_exception(self):
        from ib_iam.constants.exception_messages import EMPTY_NAME_IS_INVALID
        response_dict = {
            "response": EMPTY_NAME_IS_INVALID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": EMPTY_NAME_IS_INVALID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def get_response_for_minimum_name_length(self):
        from ib_iam.constants.exception_messages import \
            NAME_MINIMUM_LENGTH_SHOULD_BE_FIVE_OR_MORE
        response_dict = {
            "response": NAME_MINIMUM_LENGTH_SHOULD_BE_FIVE_OR_MORE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": NAME_MINIMUM_LENGTH_SHOULD_BE_FIVE_OR_MORE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def get_response_for_name_contains_special_chars_and_numbers_exception(
            self):
        from ib_iam.constants.exception_messages import \
            NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS
        response_dict = {
            "response":
                NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status":
                NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
