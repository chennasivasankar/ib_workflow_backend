import pytest
from unittest.mock import create_autospec, patch, Mock
from ib_boards.tests.factories.storage_dtos import (
    TaskDTOFactory)
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.get_task_details_interactor import \
    GetTaskDetailsInteractor


class TestGetTaskDetailsInteractor:

    @pytest.fixture()
    def get_tasks_stage_dto(self):
        return TaskDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def task_details_response(self):
        task_details = [{
            "task_id": "task_id_0",
            "fields": [{
                "field_type": "field_type_0",
                "key": "key_0",
                "value": "value_0"
            }],
            "actions": [{
                "action_id": "action_id_0",
                "name": "name_0",
                "button_text": "button_text_0",
                "button_color": None
            }]
        },
            {
                "task_id": "task_id_1",
                "fields": [{
                    "field_type": "field_type_1",
                    "key": "key_1",
                    "value": "value_1"
                }],
                "actions": [{
                    "action_id": "action_id_1",
                    "name": "name_1",
                    "button_text": "button_text_1",
                    "button_color": None
                }]
            },
            {
                "task_id": "task_id_2",
                "fields": [{
                    "field_type": "field_type_2",
                    "key": "key_2",
                    "value": "value_2"
                }],
                "actions": [{
                    "action_id": "action_id_2",
                    "name": "name_2",
                    "button_text": "button_text_2",
                    "button_color": None
                }]
            }
        ]
        return task_details

    def test_get_task_details_given_valid_inputs_return_task_details(
            self, mocker, get_tasks_stage_dto, snapshot, task_details_response):

        # Arrange
        tasks_stage_dto = get_tasks_stage_dto
        task_details_response = Mock()
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        presenter = create_autospec(PresenterInterface)
        from ib_boards.tests.common_fixtures.adapters.task_service import prepare_task_details_dtos
        prepare_task_details_dtos(mocker, tasks_stage_dto, user_id=user_id)
        presenter.get_response_for_task_details.return_value = task_details_response
        interactor = GetTaskDetailsInteractor()

        # Act
        result = interactor.get_task_details_wrapper(
            presenter=presenter, tasks_dtos=tasks_stage_dto, user_id=user_id)

        # Assert
        assert  result == task_details_response

