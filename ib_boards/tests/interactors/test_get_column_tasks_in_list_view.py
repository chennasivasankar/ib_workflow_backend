"""
Created on: 05/09/20
Author: Pavankumar Pamuru

"""
from unittest.mock import Mock

import factory
import pytest

from ib_boards.constants.enum import ViewType
from ib_boards.interactors.dtos import ColumnTasksParametersDTO, \
    TaskIdStageDTO, \
    TaskCompleteDetailsDTO
from ib_boards.interactors.get_column_tasks_interactor import \
    GetColumnTasksInteractor
from ib_boards.tests.factories.interactor_dtos import \
    FieldDetailsDTOFactory, GetTaskDetailsDTOFactory, \
    ColumnTaskIdsDTOFactory, TaskStageIdDTOFactory, ColumnStageIdsDTOFactory, \
    StageAssigneesDTOFactory, AllFieldsDTOFactory
from ib_boards.tests.factories.storage_dtos import TaskActionsDTOFactory
from ib_boards.tests.factories.storage_dtos import TaskDTOFactory, \
    TaskStageDTOFactory
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO


class TestGetColumnTasksInteractor:

    @pytest.fixture
    def task_stage_color_dtos(self):
        TaskStageDTOFactory.reset_sequence()
        return TaskStageDTOFactory.create_batch(size=3)

    @pytest.fixture
    def storage_mock(self):
        from ib_boards.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        from unittest import mock
        storage = mock.create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_boards.interactors.presenter_interfaces.presenter_interface import \
            GetColumnTasksListViewPresenterInterface
        presenter = mock.create_autospec(
            GetColumnTasksListViewPresenterInterface)
        return presenter

    @pytest.fixture
    def get_column_tasks_dto(self):
        return ColumnTasksParametersDTO(
            user_id='user_id_1',
            view_type=ViewType.LIST.value,
            column_id='COLUMN_ID_1',
            offset=0,
            limit=5,
            search_query="hello"
        )

    @pytest.fixture
    def get_column_tasks_dto_with_invalid_offset(self):
        return ColumnTasksParametersDTO(
            user_id=1,
            view_type=ViewType.LIST.value,
            column_id='COLUMN_ID_1',
            offset=-1,
            limit=1,
            search_query="hello"
        )

    @pytest.fixture
    def get_column_tasks_dto_with_invalid_limit(self):
        return ColumnTasksParametersDTO(
            user_id=1,
            view_type=ViewType.LIST.value,
            column_id='COLUMN_ID_1',
            offset=1,
            limit=-1,
            search_query="hello"
        )

    @pytest.fixture
    def task_complete_details_dto(self, task_dtos, action_dtos):
        return [
            TaskCompleteDetailsDTO(
                task_id=1,
                stage_id='STAGE_ID_1',
                stage_color="blue",
                field_dtos=FieldDetailsDTOFactory.create_batch(
                    2, field_id=factory.Iterator(
                        ['field_id_0', 'field_id_1']
                    )
                ),
                action_dtos=TaskActionsDTOFactory.create_batch(2)
            )
        ]

    @pytest.fixture
    def column_tasks_ids(self):
        task_ids = ['TASK_ID_1', 'TASK_ID_2', 'TASK_ID_3']
        stage_ids = ['STAGE_ID_1', 'STAGE_ID_2', 'STAGE_ID_3']
        return ColumnTaskIdsDTOFactory.create_batch(
            1,
            task_stage_ids=TaskStageIdDTOFactory.create_batch(
                3, task_id=factory.Iterator(task_ids),
                stage_id=factory.Iterator(stage_ids)
            )
        )

    @pytest.fixture
    def column_tasks_ids_no_duplicates(self):
        task_stage_ids = [TaskStageIdDTOFactory.create_batch(3),
                          TaskStageIdDTOFactory.create_batch(3),
                          TaskStageIdDTOFactory.create_batch(3)]
        return ColumnTaskIdsDTOFactory.create_batch(
            1, task_stage_ids=factory.Iterator(task_stage_ids)
        )

    @pytest.fixture
    def task_stage_dtos(self):
        return [
            TaskIdStageDTO(
                task_display_id="TASK_ID_1",
                task_id=1,
                stage_id="STAGE_ID_1"
            ),
            TaskIdStageDTO(
                task_display_id="TASK_ID_2",
                task_id=2,
                stage_id="STAGE_ID_2"
            )
        ]

    @pytest.fixture
    def get_task_details_dto(self):
        return GetTaskDetailsDTOFactory.create_batch(3)

    @pytest.fixture
    def task_dtos(self):
        return TaskDTOFactory.create_batch(5)

    @pytest.fixture
    def action_dtos(self):
        return TaskActionsDTOFactory.create_batch(9)

    @pytest.fixture
    def column_stage_dtos(self):
        ColumnStageIdsDTOFactory.reset_sequence()
        return ColumnStageIdsDTOFactory.create_batch(1)

    @pytest.fixture
    def assignee_dtos(self):
        StageAssigneesDTOFactory.reset_sequence()
        return StageAssigneesDTOFactory.create_batch(3)

    def test_with_valid_details_return_task_details_without_duplicates(
            self, storage_mock, presenter_mock, get_column_tasks_dto, mocker,
            task_complete_details_dto, task_dtos, assignee_dtos,
            column_tasks_ids_no_duplicates, task_stage_color_dtos,
            action_dtos, column_tasks_ids, task_stage_dtos, column_stage_dtos):
        # Arrange
        stage_ids = ['STAGE_ID_3', 'STAGE_ID_4']
        expected_response = Mock()
        project_id = "1"
        from ib_boards.tests.factories.storage_dtos import \
            FieldDisplayStatusDTOFactory
        field_display_status_dtos = FieldDisplayStatusDTOFactory.create_batch(2)
        field_ids = [
            field_display_status_dto.field_id
            for field_display_status_dto in field_display_status_dtos
        ]
        storage_mock.get_present_field_ids.return_value = field_ids
        storage_mock.get_project_id_for_given_column_id.return_value = project_id
        storage_mock.get_field_display_status_dtos.return_value = field_display_status_dtos
        storage_mock.get_field_ids_list_in_order.return_value = field_ids
        presenter_mock.get_response_for_column_tasks_in_list_view. \
            return_value = expected_response
        from ib_boards.interactors.get_column_tasks_in_list_view import \
            GetColumnTasksInteractorListView
        interactor = GetColumnTasksInteractorListView(
            storage=storage_mock
        )
        from ib_boards.tests.common_fixtures.interactors import \
            get_assignee_details_mock
        mock = get_assignee_details_mock(mocker=mocker)
        mock.return_value = assignee_dtos
        from ib_boards.interactors.presenter_interfaces.presenter_interface import \
            CompleteTasksDetailsDTO
        from ib_boards.interactors.presenter_interfaces.presenter_interface import \
            TaskDisplayIdDTO
        task_id_dtos = TaskDisplayIdDTO(
            task_id=1,
            display_id='IBWF-1'
        )
        all_fields = AllFieldsDTOFactory.create_batch(2, display_name=factory.Iterator(['KEY_1', 'KEY_2']))
        complete_tasks_details_dto = CompleteTasksDetailsDTO(
            task_actions_dtos=task_complete_details_dto[0].action_dtos,
            task_fields_dtos=task_complete_details_dto[0].field_dtos,
            total_tasks=10,
            task_id_dtos=task_id_dtos,
            task_stage_dtos=task_stage_color_dtos,
            assignees_dtos=assignee_dtos
        )
        from ib_boards.tests.common_fixtures.interactors import \
            column_tasks_interactor_mock
        interactor_mock = column_tasks_interactor_mock(mocker, complete_tasks_details_dto)
        # Act
        actual_response = interactor.get_column_tasks_wrapper(
            column_tasks_parameters=get_column_tasks_dto,
            presenter=presenter_mock
        )

        # Assert
        assert actual_response == expected_response
        storage_mock.get_present_field_ids.assert_called_once_with(
            column_id=get_column_tasks_dto.column_id,
            user_id=get_column_tasks_dto.user_id,
        )
        storage_mock.get_field_display_status_dtos.assert_called_once_with(
            column_id=get_column_tasks_dto.column_id,
            user_id=get_column_tasks_dto.user_id,
        )
        storage_mock.get_field_ids_list_in_order.assert_called_once_with(
            column_id=get_column_tasks_dto.column_id,
            user_id=get_column_tasks_dto.user_id,
        )
        presenter_mock.get_response_for_column_tasks_in_list_view. \
            assert_called_once_with(
                complete_tasks_details_dto=complete_tasks_details_dto,
                all_fields=all_fields
            )
        interactor_mock.assert_called_once_with(
            column_tasks_parameters=get_column_tasks_dto
        )
