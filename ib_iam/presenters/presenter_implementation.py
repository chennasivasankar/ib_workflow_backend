from django.http import response

from ib_iam.interactors.presenter_interfaces.presenter_interface \
    import PresenterInterface

class PresenterImplementation(PresenterInterface):

    def raise_role_id_should_not_be_empty(self):
        from ib_iam.constants.exception_messages \
            import ROLE_ID_SHOULD_NOT_BE_EMPTY
        import json
        data = json.dumps({
            "response": ROLE_ID_SHOULD_NOT_BE_EMPTY[0],
            "http_status_code": 400,
            "res_status": ROLE_ID_SHOULD_NOT_BE_EMPTY[1]
        })
        return response.HttpResponse(data, status=400)

    def raise_role_name_should_not_be_empty(self):
        from ib_iam.constants.exception_messages \
            import ROLE_NAME_SHOULD_NOT_BE_EMPTY
        import json
        data = json.dumps({
            "response": ROLE_NAME_SHOULD_NOT_BE_EMPTY[0],
            "http_status_code": 400,
            "res_status": ROLE_NAME_SHOULD_NOT_BE_EMPTY[1]
        })
        return response.HttpResponse(data, status=400)

    def raise_role_description_should_not_be_empty(self):
        from ib_iam.constants.exception_messages \
            import ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY
        import json
        data = json.dumps({
            "response": ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY[0],
            "http_status_code": 400,
            "res_status": ROLE_DESCRIPTION_SHOULD_NOT_BE_EMPTY[1]
        })
        return response.HttpResponse(data, status=400)

    def raise_role_id_format_is_invalid(self):
        from ib_iam.constants.exception_messages \
            import ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT
        import json
        data = json.dumps({
            "response": ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT[0],
            "http_status_code": 400,
            "res_status": ROLE_ID_SHOULD_NOT_BE_IN_VALID_FORMAT[1]
        })
        return response.HttpResponse(data, status=400)

    def raise_invalid_role_id_execption(self):
        from ib_iam.constants.exception_messages \
            import ROLE_ID_SHOULD_BE_STRING
        import json
        data = json.dumps({
            "response": ROLE_ID_SHOULD_BE_STRING[0],
            "http_status_code": 400,
            "res_status": ROLE_ID_SHOULD_BE_STRING[1]
        })
        return response.HttpResponse(data, status=400)

    def raise_duplicate_role_ids_exception(self):
        from ib_iam.constants.exception_messages \
            import DUPLICATE_ROLE_IDS
        import json
        data = json.dumps({
            "response": DUPLICATE_ROLE_IDS[0],
            "http_status_code": 400,
            "res_status": DUPLICATE_ROLE_IDS[1]
        })
        return response.HttpResponse(data, status=400)