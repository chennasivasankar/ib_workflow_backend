import datetime

import pytest
from freezegun import freeze_time

from ib_tasks.models import UserTaskDelayReason
from ib_tasks.storages.storage_implementation import StorageImplementation
from ib_tasks.tests.factories.interactor_dtos import \
    TaskDelayParametersDTOFactory
from ib_tasks.tests.factories.models import TaskModelFactory, TaskLogFactory, \
    TaskDueDetailsFactory, TaskFactory, \
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
        TaskLogFactory.reset_sequence()

    @pytest.fixture()
    @freeze_time("2020-08-10 12:30:00")
    def due_details(self):
        return TaskDelayParametersDTOFactory(
            task_id=1, due_date_time="2020-08-10 12:30:00",
            user_id="123e4567-e89b-12d3-a456-426614174000",
            stage_id=1
        )

    @pytest.fixture()
    @freeze_time("2020-08-10 12:30:00")
    def populate_data(self):
        tasks = TaskFactory.create_batch(size=4,
                                         due_date="2020-08-10 12:30:00")
        TaskLogFactory.create_batch(size=3, task=tasks[0])

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
        user_task_delay_reason_objects = UserTaskDelayReason.objects.filter(
            task_id=task_id, user_id=user_id, reason_id=reason_id)
        from ib_tasks.models import Task
        task_dicts = Task.objects.filter(
            pk=task_id, tasklog__user_id=user_id).values(
            'id', 'tasklog__user_id', 'due_date')
        counter = 1
        for task_delay_reason in user_task_delay_reason_objects:
            snapshot.assert_match(
                task_delay_reason.task_id,
                f"task_delay_reason_task_id_{counter}")
            snapshot.assert_match(
                task_delay_reason.due_datetime.__str__(),
                f"task_delay_reason_due_datetime_{counter}")
            snapshot.assert_match(
                task_delay_reason.count,
                f"task_delay_reason_count_{counter}")
            snapshot.assert_match(
                task_delay_reason.reason_id,
                f"task_delay_reason_id_{counter}")
            snapshot.assert_match(
                task_delay_reason.reason, f"task_delay_reason_{counter}")
            snapshot.assert_match(
                task_delay_reason.user_id,
                f"task_delay_reason_user_id_{counter}")
            snapshot.assert_match(
                task_delay_reason.stage_id,
                f"task_delay_reason_stage_id_{counter}")
            counter += 1
        for task_dict in task_dicts:
            snapshot.assert_match(task_dict['id'], f"task_id_{counter}")
            snapshot.assert_match(
                task_dict['tasklog__user_id'], f"task_log_user_id_{counter}")
            snapshot.assert_match(
                task_dict['due_date'].__str__(),
                f"task_due_date_{counter}")
