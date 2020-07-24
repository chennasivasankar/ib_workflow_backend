import pytest
from unittest.mock import create_autospec, patch, Mock
from ib_boards.tests.factories.storage_dtos import (
    TaskDTOFactory, TaskStagesDTOFactory, FieldsDTOFactory)
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.get_task_details_interactor import \
    GetTaskDetailsInteractor


class TestGetTaskDetailsInteractor:

    @pytest.fixture()
    def get_tasks_stage_dto(self):
        return TaskStagesDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_tasks_dto(self):
        return TaskDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def get_fields_dto(self):
        return FieldsDTOFactory.create_batch(size=2)

    def test_get_task_details_given_valid_inputs_return_task_details(
            self, mocker, get_tasks_stage_dto, snapshot, get_tasks_dto,
            get_fields_dto):

        # Arrange
        tasks_stage_dto = get_tasks_stage_dto
        task_details_response = Mock()
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        presenter = create_autospec(PresenterInterface)
        from ib_boards.tests.common_fixtures.adapters.task_service import prepare_task_details_dtos
        prepare_task_details_dtos(mocker, get_tasks_dto, user_id=user_id)
        presenter.get_response_for_task_details.return_value = task_details_response
        interactor = GetTaskDetailsInteractor()

        # Act
        result = interactor.get_task_details_wrapper(
            presenter=presenter, tasks_dtos=tasks_stage_dto, user_id=user_id,
            fields_dto=get_fields_dto)

        # Assert
        assert result == task_details_response

