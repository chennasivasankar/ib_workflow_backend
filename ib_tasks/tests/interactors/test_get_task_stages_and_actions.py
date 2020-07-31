from unittest.mock import create_autospec

import pytest

from ib_tasks.interactors.get_task_stages_and_actions import GetTaskStagesAndActions
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import FieldsStorageInterface
from ib_tasks.tests.factories.storage_dtos import ActionDetailsDTOFactory, StageDetailsDTOFactory


class TestGetTaskStagesAndActions:

    @pytest.fixture()
    def get_stage_actions(self):
        ActionDetailsDTOFactory.reset_sequence()
        return ActionDetailsDTOFactory.create_batch(size=4)

    @pytest.fixture()
    def get_stage_details(self):
        StageDetailsDTOFactory.reset_sequence()
        return StageDetailsDTOFactory.create_batch(size=4)

    def test_given_valid_details_get_details(self, snapshot,
                                             get_stage_actions,
                                             get_stage_details):
        # Arrange
        task_id = 1
        storage = create_autospec(FieldsStorageInterface)
        storage.get_task_stages.return_value = ["stage_id_0", "stage_id_1", "stage_id_2"]
        storage.get_actions_details.return_value = get_stage_actions
        storage.get_stage_complete_details.return_value = get_stage_details
        interactor = GetTaskStagesAndActions(storage=storage)

        # Act
        response = interactor.get_task_stages_and_actions(task_id=task_id, user_id=1)

        # Assert
        snapshot.assert_match(response, "response")
