import json

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
        print(response_dict)
