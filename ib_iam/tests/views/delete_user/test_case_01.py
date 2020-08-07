"""
# Success case for delete user
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01DeleteUserAPITestCase(TestUtils):
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

    @pytest.fixture
    def set_up(self):
        from ib_iam.tests.factories.models import UserDetailsFactory, \
            CompanyFactory, UserRoleFactory, UserTeamFactory
        user_id = "413642ff-1272-4990-b878-6607a5e02bc2"
        delete_user_id = "413642ff-1272-4990-b878-6607a5e02bc1"
        UserDetailsFactory.create(user_id=user_id, is_admin=True)

        company = CompanyFactory.create()
        UserDetailsFactory.create(user_id=delete_user_id, company=company)
        from ib_iam.tests.factories.models import RoleFactory
        [UserRoleFactory.create(
            user_id=delete_user_id, role=RoleFactory.create()
        ) for _ in range(4)]
        from ib_iam.tests.factories.models import TeamFactory
        [UserTeamFactory.create(
            user_id=delete_user_id, team=TeamFactory.create()) for _ in
            range(4)]
        return delete_user_id, user_id

    @pytest.mark.django_db
    def test_case(self, set_up, snapshot):
        delete_user_id, user_id = set_up

        body = {}
        path_params = {"user_id": delete_user_id}
        query_params = {}
        headers = {}

        from ib_iam.tests.common_fixtures.adapters.user_service import \
            deactivate_user_in_ib_users_mock
        deactivate_user_in_ib_users_mock.return_value = None

        from ib_iam.models import UserDetails
        before_delete_users_count = UserDetails.objects.count()
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        after_delete_users_count = UserDetails.objects.count()

        snapshot.assert_match(name="before_delete_user_count",
                              value=before_delete_users_count)
        snapshot.assert_match(name="after_delete_user_count",
                              value=after_delete_users_count)
