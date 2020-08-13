import json

import pytest

from ib_discussions.constants.enum import StatusCode


class TestCreateCommentPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_discussions.presenters.create_reply_presenter_implementation import \
            CreateReplyPresenterImplementation
        presenter = CreateReplyPresenterImplementation()
        return presenter

    def test_response_for_comment_id_not_found(self, presenter):
        # Arrange
        from ib_discussions.presenters.create_reply_presenter_implementation import \
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

    def test_response_for_invalid_user_ids(self, presenter):
        # Arrange
        invalid_user_ids = [
            "f26c1802-d996-4e89-9644-23ebaf02713a",
            "a5f52868-8065-403c-abe5-24c09e42bafe"
        ]
        from ib_discussions.presenters.create_comment_presenter_implementation import \
            INVALID_USER_IDS
        expected_response = INVALID_USER_IDS[0].format(
            user_ids=invalid_user_ids)
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_USER_IDS[1]

        from ib_discussions.adapters.auth_service import InvalidUserIds
        error_object = InvalidUserIds(user_ids=invalid_user_ids)

        # Act
        response_obj = presenter.response_for_invalid_user_ids(err=error_object)

        # Assert
        response_data = json.loads(response_obj.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_prepare_response_for_reply(self, presenter, snapshot):
        # Arrange
        comment_id = '91be920b-7b4c-49e7-8adb-41a0c18da848'
        user_ids = [
            '01be920b-7b4c-49e7-8adb-41a0c18da848',
            '91be920b-7b4c-49e7-8adb-41a0c18da848',
            '31be920b-7b4c-49e7-8adb-41a0c18da848'
        ]

        from ib_discussions.tests.factories.storage_dtos import \
            CommentDTOFactory
        comment_dto = CommentDTOFactory(
            comment_id=comment_id,
            comment_content='content',
            user_id='31be920b-7b4c-49e7-8adb-41a0c18da848',
        )

        from ib_discussions.tests.factories.presenter_dtos import \
            CommentIdWithEditableStatusDTOFactory
        comment_with_editable_status_dto = CommentIdWithEditableStatusDTOFactory(
            comment_id=comment_id, is_editable=True
        )

        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_profile_dtos = [
            UserProfileDTOFactory(
                user_id=user_id,
                name='name ',
                profile_pic_url='https://graph.ib_users.com/'
            )
            for user_id in user_ids
        ]

        multimedia_ids = [
            "f26c1802-d996-4e89-9644-23ebaf02713a",
            "a5f52868-8065-403c-abe5-24c09e42bafe"
        ]

        from ib_discussions.tests.factories.storage_dtos import \
            CommentIdWithMultiMediaDTOFactory
        CommentIdWithMultiMediaDTOFactory.format_type.reset()
        comment_id_with_multimedia_dtos = [
            CommentIdWithMultiMediaDTOFactory(
                multimedia_id=multimedia_id,
                comment_id=comment_id)
            for multimedia_id in multimedia_ids
        ]

        from ib_discussions.tests.factories.storage_dtos import \
            CommentIdWithMentionUserIdDTOFactory
        comment_id_with_mention_user_id_dtos = [
            CommentIdWithMentionUserIdDTOFactory(
                comment_id=comment_id, mention_user_id=user_ids[0]),
            CommentIdWithMentionUserIdDTOFactory(
                comment_id=comment_id, mention_user_id=user_ids[1])
        ]

        # Act
        response_object = presenter.prepare_response_for_reply(
            comment_dto=comment_dto, user_profile_dtos=user_profile_dtos,
            comment_with_editable_status_dto=comment_with_editable_status_dto,
            comment_id_with_mention_user_id_dtos=comment_id_with_mention_user_id_dtos,
            comment_id_with_multimedia_dtos=comment_id_with_multimedia_dtos
        )

        # Assert
        response_dict = json.loads(response_object.content)

        snapshot.assert_match(response_dict, "create_reply")
