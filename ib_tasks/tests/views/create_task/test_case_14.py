"""
test with valid details creates task
when a field is gof selector and user has permission for multiple gofs in
that gof selector name and we have to bypass the user permitted fields
validation for those gofs as use can only select one gof and it's fields
even though he has permission over all gofs and it's fields
"""
import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.tests.common_fixtures.adapters.auth_service import \
    get_user_id_team_details_dtos_mock, get_user_details_with_roles_mock
from ib_tasks.tests.common_fixtures.adapters.project_service import \
    get_valid_project_ids_mock
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_project_mock, \
    get_user_role_ids_based_on_projects_mock
from ib_tasks.tests.common_fixtures.storages import \
    elastic_storage_implementation_mock
from ib_tasks.tests.factories import models
from ib_tasks.tests.views.create_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX


class TestCase01CreateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        import json
        from ib_tasks.tests.factories.models import \
            ProjectTaskTemplateFactory, TaskTemplateFactory, \
            StageModelFactory, ActionPermittedRolesFactory, \
            StageActionFactory, GoFFactory, FieldFactory, \
            GoFToTaskTemplateFactory, GoFRoleFactory, FieldRoleFactory, \
            TaskTemplateStatusVariableFactory, \
            StagePermittedRolesFactory, TaskTemplateInitialStageFactory
        from ib_tasks.tests.factories.adapter_dtos import \
            UserDetailsDTOFactory, AssigneeDetailsDTOFactory

        ProjectTaskTemplateFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        TaskTemplateStatusVariableFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()
        TaskTemplateInitialStageFactory.reset_sequence()
        UserDetailsDTOFactory.reset_sequence()
        AssigneeDetailsDTOFactory.reset_sequence()

        template_id = 'template_1'
        project_id = "project_1"
        stage_id = "stage_1"
        variable = "variable0"

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock, get_valid_project_ids_mock \
            as auth_service_project_ids_mock, \
            get_projects_info_for_given_ids_mock, \
            get_team_info_for_given_user_ids_mock, \
            prepare_permitted_user_details_mock
        from ib_tasks.tests.common_fixtures. \
            adapters.assignees_details_service import \
            assignee_details_dtos_mock

        elastic_storage_implementation_mock(mocker)
        user_roles_mock = get_user_role_ids(mocker)
        user_roles = user_roles_mock.return_value
        is_user_in_project = True
        validate_if_user_is_in_project_mock(mocker, is_user_in_project)
        auth_service_project_ids_mock(mocker, [project_id])
        project_mock = get_valid_project_ids_mock(mocker)
        project_mock.return_value = [project_id]
        get_user_id_team_details_dtos_mock(mocker)
        get_projects_info_for_given_ids_mock(mocker)
        get_team_info_for_given_user_ids_mock(mocker)
        get_user_role_ids_based_on_project_mock(mocker)
        prepare_permitted_user_details_mock_method = \
            prepare_permitted_user_details_mock(mocker)
        assignee_details_dtos_mock_method = assignee_details_dtos_mock(mocker)
        get_user_details_with_roles_mock(mocker, user_roles)
        get_user_role_ids_based_on_projects_mock(mocker, project_ids=[project_id])

        prepare_permitted_user_details_mock_method.return_value = \
            UserDetailsDTOFactory.create_batch(
                size=2, user_id=factory.Iterator(["user_1", "user_2"]))
        assignee_details_dtos_mock_method.return_value = \
            AssigneeDetailsDTOFactory.create_batch(
                size=2, assignee_id=factory.Iterator(["user_1", "user_2"]))

        task_template_obj = TaskTemplateFactory.create(template_id=template_id)
        ProjectTaskTemplateFactory.create(
            task_template=task_template_obj, project_id=project_id)
        stage = StageModelFactory(
            stage_id=stage_id, stage_color="blue",
            task_template_id='template_1',
            display_logic="variable0==stage_1",
            card_info_kanban=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]),
            card_info_list=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]))
        path = 'ib_tasks.tests.populate.' \
               'stage_actions_logic.stage_1_action_name_1_logic'
        action = StageActionFactory(
            stage=stage, py_function_import_path=path,
            action_type="")
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")
        gof_selector_gof_ids = [
            "FIN_VENDOR_PAYMENT_DETAILS",
            "FIN_VENDOR_ONLINE_EXPENSE_TYPE"
            "FIN_ONLINE_ORDER_DETAILS",
            "FIN_GST_DETAILS"
        ]
        gof_selector_objects = GoFFactory.create_batch(
            size=len(gof_selector_gof_ids),
            gof_id=factory.Iterator(gof_selector_gof_ids))
        payment_type_gof = GoFFactory.create(gof_id="FIN_PAYMENT_TYPE")
        gof_objects = gof_selector_objects + [payment_type_gof]
        models.StageGoFFactory.create_batch(
            size=len(gof_objects), stage=stage,
            gof=factory.Iterator(gof_objects))
        fields = FieldFactory.create_batch(
            size=len(gof_selector_objects),
            gof=factory.Iterator(gof_selector_objects))
        gof_selector_field = FieldFactory.create(
            field_id="FIN_TYPE_OF_PAYMENT_REQUEST",
            gof=payment_type_gof,
            field_type=FieldTypes.GOF_SELECTOR.value,
            field_values=json.dumps([
                {
                    "name": "Vendor Payment",
                    "gof_ids": [
                        "FIN_VENDOR_PAYMENT_DETAILS",
                        "FIN_VENDOR_ONLINE_EXPENSE_TYPE"
                    ]
                },
                {
                    "name": "Online Orders/3rd Party Site Payment",
                    "gof_ids": [
                        "FIN_ONLINE_ORDER_DETAILS",
                        "FIN_GST_DETAILS"
                    ]
                }
            ]))
        fields.append(gof_selector_field)
        GoFToTaskTemplateFactory.create_batch(
            size=len(gof_selector_objects), task_template=task_template_obj,
            gof=factory.Iterator(gof_selector_objects), order=-1)
        GoFToTaskTemplateFactory.create(task_template=task_template_obj,
                                        gof=payment_type_gof)

        from ib_tasks.constants.enum import PermissionTypes
        GoFRoleFactory.create_batch(
            size=len(gof_objects),
            gof=factory.Iterator(gof_objects),
            permission_type=PermissionTypes.WRITE.value,
            role="FIN_PAYMENT_REQUESTER")
        FieldRoleFactory.create_batch(
            size=len(fields),
            field=factory.Iterator(fields),
            permission_type=PermissionTypes.WRITE.value,
            role="FIN_PAYMENT_REQUESTER")
        TaskTemplateStatusVariableFactory.create(
            task_template_id=template_id, variable=variable)

        from ib_tasks.constants.constants import ALL_ROLES_ID
        StagePermittedRolesFactory.create(stage=stage, role_id=ALL_ROLES_ID)
        TaskTemplateInitialStageFactory.create(
            task_template_id=template_id, stage=stage)

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "project_id": "project_1",
            "task_template_id": "template_1",
            "action_id": 1,
            "title": "task_title",
            "description": "task_description",
            "start_datetime": "2020-09-20 00:00:00",
            "due_datetime": "2020-10-31 00:00:00",
            "priority": "HIGH",
            "task_gofs": [
                {
                    "gof_id": "FIN_PAYMENT_TYPE",
                    "same_gof_order": 1,
                    "gof_fields": [
                        {
                            "field_id": "FIN_TYPE_OF_PAYMENT_REQUEST",
                            "field_response": "Vendor Payment"
                        }
                    ]
                },
                {
                    "gof_id": "FIN_VENDOR_PAYMENT_DETAILS",
                    "same_gof_order": 1,
                    "gof_fields": [
                        {
                            "field_id": "FIELD_ID-0",
                            "field_response": "vendor payment details"
                        }
                    ]
                }
            ]
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)
        from ib_tasks.models.task import Task
        task_object = Task.objects.get(id=1)
        snapshot.assert_match(task_object.id, 'task_id')
        snapshot.assert_match(task_object.template_id, 'template_id')
        snapshot.assert_match(task_object.title, 'task_title')
        snapshot.assert_match(task_object.description, 'task_description')
        snapshot.assert_match(str(task_object.start_date), 'task_start_date')
        snapshot.assert_match(str(task_object.due_date), 'task_due_date')
        snapshot.assert_match(task_object.priority, 'task_priority')

        task_id = 1
        from ib_tasks.models.task_gof import TaskGoF
        task_gofs = TaskGoF.objects.filter(task_id=task_id)
        counter = 1
        for task_gof in task_gofs:
            snapshot.assert_match(
                task_gof.same_gof_order, f'same_gof_order_{counter}')
            snapshot.assert_match(task_gof.gof_id, f'gof_id_{counter}')
            snapshot.assert_match(task_gof.task_id,
                                  f'gof_task_id_{counter}')
            counter = counter + 1

        from ib_tasks.models.task_gof_field import TaskGoFField
        task_gof_fields = TaskGoFField.objects.filter(
            task_gof__task_id=task_id)
        counter = 1
        for task_gof_field in task_gof_fields:
            snapshot.assert_match(task_gof_field.task_gof_id,
                                  f'task_gof_{counter}')
            snapshot.assert_match(task_gof_field.field_id, f'field_{counter}')
            snapshot.assert_match(task_gof_field.field_response,
                                  f'field_response_{counter}')
            counter = counter + 1

        from ib_tasks.models import CurrentTaskStage
        current_task_stages = CurrentTaskStage.objects.filter(task_id=task_id)
        counter = 1
        for current_task_stage in current_task_stages:
            snapshot.assert_match(
                current_task_stage.task_id, f'task_id_{counter}')
            snapshot.assert_match(
                current_task_stage.stage_id, f'task_stage_{counter}'
            )
            counter += 1

        counter = 1
        from ib_tasks.models import TaskStageHistory
        task_stage_histories = TaskStageHistory.objects.filter(task_id=task_id)
        for task_stage_history in task_stage_histories:
            snapshot.assert_match(
                task_stage_history.task_id, f'task_id_{counter}')
            snapshot.assert_match(
                task_stage_history.stage, f'stage_{counter}')
            snapshot.assert_match(
                task_stage_history.team_id, f'team_id_{counter}')
            snapshot.assert_match(
                task_stage_history.assignee_id, f'assignee_id_{counter}')
            snapshot.assert_match(
                task_stage_history.joined_at, f'joined_at_{counter}')
            snapshot.assert_match(
                task_stage_history.left_at, f'left_at_{counter}')
