"""
Successfully deleted
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02DeleteCommentAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['delete']}}

    def _get_or_create_user(self):
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_users.models import UserAccount
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.mark.django_db
    def test_with_valid_details_delete_comment(self, snapshot):
        comment_id = "413642ff-1272-4990-b878-6607a5e02bc1"
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_discussions.tests.factories.models import CommentFactory
        CommentFactory(
            id=comment_id, user_id=user_id
        )
        body = {}
        path_params = {"comment_id": comment_id}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
