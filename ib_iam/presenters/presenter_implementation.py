from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces.presenter_interface \
    import PresenterInterface


class PresenterImplementation(PresenterInterface, HTTPResponseMixin):

    def raise_role_name_should_not_be_empty_exception(self):
        from ib_iam.constants.exception_messages \
            import ROLE_NAME_SHOULD_NOT_BE_EMPTY
        from ib_iam.constants.enums import StatusCode
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
        from ib_iam.constants.enums import StatusCode
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
        from ib_iam.constants.enums import StatusCode
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
        from ib_iam.constants.enums import StatusCode
        response_dict = {
            "response": DUPLICATE_ROLE_IDS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_ROLE_IDS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
