"""
Created on: 08/08/20
Author: Pavankumar Pamuru

"""
import pytest

from ib_tasks.adapters.dtos import AssigneeDetailsDTO
from ib_tasks.constants.enum import ActionTypes
from ib_tasks.interactors.presenter_interfaces.dtos import AllTasksOverviewDetailsDTO
from ib_tasks.interactors.stages_dtos import StageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    StageActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO, TaskIdWithStageDetailsDTO, TaskWithCompleteStageDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import TaskStageStorageInterface
from ib_tasks.tests.common_fixtures.interactors import prepare_get_stage_ids_for_user
from ib_tasks.tests.factories.presenter_dtos import TaskWithCompleteStageDetailsDTOFactory


class TestGetTasksOverviewForUserInteractor:

    @pytest.fixture
    def task_actions_fields(self):
        return [GetTaskStageCompleteDetailsDTO(
            task_id=1,
            stage_id='stage_id_1',
            stage_color="blue",
            field_dtos=[
                FieldDetailsDTO(
                    field_type='Drop down',
                    field_id='FIELD-ID-1',
                    key='key', value='value'
                ),
                FieldDetailsDTO(
                    field_type='Drop down',
                    field_id='FIELD-ID-2',
                    key='key', value='value')
            ],
            action_dtos=[
                StageActionDetailsDTO(
                    action_id=1,
                    name='name_1',
                    stage_id='stage_id_1',
                    button_text='button_text_1',
                    button_color=None,
                    action_type=ActionTypes.NO_VALIDATIONS.value,
                    transition_template_id='template_id_1'
                ),
                StageActionDetailsDTO(
                    action_id=2,
                    name='name_2',
                    stage_id='stage_id_1',
                    button_text='button_text_2',
                    button_color=None,
                    action_type=ActionTypes.NO_VALIDATIONS.value,
                    transition_template_id='template_id_2'
                )
            ]
        )]

    @pytest.fixture
    def expected_response(self):
        return AllTasksOverviewDetailsDTO(task_with_complete_stage_details_dtos=[
            TaskWithCompleteStageDetailsDTO(
                task_with_stage_details_dto=TaskIdWithStageDetailsDTO(
                    db_stage_id=1, task_id=1, stage_id='stage_1',
                    stage_display_name='stage_display_1',
                    stage_color='color_1'),
                stage_assignee_dto=StageAssigneeDetailsDTO(
                    task_stage_id=1, stage_id=0,
                    assignee_details_dto=AssigneeDetailsDTO(
                        assignee_id='123e4567-e89b-12d3-a456-426614174000',
                        name='name_0',
                        profile_pic_url=
                        'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM')))],
            task_fields_and_action_details_dtos=[
                GetTaskStageCompleteDetailsDTO(
                    task_id=1,
                    stage_id='stage_id_1',
                    stage_color='blue',
                    field_dtos=[FieldDetailsDTO(
                        field_type='Drop down',
                        field_id='FIELD-ID-1',
                        key='key', value='value'),
                        FieldDetailsDTO(
                            field_type='Drop down',
                            field_id='FIELD-ID-2',
                            key='key',
                            value='value')],
                    action_dtos=[
                        StageActionDetailsDTO(
                            action_id=1,
                            name='name_1',
                            stage_id='stage_id_1',
                            button_text='button_text_1',
                            button_color=None,
                            action_type=ActionTypes.NO_VALIDATIONS.value,
                            transition_template_id='template_id_1'),
                        StageActionDetailsDTO(
                            action_id=2,
                            name='name_2',
                            stage_id='stage_id_1',
                            button_text='button_text_2',
                            button_color=None,
                            action_type=ActionTypes.NO_VALIDATIONS.value,
                            transition_template_id='template_id_2')])])

    def test_get_filtered_tasks_overview_for_user_with_valid_details(
            self, mocker, task_actions_fields, expected_response):
        # Arrange
        user_id = 'user_id'
        task_ids = [1, 2, 3]

        from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
            StageStorageInterface
        from unittest.mock import create_autospec
        stage_storage = create_autospec(StageStorageInterface)
        task_stage_storage = create_autospec(TaskStageStorageInterface)
        from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
            TaskStorageInterface
        task_storage = create_autospec(TaskStorageInterface)
        from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
            FieldsStorageInterface
        field_storage = create_autospec(FieldsStorageInterface)
        from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
            ActionStorageInterface
        action_storage = create_autospec(ActionStorageInterface)
        from ib_tasks.interactors.get_all_task_overview_with_filters_and_searches_for_user \
            import GetTasksOverviewForUserInteractor

        interactor = GetTasksOverviewForUserInteractor(
            stage_storage=stage_storage,
            task_storage=task_storage,
            field_storage=field_storage,
            action_storage=action_storage,
            task_stage_storage=task_stage_storage
        )
        from ib_tasks.tests.factories.presenter_dtos import \
            TaskIdWithStageDetailsDTOFactory
        TaskIdWithStageDetailsDTOFactory.reset_sequence()
        stage_ids_dto = TaskWithCompleteStageDetailsDTOFactory.create_batch(2)
        fields_and_actions = task_actions_fields
        stage_ids = ['stage_id_1', "stage_id_2"]
        prepare_get_stage_ids_for_user(mocker, stage_ids)
        from ib_tasks.tests.common_fixtures.interactors import \
            prepare_task_ids_with_stage_ids
        prepare_task_ids_with_stage_ids(
            mocker=mocker,
            stage_ids_dto=stage_ids_dto,
            fields_and_actions=fields_and_actions,
            stage_ids=stage_ids
        )
        from ib_tasks.constants.enum import ViewType
        view_type = ViewType.KANBAN.value
        # Act
        actual_response = interactor.get_filtered_tasks_overview_for_user(
            user_id=user_id,
            task_ids=task_ids,
            view_type=view_type
        )

        # Assert
        assert actual_response == expected_response
