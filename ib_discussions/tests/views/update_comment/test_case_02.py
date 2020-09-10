"""
comment_id not found and user cannot delete exceptions
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02UpdateCommentAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    def _get_or_create_user(self):
        user_id = "11be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_users.models import UserAccount
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.mark.django_db
    def test_with_user_cannot_edit_for_given_comment_id(
            self, snapshot, prepare_discussion_with_comment_setup,
            prepare_users_setup, prepare_multimedia_setup):
        mention_user_ids = prepare_users_setup
        multimedia = prepare_multimedia_setup
        comment_content = "Hai, How are you?"
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"

        body = {
            'comment_content': comment_content,
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
    def test_with_comment_id_not_found(
            self, snapshot, prepare_discussion_with_comment_setup,
            prepare_users_setup, prepare_multimedia_setup):
        mention_user_ids = prepare_users_setup
        multimedia = prepare_multimedia_setup
        comment_content = "Hai, How are you?"
        comment_id = "01be920b-7b4c-49e7-8adb-41a0c18da848"

        body = {
            'comment_content': comment_content,
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
