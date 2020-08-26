"""
Given valid details, it updates user profile
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

    # def _get_or_create_user(self):
    #     user_id = '217abeb3-6466-4440-96e7-bf02ee941bf8'
    #     from ib_users.models import UserAccount
    #     user = UserAccount.objects.create(user_id=user_id)
    #     return user

    # @pytest.mark.django_db
    # def test_duplicate_role_ids(self, setup, snapshot):
    #     body = {'name': 'username',
    #             'email': 'jaswanthmamidipudi@gmail.com',
    #             'profile_pic_url': 'https://sample.com',
    #             'role_ids': ["1", "1"],
    #             "cover_page_url": ""}
    #     path_params = {}
    #     query_params = {}
    #     headers = {}
    #     response = self.make_api_call(body=body,
    #                                   path_params=path_params,
    #                                   query_params=query_params,
    #                                   headers=headers,
    #                                   snapshot=snapshot)
    #
    # @pytest.mark.django_db
    # def test_invalid_role_ids(self, setup, snapshot):
    #     user_id = setup
    #     body = {'name': 'username',
    #             'email': 'jaswanthmamidipudi@gmail.com',
    #             'profile_pic_url': 'https://sample.com',
    #             'role_ids': ["2"],
    #             "cover_page_url": ""}
    #     path_params = {}
    #     query_params = {}
    #     headers = {}
    #     response = self.make_api_call(body=body,
    #                                   path_params=path_params,
    #                                   query_params=query_params,
    #                                   headers=headers,
    #                                   snapshot=snapshot)

    @pytest.fixture
    def setup(self, api_user):
        user_id = str(api_user.user_id)
        from ib_iam.tests.factories.models import UserDetailsFactory, ProjectRoleFactory
        UserDetailsFactory.create(user_id=user_id, is_admin=True)
        ProjectRoleFactory.create(id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                                  role_id='1')
        return user_id
