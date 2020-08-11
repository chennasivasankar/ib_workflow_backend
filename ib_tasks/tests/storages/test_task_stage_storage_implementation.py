import factory
import pytest

from ib_tasks.tests.factories.models import CurrentTaskStageModelFactory, \
    TaskStageHistoryModelFactory, TaskFactory


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
        CurrentTaskStageModelFactory.reset_sequence()

    @pytest.fixture()
    def populate_task_stages(self):
        CurrentTaskStageModelFactory.reset_sequence()
        stage_ids = [1, 2, 3, 4]
        CurrentTaskStageModelFactory.create_batch(size=4, task_id=1,
                                                  stage_id=factory.Iterator(
                                                      stage_ids))

    @pytest.fixture()
    def populate_task_stages_history(self):
        TaskStageHistoryModelFactory.reset_sequence()
        stage_ids = [1, 2, 3, 4]
        TaskStageHistoryModelFactory.create_batch(size=4, task_id=1,
                                                  stage_id=factory.Iterator(
                                                      stage_ids))

    def test_given_task_id_and_stage_ids_returns_valid_stage_ids(
            self, task_storage, reset_sequence, populate_task_stages
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
            self, task_storage, reset_sequence, populate_task_stages
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

    def test_given_task_id_stage_ids_returns_task_stage_assignee_dtos(
            self, task_storage, reset_sequence,
            populate_task_stages_history, snapshot
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

    def test_given_invalid_task_id_raise_excption(self, task_storage):
        # Arrange
        task_id = 2
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskIdException
        exception_obj = InvalidTaskIdException(task_id=task_id)

        # Act
        with pytest.raises(InvalidTaskIdException) as err:
            task_storage.validate_task_id(task_id=task_id)

        # Assert
        error_obj = err.value
        assert error_obj.task_id == exception_obj.task_id

    def test_given_valid_task_id_returns_task_display_id(self, task_storage):
        # Arrange
        task_id = 1
        task_obj = TaskFactory(task_display_id="IBWF-1")

        # Act
        task_display_id = task_storage.validate_task_id(task_id=task_id)

        # Assert
        assert task_display_id == task_obj.task_display_id

    def test_task_id_returns_current_stage_ids_of_task(self, task_storage):
        # Arrange
        task_obj = TaskFactory(task_display_id="IBWF-1")
        task_id = task_obj.id
        task_stage_objs = CurrentTaskStageModelFactory.create_batch(
            size=5, task=task_obj
        )
        expected_stage_ids = [
            task_stage_obj.stage_id
            for task_stage_obj in task_stage_objs
        ]

        # Act
        actual_stage_ids = task_storage.get_task_current_stage_ids(task_id)

        # Assert
        assert expected_stage_ids == actual_stage_ids

