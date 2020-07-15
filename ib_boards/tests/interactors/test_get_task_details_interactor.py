import pytest
from unittest.mock import create_autospec
from ib_boards.tests.factories.storage_dtos import (
    TaskStageDTOFactory, TaskFieldsDTOFactory)
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface


class TestGetTaskDetailsInteractor:

    @pytest.fixture()
    def get_tasks_stage_dto(self):
        return TaskStageDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_task_fields_dto(self):
        return TaskFieldsDTOFactory.create_batch(size=3)

    def test_get_fields_given_valid_task_ids_return_fields_details(
            self, get_tasks_stage_dto, get_task_fields_dto):

        # Arrange
        tasks_stage_dto = get_tasks_stage_dto
        task_fields_dto = get_task_fields_dto
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.get_task_fields_details.return_value = task_fields_dto
        interactor = GetTaskDetailsInteractor(
            storage=storage
        )

        # Act
        interactor.get_task_details_wrapper(presenter=presenter,
                                            tasks_stage_dto=tasks_stage_dto)

        # Assert


