"""
Created on: 08/08/20
Author: Pavankumar Pamuru

"""
import pytest

from ib_tasks.constants.enum import ActionTypes
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    StageActionDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO


class TestGetTasksOverviewForUserInteractor:

    @pytest.fixture
    def task_actions_fields(self):
        return GetTaskStageCompleteDetailsDTO(
                    task_id=1,
                    stage_id='stage_id_1',
                    field_dtos=[
                        FieldDetailsDTO(
                            field_type='Drop down',
                            field_id=1,
                            key='key', value='value'
                        ),
                        FieldDetailsDTO(
                            field_type='Drop down',
                            field_id=2,
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
                )

    def test_get_filtered_tasks_overview_for_user_with_valid_details(
            self, mocker, task_actions_fields):
        # Arrange
        user_id = 'user_id'
        task_ids = ['task_1', 'task_2', 'task_3']

        from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
            StageStorageInterface
        from unittest.mock import create_autospec
        stage_storage = create_autospec(StageStorageInterface)
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
        )
        from ib_tasks.tests.factories.presenter_dtos import \
            TaskIdWithStageDetailsDTOFactory
        TaskIdWithStageDetailsDTOFactory.reset_sequence()
        stage_ids_dto = TaskIdWithStageDetailsDTOFactory.create_batch(2)
        fields_and_actions = task_actions_fields
        stage_ids = ['stage_id_1', "stage_id_2"]
        from ib_tasks.interactors.presenter_interfaces.dtos import \
            AllTasksOverviewDetailsDTO
        expected_response = AllTasksOverviewDetailsDTO(
            task_id_with_stage_details_dtos=stage_ids_dto,
            task_fields_and_action_details_dtos=fields_and_actions
        )
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
