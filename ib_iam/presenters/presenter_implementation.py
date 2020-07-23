from django_swagger_utils.utils.http_response_mixin \
    import HTTPResponseMixin
from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.presenter_interface \
    import PresenterInterface


class PresenterImplementation(PresenterInterface, HTTPResponseMixin):

    def raise_role_name_should_not_be_empty_exception(self):
        from ib_iam.constants.exception_messages \
            import ROLE_NAME_SHOULD_NOT_BE_EMPTY
        response_dict = {
            "response": ROLE_NAME_SHOULD_NOT_BE_EMPTY[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": ROLE_NAME_SHOULD_NOT_BE_EMPTY[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_role_description_should_not_be_empty_exception(self):
        from ib_iam.constants.exception_messages \
            import ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY
        response_dict = {
            "response": ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_role_id_format_is_invalid_exception(self):
        from ib_iam.constants.exception_messages \
            import ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT
        response_dict = {
            "response": ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_duplicate_role_ids_exception(self):
        from ib_iam.constants.exception_messages \
            import DUPLICATE_ROLE_IDS
        response_dict = {
            "response": DUPLICATE_ROLE_IDS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_ROLE_IDS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_user_is_not_admin_exception(self):
        from ib_iam.constants.exception_messages import \
            USER_DOES_NOT_HAVE_PERMISSION
        response_dict = {
            "response": USER_DOES_NOT_HAVE_PERMISSION[0],
            "http_status_code": StatusCode.FORBIDDEN.value,
            "res_status": USER_DOES_NOT_HAVE_PERMISSION[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict)

    def edit_user_edited_successfully(self):
        from ib_iam.constants.exception_messages import EDIT_USER_SUCCESSFULLY
        response_dict = {
            "response": EDIT_USER_SUCCESSFULLY[0],
            "http_status_code": StatusCode.SUCCESS.value,
            "res_status": EDIT_USER_SUCCESSFULLY[1]

        }
        return self.prepare_200_success_response(
            response_dict=response_dict)

    def raise_user_does_not_exist(self):
        from ib_iam.constants.exception_messages \
            import USER_DOES_NOT_EXIST
        response_dict = {
            "response": USER_DOES_NOT_EXIST[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": USER_DOES_NOT_EXIST[1]
        }
        response = self.prepare_404_not_found_response(
            response_dict=response_dict)
        return response
