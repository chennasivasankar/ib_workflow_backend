'''
Update Discussion
'''

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02UpdateDiscussionAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    def _get_or_create_user(self):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        from ib_users.models import UserAccount
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.mark.django_db
    def test_update_discussion_return_response(self, snapshot):
        discussion_id = "413642ff-1272-4990-b878-6607a5e02bc1"
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        title = "Cyber Eye"
        description = "Provide Security"
        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory(
            id=discussion_id, title=title, description=description,
            user_id=user_id
        )

        body = {'title': title, 'description': description}
        path_params = {"discussion_id": discussion_id}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
