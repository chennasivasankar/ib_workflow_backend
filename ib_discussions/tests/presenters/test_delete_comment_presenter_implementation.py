import json

import pytest

from ib_discussions.constants.enum import StatusCode


class TestUpdateCommentPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_discussions.presenters.delete_comment_presenter_implementation \
            import DeleteCommentPresenterImplementation
        presenter = DeleteCommentPresenterImplementation()
        return presenter

    def test_response_for_comment_id_not_found(self, presenter):
        # Arrange
        from ib_discussions.presenters.delete_comment_presenter_implementation \
            import COMMENT_ID_NOT_FOUND
        expected_response = COMMENT_ID_NOT_FOUND[0]
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = COMMENT_ID_NOT_FOUND[1]

        # Act
        response_obj = presenter.prepare_response_for_comment_id_not_found()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_user_cannot_edit_comment(self, presenter):
        # Arrange
        from ib_discussions.presenters.delete_comment_presenter_implementation \
            import USER_CANNOT_EDIT_COMMENT
        expected_response = USER_CANNOT_EDIT_COMMENT[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = USER_CANNOT_EDIT_COMMENT[1]

        # Act
        response_obj = presenter.response_for_user_cannot_edit_comment()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_prepare_response_for_delete_comment(self, presenter):
        # Act
        response_obj \
            = presenter.prepare_response_for_delete_comment()

        # Assert
        assert response_obj.status_code == StatusCode.SUCCESS.value
