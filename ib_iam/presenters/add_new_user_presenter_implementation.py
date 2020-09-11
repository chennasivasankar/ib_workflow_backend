from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.add_new_user_presenter_inerface \
    import AddUserPresenterInterface


class AddUserPresenterImplementation(
    AddUserPresenterInterface, HTTPResponseMixin
):
    def response_for_user_is_not_admin_exception(self):
        from ib_iam.constants.exception_messages import \
            USER_DOES_NOT_HAVE_PERMISSION
        response_dict = {
            "response": USER_DOES_NOT_HAVE_PERMISSION[0],
            "http_status_code": StatusCode.FORBIDDEN.value,
            "res_status": USER_DOES_NOT_HAVE_PERMISSION[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )

    def response_for_invalid_email_exception(self):
        from ib_iam.constants.exception_messages import INVALID_EMAIL
        response_dict = {
            "response": INVALID_EMAIL[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_EMAIL[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_user_account_already_exists_exception(self):
        from ib_iam.constants.exception_messages \
            import USER_ALREADY_EXIST_WITH_THIS_EMAIL
        response_dict = {
            "response": USER_ALREADY_EXIST_WITH_THIS_EMAIL[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": USER_ALREADY_EXIST_WITH_THIS_EMAIL[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_invalid_name_length_exception(self):
        from ib_iam.constants.exception_messages \
            import INVALID_NAME_LENGTH
        from ib_iam.constants.config import MINIMUM_USER_NAME_LENGTH
        response = INVALID_NAME_LENGTH[0].format(
            minimum_name_length=MINIMUM_USER_NAME_LENGTH
        )
        res_status = INVALID_NAME_LENGTH[1]
        response_dict = {
            "response": response,
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": res_status
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_name_contains_special_character_exception(self):
        from ib_iam.constants.exception_messages \
            import NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS
        response = NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS[0]
        res_status = NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS[1]
        response_dict = {
            "response": response,
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": res_status

        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def response_for_invalid_role_ids_exception(self):
        from ib_iam.constants.exception_messages import INVALID_ROLE_IDS
        response_dict = {
            "response": INVALID_ROLE_IDS[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_ROLE_IDS[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def response_for_invalid_company_ids_exception(self):
        from ib_iam.constants.exception_messages import INVALID_COMPANY_ID
        response_dict = {
            "response": INVALID_COMPANY_ID[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_COMPANY_ID[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def response_for_invalid_team_ids_exception(self):
        from ib_iam.constants.exception_messages import INVALID_TEAM_IDS
        response_dict = {
            "response": INVALID_TEAM_IDS[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_TEAM_IDS[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def response_for_add_user_response(self):
        from ib_iam.constants.exception_messages import \
            CREATE_USER_SUCCESSFULLY
        response_dict = {
            "response": CREATE_USER_SUCCESSFULLY[0],
            "http_status_code": StatusCode.SUCCESS_CREATE.value,
            "res_status": CREATE_USER_SUCCESSFULLY[1]

        }
        return self.prepare_201_created_response(
            response_dict=response_dict
        )
