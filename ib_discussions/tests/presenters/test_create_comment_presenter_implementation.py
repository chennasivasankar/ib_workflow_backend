import json

import pytest

from ib_discussions.constants.enum import StatusCode


class TestCreateCommentPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_discussions.presenters.create_comment_presenter_implementation import \
            CreateCommentPresenterImplementation
        presenter = CreateCommentPresenterImplementation()
        return presenter

    def test_response_for_discussion_id_not_found(self, presenter):
        # Arrange
        from ib_discussions.presenters.create_comment_presenter_implementation import \
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

    def test_prepare_response_for_create_comment(self, presenter, snapshot):
        from ib_discussions.tests.factories.presenter_dtos import \
            CommentWithRepliesCountAndEditableDTOFactory
        comment_with_replies_count_and_editable_dto = CommentWithRepliesCountAndEditableDTOFactory(
            comment_id='91be920b-7b4c-49e7-8adb-41a0c18da848',
            comment_content='content',
            user_id='31be920b-7b4c-49e7-8adb-41a0c18da848',
            replies_count=0,
            is_editable=True
        )
        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_profile_dto = UserProfileDTOFactory(
            user_id='31be920b-7b4c-49e7-8adb-41a0c18da848',
            name='name ',
            profile_pic_url='https://graph.ib_users.com/'
        )

        # Act
        response_object = presenter.prepare_response_for_comment(
            comment_with_replies_count_and_editable_dto=\
                comment_with_replies_count_and_editable_dto,
            user_profile_dto=user_profile_dto
        )

        # Assert
        response_dict = json.loads(response_object.content)

        snapshot.assert_match(response_dict, "create_comment")
