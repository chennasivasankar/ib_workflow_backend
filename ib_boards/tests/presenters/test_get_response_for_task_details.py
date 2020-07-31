import pytest

from ib_boards.presenters.presenter_implementation import \
    PresenterImplementation
from ib_boards.tests.factories.interactor_dtos import TaskColumnDTOFactory
from ib_boards.tests.factories.storage_dtos import (
    TaskDTOFactory, TaskActionsDTOFactory, TaskFieldsDTOFactory)


class TestTaskDetailsResponse:

    @pytest.fixture()
    def get_tasks_dto(self):
        TaskDTOFactory.reset_sequence()
        return TaskDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_task_actions_dtos(self):
        TaskActionsDTOFactory.reset_sequence()
        return TaskActionsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_task_fields_dtos(self):
        TaskFieldsDTOFactory.reset_sequence()
        return TaskFieldsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_column_task_details(self):
        TaskColumnDTOFactory.reset_sequence()
        return TaskColumnDTOFactory.create_batch(size=3)

    def test_get_response_for_task_details(self, get_task_fields_dtos,
                                           get_column_task_details,
                                           get_task_actions_dtos, snapshot):
        # Arrange
        task_fields_dtos = get_task_fields_dtos
        task_actions_dtos = get_task_actions_dtos
        presenter = PresenterImplementation()

        # Act
        response = presenter.get_response_for_task_details(
            task_details=get_column_task_details,
            task_fields_dto=task_fields_dtos,
            task_actions_dto=task_actions_dtos)

        # Assert
        import json
        print(response)
        result = json.loads(response.content)

        snapshot.assert_match(result, "list_of_task_details")
