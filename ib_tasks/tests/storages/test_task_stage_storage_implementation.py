import factory
import pytest

from ib_tasks.tests.factories.models import TaskStageFactory


@pytest.mark.django_db
class TestTaskStageStorageImplementation:

    @pytest.fixture
    def task_storage(self):
        from ib_tasks.storages.task_stage_storage_implementation import \
            TaskStageStorageImplementation
        task_storage = TaskStageStorageImplementation()
        return task_storage

    @pytest.fixture
    def reset_sequence(self):
        TaskStageFactory.reset_sequence()

    @pytest.fixture()
    def populate_task_stages(self):
        stage_ids = [1, 2, 3, 4]
        TaskStageFactory.create_batch(size=4, task_id=1, stage_id=factory.Iterator(stage_ids))

    def test_given_task_id_and_stage_ids_returns_valid_stage_ids(
            self, task_storage, reset_sequence, populate_task_stages
    ):
        # Arrange
        task_id = 1
        stage_ids = [1, 2, 3, 4, 5, 6]
        TaskStageFactory.create_batch(size=4)
        expected_valid_stage_ids = [1, 2, 3, 4]

        # Act
        actual_valid_stage_ids = task_storage.get_valid_stage_ids_of_task(
            task_id=task_id,
            stage_ids=stage_ids
        )

        # Assert
        assert expected_valid_stage_ids == actual_valid_stage_ids

    def test_given_task_id_and_stage_ids_when_all_stage_ids_are_valid_returns_all_stage_ids(
            self, task_storage, reset_sequence, populate_task_stages
    ):
        # Arrange
        task_id = 1
        stage_ids = [1, 2, 3, 4]
        TaskStageFactory.create_batch(size=4)
        expected_valid_stage_ids = [1, 2, 3, 4]

        # Act
        actual_valid_stage_ids = task_storage.get_valid_stage_ids_of_task(
            task_id=task_id,
            stage_ids=stage_ids
        )

        # Assert
        assert expected_valid_stage_ids == actual_valid_stage_ids

    def test_given_task_id_stage_ids_returns_task_stage_assignee_dtos(
            self, task_storage, reset_sequence,
            populate_task_stages, snapshot
    ):
        # Arrange
        task_id = 1
        stage_ids = [1, 2, 3, 4]

        # Act
        task_stage_assignee_dtos = task_storage.get_stage_assignee_dtos(
            task_id=task_id,
            stage_ids=stage_ids
        )

        # Assert
        snapshot.assert_match(name="task_stage_assignee_dtos",
                              value=task_stage_assignee_dtos)
