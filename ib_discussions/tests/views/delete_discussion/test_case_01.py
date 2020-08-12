"""
test all exception
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01DeleteDiscussionAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_discussion_id_not_found_return_response(self, snapshot):
        discussion_id = "413642ff-1272-4990-b878-6607a5e02bc1"
        body = {}
        path_params = {"discussion_id": discussion_id}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_user_cannot_delete_discussion_return_response(self, snapshot):
        discussion_id = "413642ff-1272-4990-b878-6607a5e02bc1"
        title = "Cyber Eye"
        description = "Provide Security"
        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory(
            id=discussion_id, title=title, description=description
        )

        body = {'title': title, 'description': description}
        path_params = {"discussion_id": discussion_id}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
