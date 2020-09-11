"""
ALl exceptions
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02GetListOfUserRolesForGivenProjectAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture
    def setup(self, api_user):
        user_id = api_user.user_id
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.reset_sequence(0)
        user_object = UserDetailsFactory.create(user_id=user_id)
        return user_object

    @pytest.mark.django_db
    def test_with_invalid_project_id_return_response(
            self, snapshot, setup
    ):
        user_object = setup
        user_object.is_admin = True
        project_id = "project_1"
        body = {}
        path_params = {"project_id": project_id}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params, query_params=query_params,
            headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_with_user_is_not_admin_then_raise_exception(
            self, snapshot, setup
    ):
        project_id = "project_1"
        body = {}
        path_params = {"project_id": project_id}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params, query_params=query_params,
            headers=headers, snapshot=snapshot
        )
