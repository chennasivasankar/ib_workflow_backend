from datetime import datetime, timedelta

import pytest

from ib_tasks.interactors.stages_dtos import TaskStageCompleteDetailsDTO
from ib_tasks.tests.factories.adapter_dtos import AssigneeDetailsDTOFactory, EntityTypeDTOFactory
from ib_tasks.tests.factories.storage_dtos import TaskStageHistoryDTOFactory, LogDurationDTOFactory, \
    StageMinimalDTOFactory


class TestGetTaskStagesHistory:

    @pytest.fixture()
    def task_storage(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        from unittest.mock import create_autospec
        return create_autospec(TaskStorageInterface)

    @pytest.fixture()
    def stage_storage(self):

        from unittest.mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
            import TaskStageStorageInterface
        return create_autospec(TaskStageStorageInterface)

    @pytest.fixture()
    def presenter(self):
        from ib_tasks.interactors.presenter_interfaces\
            .get_task_stages_history_presenter_interface import \
            GetTaskStagePresenterInterface
        from unittest.mock import create_autospec
        return create_autospec(GetTaskStagePresenterInterface)

    def test_given_valid_returns_task_stage_complete_details(
            self, task_storage, stage_storage, mocker, presenter):

        # Arrange
        from ib_tasks.interactors.get_task_stages_history \
            import GetTaskStagesHistory
        interactor = GetTaskStagesHistory(
            task_storage=task_storage, stage_storage=stage_storage
        )
        AssigneeDetailsDTOFactory.reset_sequence(1)
        EntityTypeDTOFactory.reset_sequence(1)
        stage_dtos = StageMinimalDTOFactory.create_batch(1)
        entity_dtos = EntityTypeDTOFactory.create_batch(1)
        stage_storage.get_stage_details.return_value = stage_dtos
        StageMinimalDTOFactory.reset_sequence(1)
        user_dtos = [
            AssigneeDetailsDTOFactory(assignee_id="1")
        ]
        assignee_ids = ['1']
        task_display_id = "1"
        task_id = 1
        TaskStageHistoryDTOFactory.reset_sequence(1)
        LogDurationDTOFactory.reset_sequence(1)
        task_storage.check_is_task_exists.return_value = True
        task_storage.check_is_valid_task_display_id.return_value = True
        task_storage.get_task_id_for_task_display_id.return_value = task_id
        task_stage_1 = TaskStageHistoryDTOFactory()
        task_stages = [task_stage_1]
        log_dtos = LogDurationDTOFactory.create_batch(1)
        stage_storage.get_task_stage_dtos.return_value = task_stages
        path1 = 'ib_tasks.adapters.utility_tools_service.UtilityToolsService.get_log_duration_dtos'
        log_mock = mocker.patch(path1)
        log_mock.return_value = log_dtos
        path2 = 'ib_tasks.adapters.assignees_details_service.AssigneeDetailsService.get_assignees_details_dtos'
        user_mock_mock = mocker.patch(path2)
        user_mock_mock.return_value = user_dtos
        task_stage_details_dto = TaskStageCompleteDetailsDTO(
            stage_dtos=stage_dtos,
            task_stage_dtos=task_stages,
            log_duration_dtos=log_dtos,
            assignee_details=user_dtos
        )

        # Act
        interactor.get_task_stages_history_wrapper(
            task_display_id=task_display_id, presenter=presenter
        )

        # Assert
        task_storage.check_is_task_exists\
            .assert_called_once_with(task_id=task_id)
        log_mock.assert_called_once_with(entity_dtos=entity_dtos)
        user_mock_mock.assert_called_once_with(assignee_ids=assignee_ids)
        presenter.get_task_stages_history_response.assert_called_once_with(
            task_stages_details_dto=task_stage_details_dto
        )

    def test_given_left_none_returns_stage_complete_details(
            self, task_storage, stage_storage, mocker, presenter):

        # Arrange
        from ib_tasks.interactors.get_task_stages_history \
            import GetTaskStagesHistory
        interactor = GetTaskStagesHistory(
            task_storage=task_storage, stage_storage=stage_storage
        )
        AssigneeDetailsDTOFactory.reset_sequence(1)
        EntityTypeDTOFactory.reset_sequence(1)
        entity_dtos = EntityTypeDTOFactory.create_batch(1)
        user_dtos = [
            AssigneeDetailsDTOFactory(assignee_id="1")
        ]
        assignee_ids = ['1']
        AssigneeDetailsDTOFactory.reset_sequence(1)
        stage_dtos = StageMinimalDTOFactory.create_batch(1)
        stage_storage.get_stage_details.return_value = stage_dtos
        task_display_id = "1"
        task_id = 1
        TaskStageHistoryDTOFactory.reset_sequence(1)
        LogDurationDTOFactory.reset_sequence(1)
        task_storage.check_is_task_exists.return_value = True
        task_storage.check_is_valid_task_display_id.return_value = True
        task_storage.get_task_id_for_task_display_id.return_value = task_id
        task_stage_1 = TaskStageHistoryDTOFactory(left_at=None)
        time_mock = mocker.patch('datetime.datetime')
        time_mock.return_value = datetime(2012, 10, 11)
        task_stages = [task_stage_1]
        log_dtos = LogDurationDTOFactory.create_batch(1)
        stage_storage.get_task_stage_dtos.return_value = task_stages
        path1 = 'ib_tasks.adapters.utility_tools_service.UtilityToolsService.get_log_duration_dtos'
        log_mock = mocker.patch(path1)
        log_mock.return_value = log_dtos
        path2 = 'ib_tasks.adapters.assignees_details_service.AssigneeDetailsService.get_assignees_details_dtos'
        user_mock_mock = mocker.patch(path2)
        user_mock_mock.return_value = user_dtos
        update_task_stage = task_stage_1
        update_task_stage.stage_duration = timedelta(days=1)
        update_task_stages_dto = [update_task_stage]
        task_stage_details_dto = TaskStageCompleteDetailsDTO(
            stage_dtos=stage_dtos,
            task_stage_dtos=update_task_stages_dto,
            log_duration_dtos=log_dtos,
            assignee_details=user_dtos
        )

        # Act
        interactor.get_task_stages_history_wrapper(
            task_display_id=task_display_id, presenter=presenter
        )

        # Assert
        task_storage.check_is_task_exists\
            .assert_called_once_with(task_id=task_id)
        log_mock.assert_called_once_with(entity_dtos=entity_dtos)
        user_mock_mock.assert_called_once_with(assignee_ids=assignee_ids)
        presenter.get_task_stages_history_response.assert_called_once_with(
            task_stages_details_dto=task_stage_details_dto
        )
