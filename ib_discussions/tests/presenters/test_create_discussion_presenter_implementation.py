import json

import pytest

from ib_discussions.constants.enum import StatusCode


class TestCreateDiscussionPresenterImplementation:
    @pytest.fixture()
    def presenter(self):
        from ib_discussions.presenters.create_discussion_presenter_implementation import \
            CreateDiscussionPresenterImplementation
        presenter = CreateDiscussionPresenterImplementation()
        return presenter

    def test_prepare_success_response_for_create_discussion(self, presenter):
        # Act
        response_obj \
            = presenter.prepare_success_response_for_create_discussion()

        # Assert
        assert response_obj.status_code == StatusCode.CREATED.value

    def test_response_for_empty_title(self, presenter):
        # Arrange
        from ib_discussions.presenters.create_discussion_presenter_implementation import \
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
