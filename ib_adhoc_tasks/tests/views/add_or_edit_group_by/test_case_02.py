# """
# all invalid cases
# """
# import pytest
# from django_swagger_utils.utils.test_utils import TestUtils
#
# from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
#
#
# class TestCase02AddOrEditGroupByAPITestCase(TestUtils):
#     APP_NAME = APP_NAME
#     OPERATION_NAME = OPERATION_NAME
#     REQUEST_METHOD = REQUEST_METHOD
#     URL_SUFFIX = URL_SUFFIX
#     SECURITY = {'oauth': {'scopes': ['write']}}
#
#     @pytest.mark.django_db
#     def test_one_group_by_already_exists_in_list_view_retuens_usser_not_allowed_to_create_more_than_one_group_by_in_list_view(
#             self, api_user, snapshot
#     ):
#         user_id = str(api_user.user_id)
#         from ib_adhoc_tasks.tests.factories.models import GroupByInfoFactory
#         from ib_adhoc_tasks.constants.enum import ViewType
#         GroupByInfoFactory(
#             user_id=user_id, view_type=ViewType.LIST.value, order=1
#         )
#         body = {
#             'view_type': 'LIST',
#             'group_by_key': "STAGE",
#             'order': 1,
#         }
#         path_params = {}
#         query_params = {"project_id": "project_id_1"}
#         headers = {}
#         self.make_api_call(body=body,
#                            path_params=path_params,
#                            query_params=query_params,
#                            headers=headers,
#                            snapshot=snapshot)
#
#     @pytest.mark.django_db
#     def test_two_group_by_already_exists_in_kaban_view_retuens_usser_not_allowed_to_create_more_than_two_group_by_in_kanban_view(
#             self, api_user, snapshot
#     ):
#         user_id = str(api_user.user_id)
#         from ib_adhoc_tasks.tests.factories.models import GroupByInfoFactory
#         from ib_adhoc_tasks.constants.enum import ViewType
#         GroupByInfoFactory.create_batch(
#             size=2, user_id=user_id, view_type=ViewType.KANBAN.value
#         )
#         body = {
#             'view_type': 'KANBAN',
#             'group_by_key': "priority",
#             'order': 2,
#             'group_by_id': None
#         }
#         path_params = {}
#         query_params = {"project_id": "project_id_1"}
#         headers = {}
#         self.make_api_call(body=body,
#                            path_params=path_params,
#                            query_params=query_params,
#                            headers=headers,
#                            snapshot=snapshot)
