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

    def raise_invalid_name_length_exception_for_update_user_profile(self):
        from ib_iam.constants.exception_messages import \
            INVALID_NAME_LENGTH
        from ib_iam.constants.enums import StatusCode
        from ib_iam.constants.config import MINIMUM_USER_NAME_LENGTH
        response_dict = {
            "response": INVALID_NAME_LENGTH[0].format(
                minimum_name_length=MINIMUM_USER_NAME_LENGTH
            ),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_NAME_LENGTH[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_name_should_not_contain_special_chars_and_numbers_exception_for_update_user_profile(
            self):
        from ib_iam.constants.exception_messages import \
            NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS
        response_dict = {
            "response":
                NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status":
                NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_invalid_email_exception_for_update_user_profile(self):
        from ib_iam.constants.exception_messages import INVALID_EMAIL
        response_dict = {"response": INVALID_EMAIL[0],
                         "http_status_code": StatusCode.BAD_REQUEST.value,
                         "res_status": INVALID_EMAIL[1]}
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_email_already_in_use_exception_for_update_user_profile(self):
        from ib_iam.constants.exception_messages import EMAIL_ALREADY_IN_USE
        response_dict = {"response": EMAIL_ALREADY_IN_USE[0],
                         "http_status_code": StatusCode.BAD_REQUEST.value,
                         "res_status": EMAIL_ALREADY_IN_USE[1]}
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_invalid_role_ids_exception(self):
        from ib_iam.constants.exception_messages import INVALID_ROLE_IDS
        response_dict = {
            "response": INVALID_ROLE_IDS[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_ROLE_IDS[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_duplicate_role_ids_exception(self):
        from ib_iam.constants.exception_messages import \
            DUPLICATE_ROLE_IDS_FOR_UPDATE_USER_PROFILE
        response_dict = {
            "response": DUPLICATE_ROLE_IDS_FOR_UPDATE_USER_PROFILE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_ROLE_IDS_FOR_UPDATE_USER_PROFILE[1]}
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
