# """
# test with invalid custom logic exception raises exception
# """
# import factory
# import pytest
# from django_swagger_utils.utils.test_utils import TestUtils
#
# from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
# from ...common_fixtures.adapters.roles_service import \
#     get_user_role_ids_based_on_project_mock
#
#
# class TestCase38CreateTaskAPITestCase(TestUtils):
#     APP_NAME = APP_NAME
#     OPERATION_NAME = OPERATION_NAME
#     REQUEST_METHOD = REQUEST_METHOD
#     URL_SUFFIX = URL_SUFFIX
#     SECURITY = {'oauth': {'scopes': ['write']}}
#
#     @pytest.fixture(autouse=True)
#     def setup(self, mocker):
#         import json
#         from ib_tasks.tests.factories.models import \
#             ProjectTaskTemplateFactory, TaskTemplateFactory, \
#             StageModelFactory, ActionPermittedRolesFactory, \
#             StageActionFactory, GoFFactory, FieldFactory, \
#             GoFToTaskTemplateFactory, GoFRoleFactory, FieldRoleFactory, \
#             TaskTemplateStatusVariableFactory, \
#             StagePermittedRolesFactory, TaskTemplateInitialStageFactory
#         from ib_tasks.tests.factories.adapter_dtos import \
#             UserDetailsDTOFactory, AssigneeDetailsDTOFactory
#
#         ProjectTaskTemplateFactory.reset_sequence()
#         TaskTemplateFactory.reset_sequence()
#         StageModelFactory.reset_sequence()
#         ActionPermittedRolesFactory.reset_sequence()
#         StageActionFactory.reset_sequence()
#         GoFFactory.reset_sequence()
#         FieldFactory.reset_sequence()
#         GoFToTaskTemplateFactory.reset_sequence()
#         GoFRoleFactory.reset_sequence()
#         FieldRoleFactory.reset_sequence()
#         TaskTemplateStatusVariableFactory.reset_sequence()
#         StagePermittedRolesFactory.reset_sequence()
#         TaskTemplateInitialStageFactory.reset_sequence()
#         UserDetailsDTOFactory.reset_sequence()
#         AssigneeDetailsDTOFactory.reset_sequence()
#
#         template_id = 'template_1'
#         project_id = "project_1"
#         stage_id = "stage_1"
#         variable = "variable0"
#         from ib_tasks.tests.common_fixtures.adapters.auth_service import \
#             get_valid_project_ids_mock
#         get_valid_project_ids_mock(mocker, [project_id])
#
#         from ib_tasks.tests.common_fixtures.adapters.roles_service import \
#             get_user_role_ids
#         from ib_tasks.tests.common_fixtures.adapters.auth_service import \
#             validate_if_user_is_in_project_mock, \
#             get_valid_project_ids_mock, get_projects_info_for_given_ids_mock, \
#             get_team_info_for_given_user_ids_mock, \
#             prepare_permitted_user_details_mock
#         from ib_tasks.tests.common_fixtures.\
#             adapters.assignees_details_service import \
#             assignee_details_dtos_mock
#
#         get_user_role_ids(mocker)
#         is_user_in_project = True
#         validate_if_user_is_in_project_mock(mocker, is_user_in_project)
#         get_valid_project_ids_mock(mocker, [project_id])
#         get_user_role_ids_based_on_project_mock(mocker)
#         get_projects_info_for_given_ids_mock(mocker)
#         get_team_info_for_given_user_ids_mock(mocker)
#         prepare_permitted_user_details_mock_method = \
#             prepare_permitted_user_details_mock(mocker)
#         assignee_details_dtos_mock_method = assignee_details_dtos_mock(mocker)
#
#         prepare_permitted_user_details_mock_method.return_value = \
#             UserDetailsDTOFactory.create_batch(
#                 size=2, user_id=factory.Iterator(["user_1", "user_2"]))
#         assignee_details_dtos_mock_method.return_value = \
#             AssigneeDetailsDTOFactory.create_batch(
#                 size=2, assignee_id=factory.Iterator(["user_1", "user_2"]))
#
#         task_template_obj = TaskTemplateFactory.create(template_id=template_id)
#         ProjectTaskTemplateFactory.create(
#             task_template=task_template_obj, project_id=project_id)
#         stage = StageModelFactory(
#             stage_id=stage_id,
#             task_template_id='template_1',
#             display_logic="variable0==stage_1",
#             card_info_kanban=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]),
#             card_info_list=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]))
#         path = 'ib_tasks.tests.populate.' \
#                'stage_actions.stage_1_action_name_1'
#         action = StageActionFactory(
#             stage=stage, py_function_import_path=path
#         )
#         ActionPermittedRolesFactory.create(
#             action=action, role_id="FIN_PAYMENT_REQUESTER")
#         gof_obj = GoFFactory.create()
#
#         field_obj = FieldFactory.create(gof=gof_obj)
#         GoFToTaskTemplateFactory.create(
#             task_template=task_template_obj, gof=gof_obj)
#
#         from ib_tasks.constants.enum import PermissionTypes
#         GoFRoleFactory.create(
#             gof=gof_obj, permission_type=PermissionTypes.WRITE.value,
#             role="FIN_PAYMENT_REQUESTER"
#         )
#         FieldRoleFactory.create(
#             field=field_obj, permission_type=PermissionTypes.WRITE.value,
#             role="FIN_PAYMENT_REQUESTER"
#         )
#         TaskTemplateStatusVariableFactory.create(
#             task_template_id=template_id, variable=variable)
#
#         from ib_tasks.constants.constants import ALL_ROLES_ID
#         StagePermittedRolesFactory.create(stage=stage, role_id=ALL_ROLES_ID)
#         TaskTemplateInitialStageFactory.create(
#             task_template_id=template_id, stage=stage)
#
#     @pytest.mark.django_db
#     def test_case(self, snapshot):
#         body = {
#             "project_id": "project_1",
#             "task_template_id": "template_1",
#             "action_id": 1,
#             "title": "task_title",
#             "description": "task_description",
#             "start_datetime": "2020-09-20 00:00:00",
#             "due_datetime": "2020-10-31 00:00:00",
#             "priority": "HIGH",
#             "task_gofs": [
#                 {
#                     "gof_id": "gof_1",
#                     "same_gof_order": 1,
#                     "gof_fields": [
#                         {
#                             "field_id": "FIELD_ID-0",
#                             "field_response": "field_0_response"
#                         }
#                     ]
#                 }
#             ]
#         }
#         path_params = {}
#         query_params = {}
#         headers = {}
#         self.make_api_call(body=body,
#                            path_params=path_params,
#                            query_params=query_params,
#                            headers=headers,
#                            snapshot=snapshot)
