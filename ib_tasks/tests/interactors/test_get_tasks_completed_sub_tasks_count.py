import factory
import pytest

from ib_tasks.interactors.get_tasks_completed_sub_tasks_count import \
    GetTasksCompletedSubTasksCount
from ib_tasks.tests.factories.interactor_dtos import \
    TaskWithCompletedSubTasksCountDTOFactory


class TestGetTasksCompletedSubTasksCount:

    @pytest.fixture
    def task_stage_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface import \
            TaskStageStorageInterface
        return create_autospec(TaskStageStorageInterface)

    @pytest.fixture
    def task_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import \
            TaskStorageInterface
        return create_autospec(TaskStorageInterface)

    @pytest.fixture
    def all_task_ids(self):
        task_ids = [0, 1, 2, 3, 4, 5, 6]
        return task_ids

    @pytest.fixture
    def task_ids(self):
        task_ids = [0, 1, 2, 3, 4]
        return task_ids

    @pytest.fixture
    def sub_task_ids(self):
        sub_task_ids = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        return sub_task_ids

    @pytest.fixture
    def completed_sub_task_ids(self):
        completed_sub_task_ids = [7, 12, 8, 9, 10]
        return completed_sub_task_ids

    @pytest.fixture
    def task_with_sub_task_dtos(self, task_ids, sub_task_ids):
        from ib_tasks.tests.factories.storage_dtos import \
            TaskWithSubTaskDTOFactory
        task_with_sub_task_dtos = TaskWithSubTaskDTOFactory.create_batch(
            size=10, task_id=factory.Iterator(task_ids),
            sub_task_id=factory.Iterator(sub_task_ids)
        )
        return task_with_sub_task_dtos

    @pytest.fixture
    def task_with_completed_sub_task_count_dtos(self, all_task_ids):
        completed_sub_tasks_count = [2, 1, 1, 1, 0, 0, 0]
        task_with_completed_sub_task_count_dtos = \
            TaskWithCompletedSubTasksCountDTOFactory.create_batch(
                task_id=factory.Iterator(all_task_ids),
                completed_sub_tasks_count=factory.Iterator(
                    completed_sub_tasks_count
                ),
                size=7
            )
        return task_with_completed_sub_task_count_dtos

    def test_given_task_ids_returns_task_with_completed_sub_tasks_count_dtos(
            self, task_stage_storage_mock, task_storage_mock, all_task_ids,
            task_with_sub_task_dtos, task_with_completed_sub_task_count_dtos,
            completed_sub_task_ids
    ):
        # Arrange
        interactor = GetTasksCompletedSubTasksCount(
            task_stage_storage=task_stage_storage_mock,
            task_storage=task_storage_mock
        )
        task_storage_mock.get_valid_task_ids.return_value = all_task_ids
        task_storage_mock.get_task_with_sub_task_dtos.return_value = \
            task_with_sub_task_dtos
        task_stage_storage_mock.get_max_stage_value_for_the_given_template \
            .return_value = 10
        task_stage_storage_mock.get_completed_sub_task_ids.return_value = \
            completed_sub_task_ids

        # Act
        actual_task_with_completed_sub_task_count_dtos = \
            interactor.get_tasks_completed_sub_tasks_count(
                task_ids=all_task_ids
            )

        # Assert
        assert actual_task_with_completed_sub_task_count_dtos == \
               task_with_completed_sub_task_count_dtos
