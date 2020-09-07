import pytest
from freezegun import freeze_time

from ib_tasks.storages.storage_implementation import StorageImplementation
from ib_tasks.tests.factories.interactor_dtos import \
    TaskDelayParametersDTOFactory
from ib_tasks.tests.factories.models import TaskModelFactory, TaskLogFactory, \
    TaskDueDetailsFactory, TaskFactory, \
    StageModelFactory


@pytest.mark.django_db
class TestUpdateTaskDueDateTime:

    @classmethod
    def setup(cls):
        TaskDelayParametersDTOFactory.reset_sequence()
        TaskModelFactory.reset_sequence()
        TaskLogFactory.reset_sequence()
        TaskDueDetailsFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        TaskLogFactory.reset_sequence()

    @pytest.fixture()
    def due_details(self):
        return TaskDelayParametersDTOFactory(
            task_id=1, due_date_time="2020-08-10 12:30:00",
            user_id="123e4567-e89b-12d3-a456-426614174000")

    @pytest.fixture()
    @freeze_time("2020-08-10 12:30:00")
    def populate_data(self):
        tasks = TaskFactory.create_batch(size=4,
                                         due_date="2020-08-10 12:30:00")
        TaskLogFactory.create_batch(size=3, task=tasks[0])
        TaskDueDetailsFactory.create_batch(task=tasks[0], size=3)

    @freeze_time("2020-08-10 12:30:00")
    def test_update_task_due_datetime_given_details(
            self, snapshot, populate_data, due_details):
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
        task_dicts = Task.objects.filter(
            pk=task_id, tasklog__user_id=user_id).values(
            'id', 'tasklog__user_id', 'due_date')
        counter = 1
        for task_dict in task_dicts:
            snapshot.assert_match(task_dict['id'], f"task_id_{counter}")
            snapshot.assert_match(
                task_dict['tasklog__user_id'], f"task_log_user_id_{counter}")
            snapshot.assert_match(
                task_dict['due_date'], f"due_date_{counter}")
            counter += 1
