import json

import pytest

from ib_discussions.constants.enum import StatusCode


class TestMarkDiscussionClarifiedPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_discussions.presenters.mark_discussion_clarified_presenter_implementation import \
            MarkDiscussionClarifiedPresenterImplementation
        presenter = MarkDiscussionClarifiedPresenterImplementation()
        return presenter

    def test_raise_exception_for_discussion_id_not_found(self, presenter):
        # Arrange
        from ib_discussions.presenters.mark_discussion_clarified_presenter_implementation import \
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

    def test_raise_exception_for_user_cannot_mark_as_clarified(self,
                                                               presenter):
        # Arrange
        from ib_discussions.presenters.mark_discussion_clarified_presenter_implementation import \
            USER_CANNOT_MARK_AS_CLARIFIED
        expected_response = USER_CANNOT_MARK_AS_CLARIFIED[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = USER_CANNOT_MARK_AS_CLARIFIED[1]

        # Act
        response_obj \
            = presenter.response_for_user_cannot_mark_as_clarified()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_raise_success_response_for_mark_discussion_as_clarified(self,
                                                                     presenter):
        # Act
        response_obj \
            = presenter.prepare_success_response_for_mark_discussion_as_clarified()

        # Assert
        assert response_obj.status_code == StatusCode.CREATED.value
