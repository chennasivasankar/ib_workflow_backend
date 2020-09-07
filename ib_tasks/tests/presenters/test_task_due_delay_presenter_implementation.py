from datetime import datetime

from freezegun import freeze_time

from ib_tasks.presenters.task_due_delay_presenter_implementation import \
    TaskDueDetailsPresenterImplementation
from ib_tasks.tests.factories.adapter_dtos import AssigneeDetailsDTOFactory
from ib_tasks.tests.factories.interactor_dtos import GetTaskDueDetailsDTOFactory


class TestGetTaskDueDelay:
    def test_response_invalid_task_id(self, snapshot):
        # Arrange
        presenter = TaskDueDetailsPresenterImplementation()
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskDisplayId
        task_id = "iBWF-10"

        err = InvalidTaskDisplayId(task_id)

        # Act
        response_object = presenter.response_for_invalid_task_id(err)

        # Assert
        snapshot.assert_match(response_object.content, "response")

    def test_response_for_user_is_not_assignee_for_task(self, snapshot):
        # Arrange
        presenter = TaskDueDetailsPresenterImplementation()

        # Act
        response_object = presenter.response_for_user_is_not_assignee_for_task()

        # Assert
        snapshot.assert_match(response_object.content, "response")

    @freeze_time("2020-08-14")
    def test_get_response_for_get_task_due_details(self, snapshot):
        # Arrange
        GetTaskDueDetailsDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.adapter_dtos import AssigneeDetailsDTOFactory
        AssigneeDetailsDTOFactory.reset_sequence()
        tasks_dtos = GetTaskDueDetailsDTOFactory.create_batch(size=5,
                                                              due_date_time=datetime.now())
        presenter = TaskDueDetailsPresenterImplementation()

        # Act
        response_object = presenter.get_response_for_get_task_due_details(tasks_dtos)

        # Assert
        snapshot.assert_match(response_object.content, "response")


class TestAddTaskDueDelay:
    def test_response_for_invalid_due_datetime(self, snapshot):
        # Arrange
        presenter = TaskDueDetailsPresenterImplementation()

        # Act
        response_object = presenter.response_for_invalid_due_datetime()

        # Assert
        snapshot.assert_match(response_object.content, "response")

    def test_response_for_invalid_reason_id(self, snapshot):
        # Arrange
        presenter = TaskDueDetailsPresenterImplementation()

        # Act
        response_object = presenter.response_for_invalid_reason_id()

        # Assert
        snapshot.assert_match(response_object.content, "response")
