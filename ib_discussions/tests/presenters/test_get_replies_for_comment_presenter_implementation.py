import json

import pytest

from ib_discussions.constants.enum import StatusCode


class TestGetRepliesForCommentPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_discussions.presenters.get_replies_for_comment_presenter_implementation import \
            GetRepliesForCommentPresenterImplementation
        presenter = GetRepliesForCommentPresenterImplementation()
        return presenter

    def test_response_for_comment_id_not_found(self, presenter):
        # Arrange
        from ib_discussions.presenters.get_replies_for_comment_presenter_implementation import \
            COMMENT_ID_NOT_FOUND
        expected_response = COMMENT_ID_NOT_FOUND[0]
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = COMMENT_ID_NOT_FOUND[1]

        # Act
        response_obj = presenter.response_for_comment_id_not_found()

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_prepare_response_for_reply(self, presenter, snapshot):
        # Arrange
        user_ids = [
            '31be920b-7b4c-49e7-8adb-41a0c18da848',
            '41be920b-7b4c-49e7-8adb-41a0c18da848'
        ]
        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_profile_dtos = [
            UserProfileDTOFactory(user_id=user_id)
            for user_id in user_ids
        ]

        comment_ids = [
            '91be920b-7b4c-49e7-8adb-41a0c18da848',
            '00be920b-7b4c-49e7-8adb-41a0c18da848',
        ]
        from ib_discussions.tests.factories.storage_dtos import \
            CommentDTOFactory
        comment_dtos = [
            CommentDTOFactory(
                comment_id=comment_id,
                user_id=user_id,
            )
            for comment_id, user_id in zip(comment_ids, user_ids)
        ]

        from ib_discussions.tests.factories.presenter_dtos import \
            CommentIdWithEditableStatusDTOFactory
        CommentIdWithEditableStatusDTOFactory.is_editable.reset()
        comment_with_editable_status_dtos = [
            CommentIdWithEditableStatusDTOFactory(comment_id=comment_id)
            for comment_id in comment_ids
        ]

        # Act
        response_object = presenter.prepare_response_for_replies_with_users_dtos(
            comment_dtos=comment_dtos, user_profile_dtos=user_profile_dtos,
            comment_with_editable_status_dtos=comment_with_editable_status_dtos
        )

        # Assert
        response_dict = json.loads(response_object.content)

        snapshot.assert_match(response_dict, "get replies")
