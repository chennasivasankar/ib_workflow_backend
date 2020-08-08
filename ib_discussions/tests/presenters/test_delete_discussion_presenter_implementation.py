import json

import pytest

from ib_discussions.constants.enum import StatusCode


class TestDeleteDiscussionPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_discussions.presenters.delete_discussion_presenter_implementation import \
            DeleteDiscussionPresenterImplementation
        presenter = DeleteDiscussionPresenterImplementation()
        return presenter

    def test_response_for_discussion_id_not_found(self, presenter):
        # Arrange
        from ib_discussions.presenters.delete_discussion_presenter_implementation import \
            DISCUSSION_ID_NOT_FOUND
        expected_response = DISCUSSION_ID_NOT_FOUND[0]
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = DISCUSSION_ID_NOT_FOUND[1]

        # Act
        response_obj = presenter.response_for_discussion_id_not_found()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_user_cannot_delete_discussion(self, presenter):
        # Arrange
        from ib_discussions.presenters.delete_discussion_presenter_implementation import \
            USER_CANNOT_DELETE_DISCUSSION
        expected_response = USER_CANNOT_DELETE_DISCUSSION[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = USER_CANNOT_DELETE_DISCUSSION[1]

        # Act
        response_obj = presenter.response_for_user_cannot_delete_discussion()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_prepare_success_response_for_delete_discussion(self, presenter):
        # Act
        response_obj \
            = presenter.prepare_success_response_for_delete_discussion()

        # Assert
        assert response_obj.status_code == StatusCode.CREATED.value
