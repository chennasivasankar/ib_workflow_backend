"""
All exceptions
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02AddCommentAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    def _get_or_create_user(self):
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_users.models import UserAccount
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.fixture()
    def prepare_discussion_id_not_found_mock_setup(self, mocker):
        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_validate_user_ids_mock
        prepare_validate_user_ids_mock(mocker=mocker)

    @pytest.mark.django_db
    def test_discussion_id_not_found_return_response(
            self, snapshot, prepare_discussion_id_not_found_mock_setup,
            prepare_multimedia_setup
    ):
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = "content"
        mention_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        multimedia = prepare_multimedia_setup

        body = {
            'comment_content': comment_content,
            'mention_user_ids': mention_user_ids,
            'multimedia': multimedia
        }
        path_params = {"discussion_id": discussion_id}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_with_empty_comment_content_and_multimedia_return_response(
            self, snapshot, prepare_discussion_id_not_found_mock_setup
    ):
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = ""
        mention_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        multimedia = []

        body = {
            'comment_content': comment_content,
            'mention_user_ids': mention_user_ids,
            'multimedia': multimedia
        }
        path_params = {"discussion_id": discussion_id}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.fixture()
    def prepare_invalid_user_ids_mock_setup(self, mocker):
        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_validate_user_ids_mock
        validate_user_ids_mock = prepare_validate_user_ids_mock(mocker=mocker)
        invalid_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_discussions.adapters.auth_service import InvalidUserIds
        validate_user_ids_mock.side_effect = InvalidUserIds(
            user_ids=invalid_user_ids)

    @pytest.mark.django_db
    def test_invalid_user_ids_return_response(
            self, snapshot, prepare_invalid_user_ids_mock_setup,
            prepare_multimedia_setup
    ):
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = "content"
        mention_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        multimedia = prepare_multimedia_setup

        body = {
            'comment_content': comment_content,
            'mention_user_ids': mention_user_ids,
            'multimedia': multimedia
        }
        path_params = {"discussion_id": discussion_id}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
