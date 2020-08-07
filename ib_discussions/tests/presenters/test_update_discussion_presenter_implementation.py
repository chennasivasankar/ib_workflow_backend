import json

import pytest

from ib_discussions.constants.enum import StatusCode


class TestUpdateDiscussionPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_discussions.presenters.update_discussion_presenter_implementation import \
            UpdateDiscussionPresenterImplementation
        presenter = UpdateDiscussionPresenterImplementation()
        return presenter

    def test_response_for_empty_title(self, presenter):
        # Arrange
        from ib_discussions.presenters.update_discussion_presenter_implementation import \
            EMPTY_TITLE
        expected_response = EMPTY_TITLE[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = EMPTY_TITLE[1]

        # Act
        response_obj = presenter.response_for_empty_title()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_discussion_id_not_found(self, presenter):
        # Arrange
        from ib_discussions.presenters.update_discussion_presenter_implementation import \
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

    def test_response_for_user_cannot_update_discussion(self, presenter):
        # Arrange
        from ib_discussions.presenters.update_discussion_presenter_implementation import \
            USER_CANNOT_UPDATE_DISCUSSION
        expected_response = USER_CANNOT_UPDATE_DISCUSSION[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = USER_CANNOT_UPDATE_DISCUSSION[1]

        # Act
        response_obj = presenter.response_for_user_cannot_update_discussion()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_prepare_success_response_for_update_discussion(self, presenter):
        # Act
        response_obj \
            = presenter.prepare_success_response_for_update_discussion()

        # Assert
        assert response_obj.status_code == StatusCode.CREATED.value
