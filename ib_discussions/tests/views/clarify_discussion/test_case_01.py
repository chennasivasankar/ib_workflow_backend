"""
mark as clarified the discussion
"""

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01ClarifyDiscussionAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    def _get_or_create_user(self):
        user_id = "9cc22e39-2390-4d96-b7ac-6bb27816461f"
        from django.contrib.auth import get_user_model
        user_model = get_user_model()
        username = self.API_USER_CONFIG['username']
        password = self.API_USER_CONFIG['password']
        email = self.API_USER_CONFIG['email']
        is_staff = self.API_USER_CONFIG['is_staff']
        try:
            user = user_model.objects.get(username=username)
        except user_model.DoesNotExist:
            user = user_model.objects.create_user(
                username,
                email,
                password,
                is_staff=is_staff,
                user_id=user_id
            )
        return user

    @pytest.mark.django_db
    def test_case(self, snapshot):
        discussion_id = "413642ff-1272-4990-b878-6607a5e02bc1"
        user_id = "9cc22e39-2390-4d96-b7ac-6bb27816461f"
        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory.create_batch(2)
        DiscussionFactory(id=discussion_id, user_id=user_id)

        body = {}
        path_params = {"discussion_id": discussion_id}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )