import json

import pytest

from ib_discussions.constants.enum import StatusCode


class TestGetCommentsForDiscussionPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_discussions.presenters.get_comments_for_discussion_presenter_implementation import \
            GetCommentsForDiscussionPresenterImplementation
        presenter = GetCommentsForDiscussionPresenterImplementation()
        return presenter

    def test_response_for_discussion_id_not_found(self, presenter):
        # Arrange
        from ib_discussions.presenters.get_comments_for_discussion_presenter_implementation import \
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

    def test_response_for_comments_with_users_dtos(self, presenter, snapshot):
        # Arrange
        from ib_discussions.tests.factories.presenter_dtos import \
            CommentWithRepliesCountAndEditableDTOFactory
        comment_with_replies_count_and_editable_dtos = [
            CommentWithRepliesCountAndEditableDTOFactory(
                comment_id='91be920b-7b4c-49e7-8adb-41a0c18da848',
                comment_content='content',
                user_id='31be920b-7b4c-49e7-8adb-41a0c18da848',
                replies_count=0,
                is_editable=True
            ),
            CommentWithRepliesCountAndEditableDTOFactory(
                comment_id='11be920b-7b4c-49e7-8adb-41a0c18da848',
                comment_content='content',
                user_id='41be920b-7b4c-49e7-8adb-41a0c18da848',
                replies_count=2,
                is_editable=False
            ),
        ]

        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_profile_dtos = [
            UserProfileDTOFactory(
                user_id='31be920b-7b4c-49e7-8adb-41a0c18da848',
                name='name ',
                profile_pic_url='https://graph.ib_users.com/'
            ),
            UserProfileDTOFactory(
                user_id='41be920b-7b4c-49e7-8adb-41a0c18da848',
                name='name ',
                profile_pic_url='https://graph.ib_users.com/'
            ),
        ]

        # Act
        response_object = presenter.return_response_for_comments_with_users_dtos(
            comment_with_replies_count_and_editable_dtos= \
                comment_with_replies_count_and_editable_dtos,
            user_profile_dtos=user_profile_dtos
        )

        # Assert
        response_dict = json.loads(response_object.content)

        snapshot.assert_match(response_dict, "get_comments_for_discussion")
