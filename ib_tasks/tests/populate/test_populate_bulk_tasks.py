import json
from unittest.mock import Mock

import factory
import pytest

from ib_tasks.models import Task
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_project_mock
from ib_tasks.tests.common_fixtures.storages import \
    elastic_storage_implementation_mock
from ib_tasks.tests.factories.adapter_dtos import UserDetailsDTOFactory, \
    AssigneeDetailsDTOFactory
from ib_tasks.tests.factories.models import ProjectTaskTemplateFactory, \
    TaskTemplateFactory, StageModelFactory, ActionPermittedRolesFactory, \
    StageActionFactory, GoFFactory, FieldFactory, GoFToTaskTemplateFactory, \
    GoFRoleFactory, FieldRoleFactory, TaskTemplateStatusVariableFactory, \
    StagePermittedRolesFactory, TaskTemplateInitialStageFactory, \
    StageGoFFactory


class TestPopulateBulkTasks:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
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
        StageGoFFactory.reset_sequence()

    @pytest.fixture
    def setup(self, mocker):
        template_id = 'FIN_PR'
        project_id = "CCBP"
        stage_id = "PR_CREATE_PAYMENT_REQUEST"
        variable = "variable0"
        gof_id = "FIN_REQUESTOR_DETAILS"
        field_id = "FIN_PAYMENT_REQUESTOR_NAME"
        user_id = "2399-0993-s43g-k989"

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock, \
            get_valid_project_ids_mock, get_projects_info_for_given_ids_mock, \
            get_team_info_for_given_user_ids_mock, \
            prepare_permitted_user_details_mock
        from ib_tasks.tests.common_fixtures. \
            adapters.assignees_details_service import \
            assignee_details_dtos_mock

        elastic_storage_implementation_mock(mocker)
        get_user_role_ids(mocker)
        is_user_in_project = True
        validate_if_user_is_in_project_mock(mocker, is_user_in_project)
        get_valid_project_ids_mock(mocker, [project_id])
        get_projects_info_for_given_ids_mock(mocker)
        get_team_info_for_given_user_ids_mock(mocker)
        get_user_role_ids_based_on_project_mock(mocker)
        prepare_permitted_user_details_mock_method = \
            prepare_permitted_user_details_mock(mocker)
        assignee_details_dtos_mock_method = assignee_details_dtos_mock(mocker)

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
            task_template_id='FIN_PR',
            display_logic="variable0==PR_CREATE_PAYMENT_REQUEST",
            card_info_kanban=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]),
            card_info_list=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]))
        path = 'ib_tasks.tests.populate.' \
               'stage_actions_logic.stage_1_action_name_1_logic'
        action = StageActionFactory(
            stage=stage, py_function_import_path=path,
            action_type="")
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")
        gof_obj = GoFFactory.create(gof_id=gof_id)
        StageGoFFactory.create(stage=stage, gof=gof_obj)
        field_obj = FieldFactory.create(field_id=field_id, gof=gof_obj)
        GoFToTaskTemplateFactory.create(
            task_template=task_template_obj, gof=gof_obj)

        from ib_tasks.constants.enum import PermissionTypes
        GoFRoleFactory.create(
            gof=gof_obj, permission_type=PermissionTypes.WRITE.value,
            role="FIN_PAYMENT_REQUESTER")
        FieldRoleFactory.create(
            field=field_obj, permission_type=PermissionTypes.WRITE.value,
            role="FIN_PAYMENT_REQUESTER")
        TaskTemplateStatusVariableFactory.create(
            task_template_id=template_id, variable=variable)

        from ib_tasks.constants.constants import ALL_ROLES_ID
        StagePermittedRolesFactory.create(stage=stage, role_id=ALL_ROLES_ID)
        TaskTemplateInitialStageFactory.create(
            task_template_id=template_id, stage=stage)
        return action.id, template_id, project_id, user_id

    @pytest.fixture
    def get_sheet_records_mock(self, mocker):
        records = [
            {
                "title*": "Project Alpha",
                "description": "alpha team",
                "start_date*": "2020-09-10",
                "due_date*": "2020-09-20",
                "priority*": "High",
                "FIN_PAYMENT_REQUESTOR_NAME": "Jason Momoa"
            },
            {
                "title*": "Project Beta",
                "description": "beta team",
                "start_date*": "2020-09-10",
                "due_date*": "2020-09-20",
                "priority*": "High",
                "FIN_PAYMENT_REQUESTOR_NAME": "Khal Drogo"
            },
            {
                "title*": "Project Gamma",
                "description": "gamma team",
                "start_date*": "2020-09-10",
                "due_date*": "2020-09-20",
                "priority*": "High",
                "FIN_PAYMENT_REQUESTOR_NAME": "Danerys stormborn"
            }
        ]
        worksheet_mock_object = Mock()
        sheet_mock = mocker.patch(
            "ib_tasks.utils.get_google_sheet.get_google_sheet")
        sheet_mock.worksheet.return_value = worksheet_mock_object
        worksheet_mock_object.get_all_records.return_value = records

    def test_with_valid_details(self, setup, get_sheet_records_mock, snapshot):
        # Arrange
        action_id, template_id, project_id, user_id = setup
        from ib_tasks.populate.populate_bulk_tasks import PopulateBulkTasks
        populate_bulk_tasks = PopulateBulkTasks(
            project_id=project_id, task_template_id=template_id,
            action_id=action_id, user_id=user_id)

        # Act
        populate_bulk_tasks.populate_bulk_tasks()

        # Assert
        task_objects = Task.objects.all()
        for task_object in task_objects:
            self._take_a_task_details_snapshot(task_object, snapshot)

    @staticmethod
    def _take_a_task_details_snapshot(task_object: Task, snapshot):
        from ib_tasks.models.task_gof import TaskGoF
        from ib_tasks.models.task_gof_field import TaskGoFField
        from ib_tasks.models import CurrentTaskStage
        from ib_tasks.models import TaskStageHistory

        task_id = task_object.id

        snapshot.assert_match(task_object.id, 'task_id')
        snapshot.assert_match(task_object.template_id, 'template_id')
        snapshot.assert_match(task_object.title, 'task_title')
        snapshot.assert_match(task_object.description, 'task_description')
        snapshot.assert_match(str(task_object.start_date), 'task_start_date')
        snapshot.assert_match(str(task_object.due_date), 'task_due_date')
        snapshot.assert_match(task_object.priority, 'task_priority')

        task_gofs = TaskGoF.objects.filter(task_id=task_id)
        counter = 1
        for task_gof in task_gofs:
            snapshot.assert_match(
                task_gof.same_gof_order, f'same_gof_order_{counter}')
            snapshot.assert_match(task_gof.gof_id, f'gof_id_{counter}')
            snapshot.assert_match(task_gof.task_id,
                                  f'gof_task_id_{counter}')
            counter = counter + 1

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

        current_task_stages = CurrentTaskStage.objects.filter(task_id=task_id)
        counter = 1
        for current_task_stage in current_task_stages:
            snapshot.assert_match(
                current_task_stage.task_id, f'task_id_{counter}')
            snapshot.assert_match(
                current_task_stage.stage_id, f'task_stage_{counter}'
            )
            counter += 1

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
