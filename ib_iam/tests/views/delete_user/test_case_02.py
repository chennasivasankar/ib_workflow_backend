"""
# Invalid cases for delete user
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02DeleteUserAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['delete']}}

    def _get_or_create_user(self):
        user_id = "413642ff-1272-4990-b878-6607a5e02bc2"
        from ib_users.models import UserAccount
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.mark.django_db
    def test_with_invalid_admin_user_then_raise_exception(self, snapshot):
        from ib_iam.tests.factories.models import UserDetailsFactory, \
            CompanyFactory
        user_id = "413642ff-1272-4990-b878-6607a5e02bc2"
        delete_user_id = "413642ff-1272-4990-b878-6607a5e02bc1"
        UserDetailsFactory.create(user_id=user_id, is_admin=False)

        company = CompanyFactory.create()
        UserDetailsFactory.create(user_id=delete_user_id, company=company)

        body = {}
        path_params = {"user_id": delete_user_id}
        query_params = {}
        headers = {}

        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_with_invalid_delete_user_and_delete_user_id_not_found_then_raise_exception(
            self, snapshot):
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "413642ff-1272-4990-b878-6607a5e02bc2"
        UserDetailsFactory.create(user_id=user_id, is_admin=True)
        delete_user_id = "413642ff-1272-4990-b878-6607a5e02bc1"

        body = {}
        path_params = {"user_id": delete_user_id}
        query_params = {}
        headers = {}

        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_with_invalid_delete_user_and_delete_user_id_is_admin_then_raise_exception(
            self, snapshot):
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "413642ff-1272-4990-b878-6607a5e02bc2"
        UserDetailsFactory.create(user_id=user_id, is_admin=True)
        delete_user_id = "413642ff-1272-4990-b878-6607a5e02bc1"
        UserDetailsFactory.create(user_id=delete_user_id, is_admin=True)

        body = {}
        path_params = {"user_id": delete_user_id}
        query_params = {}
        headers = {}

        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
