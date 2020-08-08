"""
All exceptions
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02ReplyToCommentAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_comment_id_not_found_return_response(self, snapshot):
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_discussions.constants.enum import MultiMediaFormatEnum
        multimedia = [
            {
                "format_type": MultiMediaFormatEnum.IMAGE.value,
                "url": "https://picsum.photos/200"
            },
            {
                "format_type": MultiMediaFormatEnum.VIDEO.value,
                "url": "https://picsum.photos/200"
            }
        ]
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
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
