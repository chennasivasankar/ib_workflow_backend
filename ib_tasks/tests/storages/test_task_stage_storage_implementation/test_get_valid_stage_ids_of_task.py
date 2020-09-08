import factory
import pytest

from ib_tasks.tests.factories.models import CurrentTaskStageModelFactory


@pytest.mark.django_db
class TestGetValidStageIdsOfTask:

    @pytest.fixture()
    def populate_task_stages(self):
        CurrentTaskStageModelFactory.reset_sequence()
        stage_ids = [1, 2, 3, 4]
        CurrentTaskStageModelFactory.create_batch(size=4, task_id=1,
                                                  stage_id=factory.Iterator(
                                                      stage_ids))

    def test_given_task_id_and_stage_ids_returns_valid_stage_ids(
            self, task_storage, populate_task_stages
    ):
        # Arrange
        CurrentTaskStageModelFactory.reset_sequence()
        task_id = 1
        stage_ids = [1, 2, 3, 4, 5, 6]
        CurrentTaskStageModelFactory.create_batch(size=4)
        expected_valid_stage_ids = [1, 2, 3, 4]

        # Act
        actual_valid_stage_ids = task_storage.get_valid_stage_ids_of_task(
            task_id=task_id,
            stage_ids=stage_ids
        )

        # Assert
        assert expected_valid_stage_ids == actual_valid_stage_ids

    def test_given_task_id_and_stage_ids_when_all_stage_ids_are_valid_returns_all_stage_ids(
            self, task_storage, populate_task_stages
    ):
        # Arrange
        CurrentTaskStageModelFactory.reset_sequence()
        task_id = 1
        stage_ids = [1, 2, 3, 4]
        CurrentTaskStageModelFactory.create_batch(size=4)
        expected_valid_stage_ids = [1, 2, 3, 4]

        # Act
        actual_valid_stage_ids = task_storage.get_valid_stage_ids_of_task(
            task_id=task_id,
            stage_ids=stage_ids
        )

        # Assert
        assert expected_valid_stage_ids == actual_valid_stage_ids
