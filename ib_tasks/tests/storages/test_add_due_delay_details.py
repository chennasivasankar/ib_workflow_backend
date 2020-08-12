import pytest
from freezegun import freeze_time

from ib_tasks.models import UserTaskDelayReason
from ib_tasks.storages.storage_implementation import StorageImplementation
from ib_tasks.tests.factories.interactor_dtos import TaskDueParametersDTOFactory
from ib_tasks.tests.factories.models import TaskModelFactory, TaskStageFactory


@pytest.mark.django_db
class TestAddDueDelayDetails:

    @classmethod
    def setup(cls):
        TaskDueParametersDTOFactory.reset_sequence()
        TaskModelFactory.reset_sequence()
        TaskStageFactory.reset_sequence()

    @classmethod
    def teardown(cls):
        pass

    @pytest.fixture()
    def due_details(self):
        return TaskDueParametersDTOFactory(task_id=1,
                                           user_id="123e4567-e89b-12d3-a456-426614174000")

    @pytest.fixture()
    def populate_data(self):

        tasks = TaskModelFactory.create_batch(size=4)
        TaskStageFactory.create_batch(task=tasks[0], size=3)

    @freeze_time("2020-08-10 12:30:00")
    def test_add_due_delay_details_given_details(self, snapshot,
                                                 populate_data, due_details):
        # Arrange
        task_id = due_details.task_id
        user_id = due_details.user_id
        reason_id = due_details.reason_id
        storage = StorageImplementation()

        # Act
        storage.add_due_delay_details(due_details)

        # Assert
        reason = UserTaskDelayReason.objects.filter(
            task_id=task_id, user_id=user_id, reason_id=reason_id).values()
        from ib_tasks.models import Task
        task_due_datetime = Task.objects.filter(pk=task_id, tasklog__user_id=user_id).values(
            'id', 'tasklog__user_id', 'due_date'
        )
        snapshot.assert_match(task_due_datetime, "task_due_datetime")
        snapshot.assert_match(reason, "reason")
