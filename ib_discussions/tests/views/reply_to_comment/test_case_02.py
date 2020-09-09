"""
All exceptions
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02ReplyToCommentAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_comment_id_not_found_return_response(self, snapshot, mocker):
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_validate_user_ids_mock
        prepare_validate_user_ids_mock(mocker=mocker)

        from ib_discussions.constants.enum import MultimediaFormat
        multimedia = [{
            "format_type": MultimediaFormat.IMAGE.value,
            "url": "https://picsum.photos/200",
            "thumbnail_url": "https://picsum.photos/200"
        }, {
            "format_type": MultimediaFormat.VIDEO.value,
            "url": "https://picsum.photos/200",
            "thumbnail_url": "https://picsum.photos/200"
        }]
        mention_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        body = {
            'comment_content': "string",
            'mention_user_ids': mention_user_ids,
            'multimedia': multimedia
        }
        path_params = {"comment_id": comment_id}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_with_empty_comment_content_and_multimedia_return_response(
            self, snapshot
    ):
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = ""
        multimedia = []
        mention_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]

        body = {
            'comment_content': comment_content,
            'mention_user_ids': mention_user_ids,
            'multimedia': multimedia
        }
        path_params = {"comment_id": comment_id}
        query_params = {}
        headers = {}
        response = self.make_api_call(
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
            self, snapshot, prepare_invalid_user_ids_mock_setup
    ):
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_discussions.constants.enum import MultimediaFormat
        multimedia = [{
            "format_type": MultimediaFormat.IMAGE.value,
            "url": "https://picsum.photos/200",
            "thumbnail_url": "https://picsum.photos/200"
        }, {
            "format_type": MultimediaFormat.VIDEO.value,
            "url": "https://picsum.photos/200",
            "thumbnail_url": "https://picsum.photos/200"
        }]
        mention_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]

        body = {
            'comment_content': "string",
            'mention_user_ids': mention_user_ids,
            'multimedia': multimedia
        }
        path_params = {"comment_id": comment_id}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
