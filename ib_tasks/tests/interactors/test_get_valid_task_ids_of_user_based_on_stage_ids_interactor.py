"""
Created on: 08/08/20
Author: Pavankumar Pamuru

"""
import pytest


class TestGetTaskIdsOfUserBasedOnStagesInteractor:
    @pytest.fixture()
    def task_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        storage = create_autospec(TaskStorageInterface)
        return storage

    @pytest.fixture()
    def stage_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface \
            import StageStorageInterface

        storage = create_autospec(StageStorageInterface)
        return storage

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        UserStagesWithPaginationDTOFactory.reset_sequence()

    def test_given_valid_stage_ids_get_tasks_with_max_stage_value_dtos(
            self, task_storage_mock, stage_storage_mock):
        # Arrange
        valid_stage_ids = ["stage_id_1", "stage_id_2"]
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        user_stages_with_pagination_dto = UserStagesWithPaginationDTOFactory()
        user_id = user_stages_with_pagination_dto.user_id
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.return_value \
            = valid_stage_ids

        from ib_tasks.interactors.storage_interfaces.stage_dtos import \
            TaskIdWithStageValueDTO, StageValueWithTaskIdsDTO
        task_storage_mock. \
            get_user_task_ids_and_max_stage_value_dto_based_on_given_stage_ids. \
            return_value = \
            [TaskIdWithStageValueDTO(task_id=1, stage_value=2),
             TaskIdWithStageValueDTO(task_id=2, stage_value=2)]
        task_ids_group_by_stage_value_dtos = [
            StageValueWithTaskIdsDTO(stage_value=2,
                                     task_ids=[1, 2])
        ]

        from ib_tasks.interactors. \
            get_valid_task_ids_for_user_based_on_stage_ids import \
            GetTaskIdsOfUserBasedOnStagesInteractor
        # Act
        interactor = GetTaskIdsOfUserBasedOnStagesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock)
        interactor.get_task_ids_of_user_based_on_stage_ids(
            user_id=user_id,
            stage_ids=valid_stage_ids

        )

        # Assert
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids. \
            assert_called_once_with(user_stages_with_pagination_dto.stage_ids)
        task_storage_mock. \
            get_user_task_ids_and_max_stage_value_dto_based_on_given_stage_ids. \
            assert_called_once_with(
            user_id=user_id,
            stage_ids=valid_stage_ids)
        stage_storage_mock. \
            get_task_id_with_stage_details_dtos_based_on_stage_value(
            stage_values=[2],
            task_ids_group_by_stage_value_dtos=
            task_ids_group_by_stage_value_dtos,
            user_id=user_id)
