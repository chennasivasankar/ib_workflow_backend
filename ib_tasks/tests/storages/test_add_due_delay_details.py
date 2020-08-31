import pytest
from freezegun import freeze_time

from ib_tasks.models import UserTaskDelayReason
from ib_tasks.storages.storage_implementation import StorageImplementation
from ib_tasks.tests.factories.interactor_dtos import TaskDelayParametersDTOFactory
from ib_tasks.tests.factories.models import TaskModelFactory, TaskLogFactory, TaskDueDetailsFactory, TaskFactory, \
    StageModelFactory


@pytest.mark.django_db
class TestAddDueDelayDetails:

    @classmethod
    def setup(cls):
        TaskDelayParametersDTOFactory.reset_sequence()
        TaskModelFactory.reset_sequence()
        TaskLogFactory.reset_sequence()
        TaskDueDetailsFactory.reset_sequence()
        StageModelFactory.reset_sequence()

    @classmethod
    def teardown(cls):
        pass

    @pytest.fixture()
    def due_details(self):
        return TaskDelayParametersDTOFactory(task_id=1,
                                             due_date_time="2020-08-10 12:30:00",
                                             user_id="123e4567-e89b-12d3-a456-426614174000")

    @pytest.fixture()
    @freeze_time("2020-08-10 12:30:00")
    def populate_data(self):
        tasks = TaskFactory.create_batch(size=4, due_date="2020-08-10 12:30:00")
        TaskLogFactory.reset_sequence()
        TaskLogFactory.create_batch(size=3, task=tasks[0])
        TaskDueDetailsFactory.create_batch(task=tasks[0], size=3)

    @freeze_time("2020-08-10 12:30:00")
    def test_add_due_delay_details_given_details(self, snapshot,
                                                 populate_data, due_details):
        # Arrange
        task_id = due_details.task_id
        user_id = due_details.user_id
        reason_id = due_details.reason_id
        due_details.stage_id = 5
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

    @freeze_time("2020-08-10 12:30:00")
    def test_update_task_due_datetime_given_details(self, snapshot,
                                                    populate_data, due_details):
        # Arrange
        task_id = due_details.task_id
        user_id = due_details.user_id
        reason_id = due_details.reason_id
        due_details.stage_id = 5
        storage = StorageImplementation()

        # Act
        storage.update_task_due_datetime(due_details)

        # Assert
        from ib_tasks.models import Task
        task_due_datetime = Task.objects.filter(pk=task_id, tasklog__user_id=user_id).values(
            'id', 'tasklog__user_id', 'due_date'
        )
        snapshot.assert_match(task_due_datetime, "task_due_datetime")
