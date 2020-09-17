"""
Given valid details, it updates user profile and user roles
as user is admin
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01UpdateUserProfileAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture
    def setup(self, api_user):
        user_id = str(api_user.user_id)
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_object = UserDetailsFactory.create(user_id=user_id, is_admin=True)
        from ib_iam.tests.factories.models import ProjectRoleFactory, \
            UserRoleFactory
        role_object = ProjectRoleFactory.create(
            role_id='1', name="role_1")
        user_role_object = UserRoleFactory(user_id=user_id,
                                           project_role=role_object)
        return user_id, user_role_object, user_object, role_object

    @pytest.mark.django_db
    def test_case(self, mocker, setup, snapshot):
        user_id = setup[0]
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        update_user_profile_adapter_mock(mocker=mocker)
        body = {'name': 'username',
                'email': 'jaswanthmamidipudi@gmail.com',
                'profile_pic_url': 'https://sample.com',
                'role_ids': ["1"],
                "cover_page_url": ""}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            snapshot=snapshot
        )
        from ib_iam.models import UserDetails, UserRole
        user_object = UserDetails.objects.get(user_id=user_id, is_admin=True)
        snapshot.assert_match(user_object.name, "updated_user_name")
        # user_role = UserRole.objects.get(user_id=user_id)
        # snapshot.assert_match(user_role.project_role.name,
        #                       "updated_user_role_id")
