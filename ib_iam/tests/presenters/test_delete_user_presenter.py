import json

from ib_iam.constants.enums import StatusCode
from ib_iam.presenters.delete_user_presenter_implementation import \
    DeleteUserPresenterImplementation


class TestDeleteUserPresenter:
    def test_get_delete_user_response_return_http_response_with_200_status_code(
            self):
        presenter = DeleteUserPresenterImplementation()

        from django.http import HttpResponse
        expected_response = HttpResponse(status=200, content={})

        actual_response = presenter.get_delete_user_response()

        response_dict = json.loads(actual_response.content)
        assert expected_response.status_code == StatusCode.SUCCESS.value
        assert response_dict == {}

    def test_raise_user_is_not_admin_exception(self):
        presenter = DeleteUserPresenterImplementation()
        from ib_iam.constants.exception_messages import \
            USER_DOES_NOT_HAVE_PERMISSION
        expected_response = USER_DOES_NOT_HAVE_PERMISSION[0]
        response_status_code = USER_DOES_NOT_HAVE_PERMISSION[1]

        actual_response = presenter.response_for_user_is_not_admin_exception()

        response_dict = json.loads(actual_response.content)
        assert response_dict['http_status_code'] == StatusCode.FORBIDDEN.value
        assert response_dict['res_status'] == response_status_code
        assert response_dict['response'] == expected_response

    def test_raise_user_is_not_found_exception(self):
        presenter = DeleteUserPresenterImplementation()
        from ib_iam.constants.exception_messages import \
            USER_DOES_NOT_EXIST
        expected_response = USER_DOES_NOT_EXIST[0]
        response_status_code = USER_DOES_NOT_EXIST[1]

        actual_response = presenter.raise_user_is_not_found_exception()

        response_dict = json.loads(actual_response.content)
        assert response_dict['http_status_code'] == StatusCode.NOT_FOUND.value
        assert response_dict['res_status'] == response_status_code
        assert response_dict['response'] == expected_response

    def test_raise_user_does_not_have_delete_permission_exception(self):
        presenter = DeleteUserPresenterImplementation()
        from ib_iam.constants.exception_messages import \
            USER_DOES_NOT_HAVE_DELETE_PERMISSION
        expected_response = USER_DOES_NOT_HAVE_DELETE_PERMISSION[0]
        response_status_code = USER_DOES_NOT_HAVE_DELETE_PERMISSION[1]

        actual_response = presenter.raise_user_does_not_have_delete_permission_exception()

        response_dict = json.loads(actual_response.content)
        assert response_dict['http_status_code'] == StatusCode.FORBIDDEN.value
        assert response_dict['res_status'] == response_status_code
        assert response_dict['response'] == expected_response
