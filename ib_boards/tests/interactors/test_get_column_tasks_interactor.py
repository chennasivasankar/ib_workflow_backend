"""
Created on: 16/07/20
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
from ib_boards.tests.factories.interactor_dtos import ActionDTOFactory, \
    FieldDetailsDTOFactory, GetTaskDetailsDTOFactory, \
    ColumnTaskIdsDTOFactory, TaskStageIdDTOFactory, ColumnStageIdsDTOFactory
from ib_boards.tests.factories.storage_dtos import TaskDTOFactory, TaskStageColorDTOFactory
    ColumnTaskIdsDTOFactory, TaskStageIdDTOFactory
from ib_boards.tests.factories.storage_dtos import TaskDTOFactory, TaskStageDTOFactory
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO


class TestGetColumnTasksInteractor:

    @pytest.fixture
    def task_stage_color_dtos(self):
        TaskStageColorDTOFactory.reset_sequence()
        return TaskStageColorDTOFactory.create_batch(size=3)

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
            GetColumnTasksPresenterInterface
        presenter = mock.create_autospec(GetColumnTasksPresenterInterface)
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
                field_dtos=FieldDetailsDTOFactory.create_batch(2),
                action_dtos=ActionDTOFactory.create_batch(2)
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
                task_id="TASK_ID_1",
                stage_id="STAGE_ID_1"
            ),
            TaskIdStageDTO(
                task_id="TASK_ID_2",
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
        return ActionDTOFactory.create_batch(9)

    @pytest.fixture
    def column_stage_dtos(self):
        ColumnStageIdsDTOFactory.reset_sequence()
        return ColumnStageIdsDTOFactory.create_batch(1)

    def test_with_invalid_column_id_return_error_message(
            self, presenter_mock, storage_mock, get_column_tasks_dto):
        # Arrange
        expected_response = Mock()
        column_id = 'COLUMN_ID_1'
        from ib_boards.exceptions.custom_exceptions import InvalidColumnId
        storage_mock.validate_column_id.side_effect = InvalidColumnId
        presenter_mock.get_response_for_the_invalid_column_id. \
            return_value = expected_response

        interactor = GetColumnTasksInteractor(
            storage=storage_mock
        )
        # Act
        actual_response = interactor.get_column_tasks_wrapper(
            column_tasks_parameters=get_column_tasks_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.validate_column_id.assert_called_once_with(
            column_id=column_id
        )
        presenter_mock.get_response_for_the_invalid_column_id.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_invalid_offset_value_return_error_message(
            self, storage_mock, presenter_mock,
            get_column_tasks_dto_with_invalid_offset):
        # Arrange
        expected_response = Mock()
        interactor = GetColumnTasksInteractor(
            storage=storage_mock
        )
        presenter_mock.get_response_for_invalid_offset. \
            return_value = expected_response

        # Act
        actual_response = interactor.get_column_tasks_wrapper(
            column_tasks_parameters=get_column_tasks_dto_with_invalid_offset,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.get_response_for_invalid_offset.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_invalid_limit_value_return_error_message(
            self, storage_mock, presenter_mock,
            get_column_tasks_dto_with_invalid_limit):
        # Arrange
        expected_response = Mock()
        interactor = GetColumnTasksInteractor(
            storage=storage_mock
        )
        presenter_mock.get_response_for_invalid_limit. \
            return_value = expected_response

        # Act
        actual_response = interactor.get_column_tasks_wrapper(
            column_tasks_parameters=get_column_tasks_dto_with_invalid_limit,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.get_response_for_invalid_limit.assert_called_once_with()
        assert actual_response == expected_response

    def test_with_user_id_not_have_permission_for_column_return_error_message(
            self, storage_mock, presenter_mock, get_column_tasks_dto, mocker):
        # Arrange
        user_role = 'User'
        column_id = 'COLUMN_ID_1'
        expected_response = Mock()
        interactor = GetColumnTasksInteractor(
            storage=storage_mock
        )
        from ib_boards.exceptions.custom_exceptions import \
            UserDoNotHaveAccessToColumn
        storage_mock.validate_user_role_with_column_roles. \
            side_effect = UserDoNotHaveAccessToColumn
        presenter_mock.get_response_for_user_have_no_access_for_column. \
            return_value = expected_response

        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )

        # Act
        actual_response = interactor.get_column_tasks_wrapper(
            column_tasks_parameters=get_column_tasks_dto,
            presenter=presenter_mock
        )

        # Assert
        adapter_mock.assert_called_once_with(
            user_id=get_column_tasks_dto.user_id
        )
        storage_mock.validate_user_role_with_column_roles.assert_called_once_with(
            user_role=user_role, column_id=column_id
        )
        presenter_mock.get_response_for_user_have_no_access_for_column. \
            assert_called_once_with()
        assert actual_response == expected_response

    def test_with_valid_details_return_task_details(
            self, storage_mock, presenter_mock, get_column_tasks_dto, mocker,
            task_complete_details_dto, task_dtos,
            action_dtos, column_tasks_ids, task_stage_dtos,
            get_task_details_dto, task_stage_color_dtos, column_stage_dtos):
        # Arrange
        view_type = get_column_tasks_dto.view_type
        stage_ids = ['STAGE_ID_1', 'STAGE_ID_2']
        task_ids = ['TASK_ID_1', 'TASK_ID_2', 'TASK_ID_3']
        expected_response = Mock()
        storage_mock.get_columns_stage_ids.return_value = column_stage_dtos
        presenter_mock.get_response_for_column_tasks. \
            return_value = expected_response
        interactor = GetColumnTasksInteractor(
            storage=storage_mock
        )
        user_id = 'user_id_1'
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            task_details_mock
        task_details_mock = task_details_mock(mocker, task_complete_details_dto)
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_task_ids_mock

        task_ids_mock = get_task_ids_mock(mocker, column_tasks_ids)
        task_config_dto = [
            TaskDetailsConfigDTO(
                unique_key=get_column_tasks_dto.column_id,
                stage_ids=stage_ids,
                offset=get_column_tasks_dto.offset,
                limit=get_column_tasks_dto.limit,
                user_id='user_id_1',
                search_query="hello"
            )
        ]
        user_role = 'User'
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )

        # Act
        actual_response = interactor.get_column_tasks_wrapper(
            column_tasks_parameters=get_column_tasks_dto,
            presenter=presenter_mock
        )

        # Assert
        assert actual_response == expected_response
        task_ids_mock.assert_called_once_with(
            task_config_dtos=task_config_dto
        )
        task_details_mock.assert_called_once_with(
            get_task_details_dto, user_id=user_id, view_type=view_type
        )
        presenter_mock.get_response_for_column_tasks.assert_called_once_with(
            task_actions_dtos=task_complete_details_dto[0].action_dtos,
            task_fields_dtos=task_complete_details_dto[0].field_dtos,
            total_tasks=10,
            task_ids=task_ids,
            task_stage_dtos=task_stage_color_dtos
        )

    def test_with_valid_details_return_task_details_without_duplicates(
            self, storage_mock, presenter_mock, get_column_tasks_dto, mocker,
            task_complete_details_dto, task_dtos,
            column_tasks_ids_no_duplicates, task_stage_color_dtos,
            action_dtos, column_tasks_ids, task_stage_dtos, column_stage_dtos):

        # Arrange
        stage_ids = ['STAGE_ID_3', 'STAGE_ID_4']
        task_ids = ['TASK_ID_7', 'TASK_ID_8', 'TASK_ID_9']
        expected_response = Mock()
        storage_mock.get_columns_stage_ids.return_value = column_stage_dtos
        presenter_mock.get_response_for_column_tasks. \
            return_value = expected_response
        interactor = GetColumnTasksInteractor(
            storage=storage_mock
        )

        from ib_boards.tests.common_fixtures.adapters.task_service import \
            task_details_mock
        task_details_mock(mocker, task_complete_details_dto)
        from ib_boards.tests.common_fixtures.adapters.task_service import \
            get_task_ids_mock

        task_ids_mock = get_task_ids_mock(mocker,
                                          column_tasks_ids_no_duplicates)
        task_config_dto = [
            TaskDetailsConfigDTO(
                unique_key=get_column_tasks_dto.column_id,
                stage_ids=stage_ids,
                offset=get_column_tasks_dto.offset,
                limit=get_column_tasks_dto.limit,
                user_id='user_id_1',
                search_query="hello"
            )
        ]
        user_role = 'User'
        from ib_boards.tests.common_fixtures.adapters.iam_service import \
            adapter_mock_to_get_user_role
        adapter_mock = adapter_mock_to_get_user_role(
            mocker=mocker, user_role=user_role
        )

        # Act
        actual_response = interactor.get_column_tasks_wrapper(
            column_tasks_parameters=get_column_tasks_dto,
            presenter=presenter_mock
        )

        # Assert
        assert actual_response == expected_response
        task_ids_mock.assert_called_once_with(
            task_config_dtos=task_config_dto
        )
        presenter_mock.get_response_for_column_tasks.assert_called_once_with(
            task_actions_dtos=task_complete_details_dto[0].action_dtos,
            task_fields_dtos=task_complete_details_dto[0].field_dtos,
            total_tasks=10,
            task_ids=task_ids,
            task_stage_dtos=task_stage_color_dtos
        )
